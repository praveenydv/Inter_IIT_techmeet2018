import matplotlib.pyplot as plt 
import numpy as np
import scipy
from scipy import signal
count=0
t2=[]
def makefig():
	plt.xlabel('time') 
	plt.ylabel('wave') 
	plt.ylim(0,1023)
	plt.xlim(0,3)
	plt.title('Glucometer reading')
	plt.grid(True)
	plt.plot(t2,'bo-')
	plt2=plt.twinx()
	plt.ylim(0,1023)
	#plt2.plot(y2,'ro-')	




t2=np.fft.fft(t1)
plt.pause(0.00000001)
count=count+1
if(count>50):
	y1.pop(0)
	