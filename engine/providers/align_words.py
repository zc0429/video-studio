"""Offline ASR word timestamp refinement; explicit uncertainty, never claimed forced alignment."""
from pathlib import Path
import argparse,json,re,difflib
import numpy as np,soundfile as sf,jieba
from scipy.signal import resample_poly
from faster_whisper import WhisperModel
from pypinyin import lazy_pinyin
p=argparse.ArgumentParser();p.add_argument('timeline');a=p.parse_args();file=Path(a.timeline);tl=json.loads(file.read_text());root=file.parent
model=WhisperModel('small',device='cpu',compute_type='int8',cpu_threads=2,num_workers=1)
all_reports=[]
for shot in tl['shots']:
 audio,sr=sf.read(root/shot['audio']);pcm=resample_poly(audio,16000,sr).astype('float32')
 segs,info=model.transcribe(pcm,language='zh',beam_size=3,word_timestamps=True,vad_filter=False,initial_prompt=shot['text'])
 observed=[]
 for s in segs:
  for w in s.words or []:
   chars=[c for c in w.word if re.match(r'[\u4e00-\u9fffA-Za-z0-9]',c)]
   for i,ch in enumerate(chars):observed.append((ch,(w.start+(w.end-w.start)*i/max(1,len(chars)))*1000,(w.start+(w.end-w.start)*(i+1)/max(1,len(chars)))*1000))
 chars=[c for c in shot['text'] if re.match(r'[\u4e00-\u9fffA-Za-z0-9]',c)]
 matches={};matcher=difflib.SequenceMatcher(a=lazy_pinyin(''.join(chars)),b=lazy_pinyin(''.join(x[0] for x in observed)),autojunk=False)
 for m in matcher.get_matching_blocks():
  for j in range(m.size):matches[m.a+j]=observed[m.b+j][1:]
 duration=shot['voice_duration_ms'];ct=[]
 for i,c in enumerate(chars):
  if i in matches:start,end=matches[i];method='asr_word_interpolated'
  else:start=i/max(1,len(chars))*duration;end=(i+1)/max(1,len(chars))*duration;method='duration_estimate_unmatched'
  ct.append({'text':c,'start_ms':round(max(0,start)),'end_ms':round(min(duration,end)),'source':method})
 # Enforce monotonicity on noisy word boundaries without pretending exact phoneme alignment.
 for i,w in enumerate(ct):
  if i:w['start_ms']=max(w['start_ms'],ct[i-1]['end_ms'])
  w['end_ms']=max(w['start_ms']+20,w['end_ms'])
 for k in shot['keywords']:jieba.add_word(k,freq=1000000)
 clauses=[]
 for part in re.split('[，。！!？?：；]',shot['text']):
  if not part:continue
  while len(part)>14:clauses.append(part[:12]);part=part[12:]
  if part:clauses.append(part)
 phrases=[];cursor=0
 for clause in clauses:
  words=[]
  for token in jieba.lcut(clause):
   n=len(token);chunk=ct[cursor:cursor+n];cursor+=n
   if chunk:words.append({'text':token,'start_ms':chunk[0]['start_ms'],'end_ms':chunk[-1]['end_ms'],'source':'asr_word_interpolated' if all(w['source']=='asr_word_interpolated' for w in chunk) else 'includes_estimate'})
  if words:phrases.append({'text':clause,'start_ms':words[0]['start_ms'],'end_ms':words[-1]['end_ms'],'words':words})
 shot['words']=ct;shot['phrases']=phrases;shot['alignment_method']='ASR word boundaries + pinyin string match; characters within ASR words interpolated, unmatched explicitly estimated; not phoneme forced alignment'
 all_reports.append({'shot':shot['id'],'matched_chars':len(matches),'total_chars':len(chars),'asr_text':''.join(x[0] for x in observed)})
 print(all_reports[-1],flush=True)
file.write_text(json.dumps(tl,ensure_ascii=False,indent=2));(root/'qa/alignment-report.json').write_text(json.dumps(all_reports,ensure_ascii=False,indent=2))
