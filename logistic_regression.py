# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 14:09:04 2018

@author: Sagar
"""

import numpy as np
import math as m
import matplotlib.pyplot as plt

x_data = np.array([[1],[20],[22],[2],[30],[40]])
y_data = np.array([[0],[1],[1],[0],[1],[1]])

data = np.column_stack((x_data, y_data))

#data = np.array([[1,0],[1,1],[1,2],[1,3],[3,1],[3,2]])

w0 = 0.01
w1 = 0.04

learn_rate = 0.01
err_sum=1
y_hat1 = np.zeros(len(data))
y_hat0 = np.zeros(len(data))
y_err = np.zeros(len(data))
y_pred = np.zeros(len(data))
while(err_sum>0.001):
    err_sum = 0
    for i in range(0,len(data)-1):
        
        if (y_data[i]==1):
            y_hat1[i] = (m.exp(w0+w1*x_data[i]))/(1+(m.exp(w0+w1*x_data[i])))
            y_err[i] = y_data[i]-y_hat1[i]
            err_sum = err_sum+(x_data[i]*y_err[i])
        else:
            y_hat0[i] = 1/(1+(m.exp(w0+w1*x_data[i])))
            y_err[i] = y_data[i]-y_hat0[i]
            err_sum = err_sum+(x_data[i]*y_err[i])
    w0 = w0+learn_rate*err_sum
    w1 = w1+learn_rate*err_sum


for i in range(0,len(data)):
    y_pred[i] = 1.0/(1.0+m.exp(-(w0+w1*x_data[i])))

print(w0,w1)

    
    








#plt.stem(x_data,y_data)

