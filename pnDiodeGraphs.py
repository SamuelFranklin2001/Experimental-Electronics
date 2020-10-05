# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit as cf

#for graph 1 enter data here
voltage_forward = []
current_forward = []

#for graph 2 enter data here
voltage_backwards = []
current_backwards = []

plt.xlabel("Current / A")
plt.ylabel("Voltage / V")

#plot first graph
"""
plt.xscale("log")
plt.yscale("log")
plt.plot (voltage_forward,current_forward, "b")
plt.title("Forward Bias; Voltage against Current")

"""
#plot second graph
"""
plt.xscale("log")
plt.yscale("log")
plt.plot (voltage_backwards,current_backwards, "r")
plt.title("Reverse Bias; Voltage against Current")
"""

q=0
k = 1.380649*(10**(-23))

#use to find I_s and T from graph 1
def predictedFunc1 (I_s, T):
    return I_s * np.exp((q*voltage_forward)/(k*T))

popt1, pcov1 = cf(predictedFunc1, current_forward, voltage_forward)

print(popt1)
