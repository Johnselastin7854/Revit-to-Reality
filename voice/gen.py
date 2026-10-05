import asyncio, edge_tts, os, sys
from feat import feats
import numpy as np
TEXT=("So here's the idea. You drop in a model, and a few seconds later you're walking through the building. "
      "You can switch off the walls, check the ducts, and just ask a question. It feels less like software, and more like being on site.")
async def main():
    vs=await edge_tts.list_voices()
    names=[v['ShortName'] for v in vs if v['Locale'].startswith('en-')]
    print(len(names),'english voices')
    ref,reflt=feats(r"C:/Users/USER/Downloads/TTS Task 10-3-2026, 9-58-47 AM.mp3")
    rows=[]
    for n in names:
        out=os.path.join(os.path.dirname(os.path.abspath(__file__)),"voices",n+".mp3"); os.makedirs(os.path.dirname(out),exist_ok=True)
        if not os.path.exists(out):
            try: await edge_tts.Communicate(TEXT,n).save(out)
            except Exception as e: print('fail',n,e); continue
        d,lt=feats(out)
        dist=abs(np.log(d['f0_med']/ref['f0_med']))*6 + np.sqrt(np.mean((lt-reflt)**2)) + abs(np.log((d['f0_iqr']+1)/(ref['f0_iqr']+1)))*1.5
        g=next(v['Gender'] for v in vs if v['ShortName']==n)
        rows.append((round(float(dist),3),n,g,d['f0_med'],d['f0_iqr']))
    rows.sort()
    for r in rows[:15]: print(r)
asyncio.run(main())
