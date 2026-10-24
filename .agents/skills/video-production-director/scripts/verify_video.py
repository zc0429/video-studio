#!/usr/bin/env python3
"""Inspect output metadata/frame count; optional full ffmpeg decode. Does not prove aesthetics or native source fps."""
import argparse,json,subprocess
from fractions import Fraction
from pathlib import Path

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('video',type=Path);ap.add_argument('--project',type=Path);ap.add_argument('--decode',action='store_true');args=ap.parse_args()
    try:
        raw=subprocess.check_output(['ffprobe','-v','error','-count_frames','-show_streams','-show_format','-of','json',str(args.video)],stderr=subprocess.STDOUT)
        d=json.loads(raw);v=next(s for s in d['streams'] if s.get('codec_type')=='video');a=[s for s in d['streams'] if s.get('codec_type')=='audio']
        fps=float(Fraction(v.get('avg_frame_rate','0/1')));dur=float(d['format']['duration']);count=int(v.get('nb_read_frames',v.get('nb_frames','0')))
        errors=[]
        if args.project:
            p=json.loads(args.project.read_text());f=p['format'];tol=max(1/float(f['fps']),.001)+.002
            if (v['width'],v['height'])!=(f['width'],f['height']):errors.append('resolution mismatch')
            if abs(fps-f['fps'])>.001:errors.append('output frame rate mismatch')
            if abs(dur-f['duration_s'])>tol:errors.append('duration mismatch')
            if count!=round(f['fps']*f['duration_s']):errors.append('frame count mismatch')
        if args.decode:subprocess.run(['ffmpeg','-v','error','-xerror','-i',str(args.video),'-f','null','-'],check=True)
        report={'passed':not errors,'width':v['width'],'height':v['height'],'output_fps':fps,'read_frames':count,'duration_s':dur,'video_codec':v['codec_name'],'pixel_format':v.get('pix_fmt'),'audio_streams':len(a),'full_decode':bool(args.decode),'errors':errors,'native_source_fps_verified':False,'review_scope':'Technical checks only. Source cadence, retiming/interpolation, story, image quality, audio listening and actual remote delivery require separate evidence.'}
        print(json.dumps(report,ensure_ascii=False,indent=2));return 0 if not errors else 2
    except (OSError,ValueError,KeyError,StopIteration,subprocess.CalledProcessError) as e:
        print(json.dumps({'passed':False,'error':str(e)},ensure_ascii=False));return 2
if __name__=='__main__':raise SystemExit(main())
