import serial
import matplotlib.pyplot as plt 
import matplotlib.animation as animation



arduino=serial.Serial("/dev/ttyUSB1",timeout=1)

data1 =[]
data2 =[]
maxdata=0
mindata=1023
time=1
x=[]
y=[]
count=0
while count<1000:
	data=arduino.readline()
	data=list(str(data))
	l=len(data)
	del data[l-1],data[l-2],data[l-3],data[l-4],data[l-5],data[0],data[0];
	data=''.join(data)
	data=data.split()
	if len(data)==2:
		data1=float(data[0])
		data2=float(data[1])
	elif len(data)==1:
		data2=float(data[0])
	else:
		continue
	maxdata=max(maxdata,data1)
	mindata=min(mindata,data1)

	print(maxdata,mindata,data2)

	x.append(time)
	y.append(data1)
	plt.scatter(x, y)
	time=time+1
	plt.xlabel('time') 
	plt.ylabel('wave') 
	plt.title('Glucometer reading')
	count=count+1
plt.show() 




  
