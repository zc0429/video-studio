#!/usr/bin/env python3
"""Inspect output metadata, decoded-frame timestamps and optional full decode. Does not prove native source fps."""
import argparse,json,subprocess,math
from fractions import Fraction
from pathlib import Path

def check_frame_timing(frames,fps,time_base='0/1'):
    """Compare decoded presentation timestamps with a uniform grid, allowing time-base quantization."""
    if not math.isfinite(fps) or fps<=0:raise ValueError('fps must be positive and finite')
    tolerance=max(abs(float(Fraction(time_base)))*1.1,1e-5)
    timestamps=[];errors=[]
    for frame in frames:
        value=frame.get('best_effort_timestamp_time',frame.get('pts_time'))
        if value is None:errors.append('frame timestamp is missing');break
        timestamp=float(value)
        if not math.isfinite(timestamp):errors.append('frame timestamp is not finite');break
        timestamps.append(timestamp)
    if len(timestamps)<2:errors.append('too few timestamps to verify constant frame rate')
    if any(b<=a for a,b in zip(timestamps,timestamps[1:])):errors.append('frame timestamps are not strictly increasing')
    deviation=max((abs((ts-timestamps[0])-i/fps) for i,ts in enumerate(timestamps)),default=0)
    if deviation>tolerance:errors.append('frame timestamps do not match the constant-fps grid')
    return {'checked':True,'constant':not errors,'frames_checked':len(timestamps),'max_grid_error_s':deviation,'tolerance_s':tolerance,'errors':errors}

def inspect_video(video,project=None,decode=False):
    raw=subprocess.check_output(['ffprobe','-v','error','-count_frames','-show_streams','-show_format','-of','json',str(video)],stderr=subprocess.STDOUT)
    d=json.loads(raw);v=next(s for s in d['streams'] if s.get('codec_type')=='video');a=[s for s in d['streams'] if s.get('codec_type')=='audio']
    fps=float(Fraction(v.get('avg_frame_rate','0/1')));dur=float(d['format']['duration']);count=int(v.get('nb_read_frames',v.get('nb_frames','0')))
    errors=[];timing={'checked':False,'constant':None};f=project['format'] if project else None
    if f:
        target=float(f['fps']);tol=max(1/target,.001)+.002
        if (v['width'],v['height'])!=(f['width'],f['height']):errors.append('resolution mismatch')
        if abs(fps-target)>.001:errors.append('output frame rate mismatch')
        if abs(dur-f['duration_s'])>tol:errors.append('duration mismatch')
        if count!=round(target*f['duration_s']):errors.append('frame count mismatch')
        if project.get('audio',{}).get('required',False) and not a:errors.append('required audio stream is missing')
    if f and f.get('frame_rate_mode','cfr')=='cfr':
        raw_frames=subprocess.check_output(['ffprobe','-v','error','-select_streams','v:0','-show_frames','-show_entries','frame=best_effort_timestamp_time,pts_time','-of','json',str(video)],stderr=subprocess.STDOUT)
        timing=check_frame_timing(json.loads(raw_frames).get('frames',[]),float(f['fps']),v.get('time_base','0/1'))
        errors.extend(timing['errors'])
        if timing['frames_checked']!=count:errors.append('timestamp count differs from decoded frame count')
    if decode:subprocess.run(['ffmpeg','-v','error','-xerror','-i',str(video),'-f','null','-'],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
    return {'passed':not errors,'width':v['width'],'height':v['height'],'output_fps':fps,'read_frames':count,'duration_s':dur,'video_codec':v['codec_name'],'pixel_format':v.get('pix_fmt'),'audio_streams':len(a),'frame_timing':timing,'full_decode':bool(decode),'errors':errors,'native_source_fps_verified':False,'review_scope':'Technical checks only. Uniform timestamps can still contain duplicated/interpolated images. Source cadence, story, image quality, audio listening and actual remote delivery require separate evidence.'}

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('video',type=Path);ap.add_argument('--project',type=Path);ap.add_argument('--decode',action='store_true');args=ap.parse_args()
    try:
        project=json.loads(args.project.read_text()) if args.project else None
        report=inspect_video(args.video,project,args.decode)
    except (OSError,ValueError,KeyError,TypeError,ZeroDivisionError,StopIteration,subprocess.CalledProcessError) as e:
        report={'passed':False,'error':str(e)}
    print(json.dumps(report,ensure_ascii=False,indent=2,allow_nan=False));return 0 if report['passed'] else 2
if __name__=='__main__':raise SystemExit(main())
