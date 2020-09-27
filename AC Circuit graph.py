# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 17:25:19 2020

@author: Sam
"""


#impoty librarys
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit as cv
#Import the data from the Text File

data = np.genfromtxt("ACcircuit1.txt",skip_header =3,delimiter="\t")



time=data[:, 0]
V_out=data[:,2]
V_in=data[:,1]

plt.xlabel("Time / s")
plt.ylabel("Voltage / V")
plt.plot(time,V_out, "r", label = "V_out")
plt.plot(time,V_in, "b", label = "V_in")
plt.title("AC output for V_in and V_out against time")
plt.legend()

def findfirstmax (array):
    count=0
    prev = 0
    while array[count] > prev:
        prev = array[count]
        count =count+1
    return count
def findfirstmax2 (array):
    count=0
    prev = 0
    while array[count] > prev:
        prev = array[count]
        count =count+1
    return prev

def findphasediff (count1, count2):
    phase = time[count1]-time[count2]
    return phase
print(round(findphasediff(findfirstmax(V_out),findfirstmax(V_in)), 5))

print(findfirstmax2(V_out))
print(findfirstmax2(V_in))