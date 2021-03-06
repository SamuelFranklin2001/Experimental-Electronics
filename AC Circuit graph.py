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

plt.xlabel("V_in / V")
plt.ylabel("V_out / V")
"""
plt.plot(time,V_out, "r", label = "V_out")
plt.plot(time,V_in, "b", label = "V_in")
"""


def findfirstmax (array):
    count=0
    prev = 0
    while array[count] > prev:
        prev = array[count]
        count =count+1
    return count

print(findfirstmax(V_out))


    
plt.plot(V_in,V_out,"black", label="phase")
plt.title("Phase between V_in and V_out for AC")
plt.legend()
