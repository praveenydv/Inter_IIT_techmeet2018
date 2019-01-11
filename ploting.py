import serial # import from pySerial
import numpy as np# import library from Numerical python
import matplotlib.pyplot as plt # import Library from matplotlib
from drawnow import drawnow # import lib from drawnow

ConF = [] # create an empty array for graphing
ArduinoData = serial.Serial('/dev/ttyUSB0',115200) # set up serial connection with    arduino
plt.ion() # tell matplotlib you want interactive mode to plot data
cnt = 0
def makeFig(): # creat a function to make plot
    plt.plot(ConF, 'go-')

while True: # loop that lasts forever
    while (ArduinoData.inWaiting()==0): # wait till there is data to plot
         pass # do nothing

    arduinoString = ArduinoData.readline().decode().strip('\r\n')
    dataArray = arduinoString
    #Con = float(arduinoString) # turn string into numbers

    ConF=np.random.rand(10,1) # addinf to the array.

    drawnow(makeFig) # call draw now to update
    plt.pause(.000001)
    cnt=cnt+1
    if(cnt>50):
         ConF.pop(0)