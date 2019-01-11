import serial
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import numpy as np
import scipy
from scipy import signal
from drawnow import *
arduino=serial.Serial("/dev/ttyUSB0",timeout=1)
plt.ion()
data1 =[]
data2 =[]
maxdata=0
mindata=1023
time=1
x=[]
y1=[]
y2=[]

count=0
def makefig():
	plt.xlabel('freq') 
	plt.ylabel('amp') 
	plt.ylim(0,400)
	plt.xlim(3,10)
	plt.title('Glucometer reading')
	plt.grid(True)
	plt.plot(freq,t2)
	plt2=plt.twinx()
	plt.ylim(0,1023)
	#plt2.plot(y2,'ro-')	


while True:
	arduinoString = arduino.readline().decode('utf-8')
	data = arduinoString
	data=data.split()

	if len(data)==2:
		data1=float(data[0])
		data2=float(data[1])
		data1=int(data1)
		data2=int(data2)
	elif len(data)==1:
		data2=float(data[0])
		data2=int(data2)
	else:
		continue
	if len(data)==2:
		y1.append(data1)
		y2.append(data2)
	else:
		y2.append(data2)
	x.append(time)
	time+=1
	t1=np.array(y1)
	
	print(data1,data2)
	#numarr=scipy.signal.savgol_filter(t1,5,1)

	if len(t1)!=0:
		t2=np.fft.fft(t1)
		N=len(t2)
		freq=np.zeros(N)
		for i in range(0,N):
			freq[i]=float(2*3.1415926*(i+1)/N)

		drawnow(makefig)
	plt.pause(0.00000001)
	count=count+1
	if(count>50):
		y1.pop(0)
	

	
 




  
