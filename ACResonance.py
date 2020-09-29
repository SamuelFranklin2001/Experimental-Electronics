# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 22:43:17 2020

@author: Sam
"""


#impoty librarys
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit as cv
#Import the data from the Text File

#This is inefficiant, i dont care
data10k = np.genfromtxt("ACresonance10kNew.txt",skip_header =3,delimiter=",")

frequency=data10k[:, 0]
rlV_out10k=data10k[:,1]
imV_out10k=data10k[:,2]

data1k = np.genfromtxt("ACresonance1kNew.txt",skip_header =3,delimiter=",")
rlV_out1k=data1k[:,1]
imV_out1k=data1k[:,2]

data100 = np.genfromtxt("ACresonance100New.txt",skip_header =3,delimiter=",")
rlV_out100=data100[:,1]
imV_out100=data100[:,2]

data10 = np.genfromtxt("ACresonance10New.txt",skip_header =3,delimiter=",")
rlV_out10=data10[:,1]
imV_out10=data10[:,2]

data2 = np.genfromtxt("ACresonance2New.txt",skip_header =3,delimiter=",")
rlV_out2=data2[:,1]
imV_out2=data2[:,2]

"""                 
plt.figure(figsize=(20, 10))                    
plt.xscale("log")
plt.xlabel("frequency / Hz")
plt.ylabel("Voltage / V")
plt.plot(frequency,rlV_out10k, "g", label = "V_out_real for 10k Ohms for the resistors")
plt.plot(frequency,rlV_out1k, "b", label = "V_out_real for 1k Ohms for the resistors")
plt.plot(frequency,rlV_out100, "pink", label = "V_out_real for 100 Ohms for the resistors")
plt.plot(frequency,rlV_out10, "r", label = "V_out_real for 10 Ohms for the resistors")
plt.plot(frequency,rlV_out2, "black", label = "V_out_real for 2 Ohms for the resistors")
plt.title("AC Resonance graph")
plt.legend()
"""


x = lambda x, y : (x**2 + y**2)**0.5

V_out10k= []
for i in range (len(rlV_out10k)):
    V_out10k.append(x(rlV_out10k[i], imV_out10k[i]))
    
V_out1k= []
for i in range (len(rlV_out1k)):
    V_out1k.append(x(rlV_out1k[i], imV_out1k[i])) 
    
V_out100= []
for i in range (len(rlV_out100)):
    V_out100.append(x(rlV_out100[i], imV_out100[i])) 
    
V_out10= []
for i in range (len(rlV_out10)):
    V_out10.append(x(rlV_out10[i], imV_out10[i]))     

V_out2= []
for i in range (len(rlV_out2)):
    V_out2.append(x(rlV_out2[i], imV_out2[i])) 
    
plt.figure(figsize=(20, 10))     
plt.xscale("log")
plt.xlabel("frequency / Hz")
plt.ylabel("Voltage / V")
plt.plot(frequency,V_out10k, "g", label = "V_out for 10k Ohms for the resistors (Magnitude)") 
plt.plot(frequency,V_out1k, "b", label = "V_out for 1k Ohms for the resistors (Magnitude)")
plt.plot(frequency,V_out100, "r", label = "V_out for 100 Ohms for the resistors (Magnitude)")
plt.plot(frequency,V_out10, "orange", label = "V_out for 10 Ohms for the resistors (Magnitude)")
plt.plot(frequency,V_out2, "black", label = "V_out for 2 Ohms for the resistors (Magnitude)")
plt.title("AC Resonance graph (Magnitudes)")
plt.legend()   
    
def freqAtHalfAmp (V, f):
    for i in range (len(V)):
        if V[i] > 0.244 and V[i] < 0.256:
            print(f[i])
def resonantFreq (V, f):
    for i in range (len(V)):
        if V[i] > 0.49 and V[i] < 0.51:
            print(f[i])   
            
           
     
            
"""        
freqAtHalfAmp(V_out1k, frequency)
freqAtHalfAmp (V_out100, frequency)
freqAtHalfAmp (V_out10, frequency)
freqAtHalfAmp (V_out2, frequency)
"""
