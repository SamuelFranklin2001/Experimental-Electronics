# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit as cf

#for graph 1 enter data here
voltage_forward = [0.53,0.58,0.68,0.73,0.77,0.80,0.831]
current_forward = [0.0003,0.0010,0.0069,0.0218,0.0600,0.1200,0.3055]

#for graph 2 enter data here
voltage_backwards = [8.94,12.12,14.98,16.83,18.00,20.00]
current_backwards = [0.20*10**(-6),1.44*10**(-6),1.77*10**(-6),1.98*10**(-6),2.10*10**(-6),2.33*10**(-6)]

voltage_backwards = [12,14.1,15.0,16.0,17.0]
current_backwards = [1.20*10**(-6),1.41*10**(-6),1.50*10**(-6),1.60*10**(-6),1.70*10**(-6)]

plt.ylabel("Current / A")
plt.xlabel("Voltage / V")

#plot first graph
"""
plt.yscale("log")
plt.plot(voltage_forward,current_forward, "b")
plt.plot()
plt.title("Forward Bias; Current against Voltage for pn Diode")
"""

#plot second graph


plt.plot (voltage_backwards,current_backwards, "r")
plt.title("Reverse Bias; Voltage against Current for pn")

lncurrent=[]
for i in range (len(current_forward)):
    lncurrent.append(np.log(current_forward[i]))

q=1.6*10**(-19)
k = 1.380649*(10**(-23))

#use to find I_s and T from graph 1
def func(v, T, lnIs):
    return v*(q/(k*T)) +lnIs

popt1, pcov1 = cf(func, voltage_forward, lncurrent,maxfev = 100000)

print(np.exp(popt1[1]))
print(popt1[0])
