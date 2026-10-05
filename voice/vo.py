import asyncio, edge_tts, os, json, subprocess, imageio_ffmpeg, base64
from feat import load
FF=imageio_ffmpeg.get_ffmpeg_exe()
VOICE="en-US-JennyNeural"
CH=[0,6,16,24,38.5,45.5,56,70,79]; END=86; DELAY=.3
LINES=[
 "Hi! This is Revit to Reality. Your BIM model, as a building you can explore.",
 "It starts with an upload. Drop in your IFC model, and the workers take it from there. They check it, and sort every element.",
 "Then it streams in, floor by floor. Even a huge tower stays smooth, right in your browser.",
 "Now, here's where it gets useful. Turn off the architecture... then the structure... and you're left with just the building services. Want only the ductwork? That's one click.",
 "Pull the floors apart, switch on X-ray, and you can see exactly what's hiding in the ceiling.",
 "Or, honestly, just ask. Type a question, and the assistant finds the answer and lights it up in the model.",
 "Okay, let's go inside. You can walk Level twelve, just like a game. The minimap turns with you, and it'll guide you to any room.",
 "And after handover, it becomes a digital twin. Live sensors show you every room, so you know the moment something's wrong.",
 "Revit to Reality. Upload it, understand it, walk it, run it."
]
async def main():
    out=[]
    for i,txt in enumerate(LINES):
        rate="+0%"
        while True:
            p=f"vo{i}.mp3"
            await edge_tts.Communicate(txt,VOICE,rate=rate).save(p)
            x,sr=load(p); d=len(x)/sr
            nxt=(CH[i+1] if i+1<len(CH) else END)
            room=nxt-CH[i]-DELAY-.35
            if d<=room or rate=="+5%": break
            rate="+5%"
        out.append(dict(i=i,dur=round(d,2),room=round(room,2),rate=rate))
        print(out[-1])
    json.dump(out,open("vo.json","w"))
asyncio.run(main())
