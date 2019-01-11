import numpy as np
from scipy.signal import butter, lfilter
from scipy.stats import iqr
import detect_peaks

import matplotlib.pyplot as plt

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks



def butter_bandpass(sig,lowcut, highcut, fs, order=2):
   nyq = 0.5 * fs
   low = lowcut / nyq
   high = highcut / nyq
   b, a = butter(order, [low, high], btype='band')
   y=lfilter(b,a,sig)
   return y

def mfft(sig,fs=100):
    y1=np.fft.fft(sig)
    N = len(y1)
    y1 = y1[0:N/2]
    fr = np.linspace(0,fs/2,N/2)
    return y1,fr

def a2m(sig):
    n=len(sig)
    t=0
    H=[]
    while(t<n):
        H.append(float(sig[t]))
        t=t+1
    return H

def flex_feat(sig,lpass,hpass):

    k=0
    maxi=0
    while(k<len(sig)):
        if (sig[k]>hpass):
            j=0
        elif (sig[k]>maxi):
            maxi=sig[k]
        k=k+1

    if (maxi>lpass):
        return 2000
    return 0

def max_freq(sig):
    n=len(sig)
    mf,fr=mfft(sig)

    return np.argmax(abs(mf))

def rms(sig):
    n=len(sig)
    summ=0
    i=0
    while (i<n):
        summ = summ + sig[i]**2
        i=i+1
    summ = summ**(0.5)
    return int((summ*1000)/n)

def peaks_indices(sig,mph,mpd):
    indexes = detect_peaks.detect_peaks(sig, mph, mpd)
    return indexes

def peaks(sig,mph=1,mpd=1):
    indi=peaks_indices(sig,mph,mpd)
    n=len(indi)
    i=0
    peak=[]
    while (i<n):
        peak.append(sig[indi[i]])
        i=i+1
    return peak
def slope_sign_change(sig,mph=00,mpd=5):
    sig=abs(sig)
    n=len(peaks_indices(sig,mph,mpd))
    return n

def range(sig):
    a=int(100*(max(sig)-min(sig)))
    return a

def check_predict(sig):
    i=1
    count=0
    while (i<3):
        if (sig[i]==sig[i-1]):

            count=count+1

        i=i+1
    if (count==2):
        return 1
    return 0

def mad(arr):
    arr = np.ma.array(arr).compressed() # should be faster to not use masked arrays.
    med = np.median(arr)
    return np.median(np.abs(arr - med))
def IQR(sig):
    return iqr(sig)

i=18
while i<24:
        data1 = pd.read_csv("person%d.csv"%i)
        x= data1[data1.columns[0]]
        x=x[:1500]
        y = -1*np.array(x)
        sd=np.std(x)
        mean=np.mean(x)
        peaks= peaks(x,2,10)
        minima,_= find_peaks(y,distance=50)
        np.diff(minima)
        y=-1*np.array(y)
        plt.plot(minima,y[minima],"x")
        
        np.diff(peaks)
        plt.plot(x)
        plt.plot(peaks, x[peaks], "x")
        plt.show()
        plt.close()
        i=i+1
