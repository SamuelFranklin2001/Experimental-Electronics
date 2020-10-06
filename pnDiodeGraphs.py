# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit as cf

#for graph 1 enter data here
voltage_forward = [0.19,0.24,0.28,0.36,0.42]
current_forward = [0.0002,0.001,0.0042,0.0346,0.0870]

#for graph 2 enter data here
voltage_backwards = [8.94,12.12,14.98,16.83,18.00,20.00]
current_backwards = [0.20*10**(-6),1.44*10**(-6),1.77*10**(-6),1.98*10**(-6),2.10*10**(-6),2.33*10**(-6)]



plt.ylabel("Current / A")
plt.xlabel("Voltage / V")

#plot first graph

plt.yscale("log")
plt.plot(voltage_forward, current_forward, "b")
plt.title("Forward Bias; Current against Voltage for Shottky Diode")


#plot second graph

"""
plt.plot (voltage_backwards,current_backwards, "r")
plt.title("Reverse Bias; Voltage against Current for shottky")
"""

#use to find I_s and T from graph 1
lncurrent=[]
for i in range (len(current_forward)):
    lncurrent.append(np.log(current_forward[i]))
