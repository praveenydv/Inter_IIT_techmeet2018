import serial
import time as tr
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import numpy as np
import scipy
from scipy import signal

arduino=serial.Serial("/dev/ttyUSB0",timeout=1)
data1 =[]
data2 =[]
maxdata=0
mindata=1023
time=1
x=[]
y1=[]
y2=[]
count=0
	

y1=[]
y2=[]
prev_max = 0
prev_min =0
while True:
	try:
		arduinoString = arduino.readline().decode('utf-8')			
		data_new=arduinoString.split()
	except:
		continue
	if(len(data_new) !=2):
		continue
	ac_data = float(data_new[0])
	dc_data = float(data_new[1])
	y1.append(dc_data)
	y2.append(ac_data)	
	if(len(y1) > 500):
		y1 = y1[len(y1)-499:]
		y2 = y2[len(y2)-499:]
	#print(len(y1),len(y2))
	ac_array = np.asarray(y2)
	dc_array = np.asarray(y1)
	cur_max = ac_array.max()
	cur_min = ac_array.min()
	rms = np.sqrt(np.mean(np.square(ac_array)))
	#if(cur_max != prev_max or cur_min != prev_min):
	print(float(tr.time()))
	print(ac_data,dc_data,rms)
	

	prev_max = ac_array.max()
	prev_min = ac_array.min()