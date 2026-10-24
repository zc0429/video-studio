"""Local generic male TTS adapter. Apache-2.0 Kokoro; no paid service or impersonation."""
import argparse,json,os
from pathlib import Path
import numpy as np,soundfile as sf,torch
from kokoro import KModel,KPipeline
p=argparse.ArgumentParser();p.add_argument('--script');p.add_argument('--out');p.add_argument('--speed',type=float,default=1.18);a=p.parse_args()
torch.set_num_threads(2);os.environ['TOKENIZERS_PARALLELISM']='false'
d=json.load(open(a.script));out=Path(a.out);out.mkdir(parents=True,exist_ok=True)
model=KModel(repo_id='hexgrad/Kokoro-82M-v1.1-zh').to('cpu').eval();pipe=KPipeline(lang_code='z',repo_id='hexgrad/Kokoro-82M-v1.1-zh',model=model)
for i,s in enumerate(d['shots']):
 path=out/f'{i+1:02d}-raw.wav'
 if path.exists():continue
 rs=list(pipe(s['text'],voice=d['voice'],speed=a.speed));audio=np.concatenate([r.audio.numpy() for r in rs]);sf.write(path,audio,24000,subtype='PCM_24');print(i+1,len(audio)/24000,s['text'],flush=True)
