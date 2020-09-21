#!/usr/bin/env python3
import serial
import time
import RPi.GPIO as GPIO 
GPIO.setmode(GPIO.BCM) 

ser=serial.Serial('/dev/ttyS0', 9600)
ser.flush()
line = ser.readline()
line=ser.readline()
C=line.split("\t")
celcius =C[0]
dielectric=C[1]
elec_conductivity=C[2]
cap=C[3]
soil_moisture=C[4]
imd=C[5]
print(celcius)
print(dielectric)
print(elec_conductivity)
print(cap)
print(soil_moisture)
print(imd)
       

'''Relay2_GPIO = 17 
GPIO.setup(Relay2_GPIO , GPIO.OUT)
GPIO.output(Relay2_GPIO, GPIO.LOW)
'''

def sensor():
    #GPIO.output(Relay2_GPIO, GPIO.HIGH) 
    ser = serial.Serial('/dev/ttyS0', 9600)
    ser.flush()
    line = ser.readline()
    line=ser.readline()
    C=line.split("\t")
    celcius =C[0]
    print(C[0])    
    print(C[1])    
    #while True:
        #ser.write("5\n".encode('ascii'))#ser.write(b"e\n")
        #time.sleep(5)
       # if ser.in_waiting > 0:
        #time.sleep(60)
        #print("started")
        #separating the incoming data
        #line1 = ser.read_until("\n").decode('utf-8').rstrip()
        #Celcius=ser.read_until("\n").decode('utf-8').rstrip()
        #dielectric=ser.read_until("\n").decode('utf-8').rstrip()
        #elec_conductivity=ser.read_until("\n").decode('utf-8').rstrip()
        #cap=ser.read_until("\n").decode('utf-8').rstrip()
        #soil_moist=ser.read_until("\n").decode('utf-8').rstrip()
        #imd=ser.read_until("\n").decode('utf-8').rstrip()
        # Shool Paramters
        #print(line1)
        #print(Celcius)
        #print(dielectric)
        #print(elec_conductivity)
        #print(cap)
        #print(soil_moist)
        #print(imd)
        #break;
    #GPIO.output(Relay2_GPIO, GPIO.LOW)
    #return(Celcius)
    time.sleep(10)

'''if __name__ == '__main__':
    sensor()
    
    print(C[0])'''
    

