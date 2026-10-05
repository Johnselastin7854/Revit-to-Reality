import subprocess, numpy as np, imageio_ffmpeg, sys
FF=imageio_ffmpeg.get_ffmpeg_exe()
def load(p, sr=16000):
    raw=subprocess.run([FF,'-v','quiet','-i',p,'-ac','1','-ar',str(sr),'-f','s16le','-'],capture_output=True).stdout
    return np.frombuffer(raw,np.int16).astype(np.float32)/32768, sr
def feats(p):
    x,sr=load(p); dur=len(x)/sr
    fl=int(.04*sr); hop=int(.01*sr); f0=[]; specs=[]
    win=np.hanning(1024)
    for i in range(0,len(x)-fl,hop):
        fr=x[i:i+fl]
        if np.sqrt(np.mean(fr**2))<0.02: continue
        fr=fr-fr.mean(); ac=np.correlate(fr,fr,'full')[fl-1:]
        lo,hi=int(sr/400),int(sr/70)
        k=lo+np.argmax(ac[lo:hi])
        if ac[k]>0.45*ac[0]: f0.append(sr/k)
        if i%(hop*4)==0 and i+1024<len(x):
            specs.append(np.abs(np.fft.rfft(x[i:i+1024]*win)))
    S=np.log(np.mean(specs,0)+1e-6); bands=np.array_split(S[8:400],24); lt=np.array([b.mean() for b in bands]); lt-=lt.mean()
    f0=np.array(f0)
    speech=np.mean([np.sqrt(np.mean(x[i:i+hop]**2))>0.02 for i in range(0,len(x)-hop,hop)])
    return dict(dur=round(dur,1), f0_med=round(float(np.median(f0)),1), f0_iqr=round(float(np.percentile(f0,75)-np.percentile(f0,25)),1), voiced=round(float(speech),2)), lt
if __name__=='__main__':
    d,lt=feats(sys.argv[1]); print(d)
