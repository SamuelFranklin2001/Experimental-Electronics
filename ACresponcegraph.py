# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 18:47:06 2020

@author: Sam
"""

#impoty librarys
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit as cv
#Import the data from the Text File

data = np.genfromtxt("ACresponceNew.txt",skip_header =3,delimiter=",")



frequency=data[:, 0]
rlV_out=data[:,1]
imV_out=data[:,2]



x = lambda x, y : (x**2 + y**2)**0.5

V_out= []
for i in range (len(rlV_out)):
    V_out.append(x(rlV_out[i], imV_out[i]))

# rempve the relevant " " for the  graph i  want to produce.
    
"""
plt.xscale("log")
plt.xlabel("frequency / Hz")
plt.ylabel("Voltage / V")
plt.plot(frequency,rlV_out, "r", label = "Real V_out")
plt.plot(frequency,imV_out, "b", label = "Imaginary V_out")
plt.title("AC Responce to Amplitude")
plt.legend()


plt.xscale("log")
plt.xlabel("frequency / Hz")
plt.ylabel("Voltage / V")
plt.plot(frequency,V_out, "g", label = "Magnitude of V_out")
plt.title("AC Responce to Amplitude (Magnitude)")
plt.legend()
"""