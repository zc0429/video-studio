#!/usr/bin/env python3
"""Deterministic planning checks. Does not score art, grant approval, or generate media."""
import argparse,json,math
from pathlib import Path

def check_project(p,phase=None):
    errors=[];warnings=[];derived={}
    def error(s):errors.append(s)
    def warning(s):warnings.append(s)
    def num(x):return isinstance(x,(int,float)) and not isinstance(x,bool) and math.isfinite(x)
    if p.get('schema_version')!='1.0':error('schema_version must be 1.0')
    if not p.get('project_id'):error('project_id is missing')
    mode=phase or p.get('phase','development')
    if mode not in ('development','production','delivery'):error('invalid phase')
    producing=mode in ('production','delivery')
    brief=p.get('brief',{})
    for key in ('audience','premise','viewer_takeaway'):
        if not isinstance(brief.get(key),str) or not brief[key].strip():error('brief.'+key+' is missing')
    fmt=p.get('format',{});fps=fmt.get('fps');duration=fmt.get('duration_s')
    if not num(fps) or fps<=0:error('format.fps must be positive')
    if fmt.get('frame_rate_mode','cfr') not in ('cfr','vfr'):error('format.frame_rate_mode must be cfr or vfr')
    if duration is None and not producing:
        warning('format.duration_s is unresolved; select it from the script and animatic before production')
    elif not num(duration) or duration<=0:error('format.duration_s must be positive before production')
    for key in ('width','height'):
        v=fmt.get(key)
        if not isinstance(v,int) or isinstance(v,bool) or v<=0:error('format.'+key+' must be a positive integer')
        elif v%2:warning('odd '+key+' may need padding for yuv420p')
    if num(fps) and fps>0 and num(duration) and duration>0:
        count=round(fps*duration);derived.update(expected_frames=count,quantized_duration_s=count/fps)
        if abs(count-fps*duration)>1e-5:(error if producing else warning)('requested duration is not exactly on the frame grid; choose a final frame count')
    clearance=p.get('text_clearance_px')
    if not num(clearance) or clearance<0:error('text_clearance_px must be non-negative')
    approvals=p.get('approvals',{})
    for key in ('script','look','animatic','pilot'):
        a=approvals.get(key,{})
        ready=a.get('status') in ('approved','delegated')
        if ready and not str(a.get('basis','')).strip():error(key+' approval/delegation has no recorded basis')
        if producing and not ready:error(key+' is not ready for production; reuse existing authorization if already given')
    g=p.get('generation',{});limit=g.get('max_trials_per_shot',2)
    if not isinstance(g.get('enabled',False),bool):error('generation.enabled must be a boolean')
    if g.get('enabled') and not isinstance(g.get('requires_paid_jobs'),bool):
        (error if producing else warning)('enabled generation must explicitly declare requires_paid_jobs true or false')
    if not isinstance(limit,int) or isinstance(limit,bool) or limit<1:error('max_trials_per_shot must be a positive integer');limit=2
    cap=g.get('approved_budget');spent=g.get('spent',0)
    if not num(spent) or spent<0:error('generation.spent must be non-negative')
    if cap is not None:
        if not num(cap) or cap<0:error('approved_budget must be non-negative or null')
        elif num(spent) and spent>cap:error('recorded spending exceeds approved budget')
        if not g.get('unit'):error('budget unit is missing')
    if producing and g.get('enabled') and g.get('requires_paid_jobs') and cap is None:error('paid generation has no authorized budget')
    shots=p.get('shots',[])
    if not isinstance(shots,list):error('shots must be a list');shots=[]
    if not shots:(error if producing else warning)('no shots yet; storyboard is still in development')
    previous=0;valid_timeline=True;ids=set()
    for i,s in enumerate(shots):
        sid=s.get('id','shot-'+str(i+1))
        if sid in ids:error('duplicate shot id: '+sid)
        ids.add(sid)
        if not str(s.get('purpose','')).strip():error(sid+': narrative/perceptual purpose is missing')
        start=s.get('start_s');end=s.get('end_s')
        if not num(start) or not num(end) or start<0 or end<=start:error(sid+': invalid interval');valid_timeline=False
        else:
            if abs(start-previous)>1e-4:error(sid+': story-unit timeline has a gap or overlap')
            previous=end
        if s.get('method') not in ('code','blender','generative','footage','composite'):(error if producing else warning)(sid+': method has not been selected')
        source=s.get('source_fps')
        if num(source) and source<=0:error(sid+': source_fps must be positive when numeric')
        if num(source) and num(fps) and abs(source-fps)>1e-4:
            if s.get('fps_conversion') not in ('duplicate','interpolate','retime','render_at_output_fps'):
                (error if producing else warning)(sid+': mismatched source/output fps needs a recorded fps_conversion method')
        if fmt.get('native_fps_claim'):
            analytic=source=='per_frame' and s.get('method') in ('code','blender')
            if not analytic and (not num(source) or not num(fps) or abs(source-fps)>1e-4):error(sid+': source cadence does not support the native-fps claim')
        trials=s.get('trials',[])
        if len(trials)>limit and not s.get('trial_limit_override_reason'):error(sid+': trial limit exceeded without a recorded revised policy')
        for j,tr in enumerate(trials):
            for k in ('hypothesis','changed_variable'):
                if not str(tr.get(k,'')).strip():error(f'{sid} trial {j+1}: {k} is missing')
            if tr.get('result')=='fail' and not str(tr.get('diagnosis','')).strip():error(f'{sid} trial {j+1}: failure has no diagnosis')
    if shots and valid_timeline and num(duration) and abs(previous-duration)>1e-4:error('story-unit timeline does not end at the requested duration')
    for asset in p.get('assets',[]):
        if asset.get('usage')=='export' and asset.get('rights_status') not in ('licensed','owned','public_domain','generated_with_verified_terms'):
            (error if producing else warning)('export asset has unresolved usage terms: '+str(asset.get('id','unnamed')))
    return {'passed':not errors,'phase':mode,'errors':errors,'warnings':warnings,'derived':derived,
            'limits':'Config checks only: no aesthetic judgment, no factual verification, no proof of actual approval or native frame generation.'}

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('project',type=Path);ap.add_argument('--phase',choices=['development','production','delivery']);ap.add_argument('--json',action='store_true');args=ap.parse_args()
    try:p=json.loads(args.project.read_text(encoding='utf-8'));report=check_project(p,args.phase)
    except (OSError,ValueError,TypeError,AttributeError) as e:report={'passed':False,'errors':['Unable to read project configuration: '+str(e)],'warnings':[]}
    if args.json:print(json.dumps(report,ensure_ascii=False,indent=2))
    else:
        print('PASS' if report['passed'] else 'NOT READY')
        for k in ('errors','warnings'):
            for line in report.get(k,[]):print(k.upper()+': '+line)
        if report.get('derived'):print('DERIVED:',json.dumps(report['derived'],ensure_ascii=False))
        print(report.get('limits',''))
    raise SystemExit(0 if report['passed'] else 2)
if __name__=='__main__':main()
