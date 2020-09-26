# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 16:00:28 2020

@author: Sam
"""

#impoty librarys
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit as cv
#Import the data from the Text File

data = np.genfromtxt("Draft4.txt",skip_header =3,delimiter="\t")

time=data[:, 0]
V_out=data[:,1]

def func(x, b):
    return 0.5*np.exp(-b * x)

popt1, pcov1 = cv(func, time, V_out)


print(popt1)

bVal1= str(round(popt1[0],3))




eq1 = " EXP(-" + bVal1 + "x)"


plt.xlabel("Time / s")
plt.ylabel("Voltage / V")
plt.plot(time,V_out, "r", label = "V_out, " + eq1)
plt.title("Time against Voltage at Different Parts of the Circuit")
plt.legend()
