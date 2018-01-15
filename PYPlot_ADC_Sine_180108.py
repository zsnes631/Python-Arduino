import serial
import numpy as np
import matplotlib.pyplot as plt
from drawnow import *
import serial.tools.list_ports

values = []
values1 = []
plt.ion()
cnt=0
valueX=0
Fs=100
f=4
x=0

arduino_ports = [
    p.device
    for p in serial.tools.list_ports.comports()
    if 'CH340' in p.description
]
serialArduino = serial.Serial(arduino_ports[0], 19200)   # close by serialArduino.close()

def plotValues():
    plt.title('Serial value from Arduino ADC  A0 pin')
    plt.grid(True)
    plt.ylabel('Voltage Values')
    plt.plot(values,  label='values', linestyle=":", linewidth=2)
    plt.plot(values1,  label='values1', linestyle="-", linewidth=2)
    plt.legend(loc='upper right')     #label location in the plot.
    plt.axis([0, 100, 0, 1024])

#pre-load dummy data    
for i in range(0,100):   #insert "0" into List "values" 
    values.append(0)
    values1.append(0)


while True:
    while (serialArduino.inWaiting() == 0):
        pass  
    valueRead = serialArduino.readline()
 

    #check if valid value can be casted
    try:
        valueInInt = int(valueRead)  
        print(valueInInt)
        print(valueX)
        if valueInInt <= 1024:
            if valueInInt >= 0:
                values.append(valueInInt)    
                values.pop(0)                             
                valueX = 300*np.sin(2*np.pi*f * (x/Fs))+400
                x=x+1
                if x > 100:
                   x=0
                values1.append(valueX)
                values1.pop(0)
                drawnow(plotValues)
            else:
                print ("Invalid! negative number")
        else:
            print ("Invalid! too large")
    except ValueError:
            print  ('Invalid! cannot cast')
