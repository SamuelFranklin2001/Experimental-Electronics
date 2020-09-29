# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 16:42:47 2020

@author: Sam
"""


#impoty librarys
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit as cv
#Import the data from the Text File

data = np.genfromtxt("TransientResponse.txt",skip_header =3,delimiter="\t")
time=data[:, 0]
V_out=data[:,1]

"""
plt.xlabel("Time / s")
plt.ylabel("Voltage / V")
plt.plot(time,V_out, "r", label = "V_out")
plt.title("Transient Responce")
plt.legend()


for i in range (len(time)):
    if V_out[i]>0.0175 and V_out[i]<0.0185:
        print (time[i])
"""  


V_out_sin=[]
V_out_exp=[]

for i in range (len(V_out)):
    V_out_sin.append (V_out[i] / (0.05*np.e**(-time[i]/0.0096)) )

def func(x, a, b):
    return a*np.sin(b*x)

popt1, pcov1 = cv(func, time, V_out_sin)

print(popt1)


plt.xlabel("Time / s")
plt.ylabel("Voltage / V")
plt.plot(time,V_out_sin, "r", label = "V_out")
plt.title("Transient Responce")
plt.legend()