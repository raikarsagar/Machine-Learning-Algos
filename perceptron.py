# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 14:17:43 2018

@author: Sagar
"""

import numpy as np
import matplotlib.pyplot as plt
import math as m

x0_data = np.array([[1],[1],[1],[1]])
x1_data = np.array([[0],[0],[1],[1]])
x2_data = np.array([[0],[1],[0],[1]])
y_exp = np.array([[-1],[1],[1],[1]])

data = np.column_stack((x0_data,x1_data, x2_data))

w0 = -0.5
w1 = 0.4
w2 = 0.6

learning_rate = 0.1
#activation = w0
y_pred = np.array([[0],[0],[0],[0]])
weights = np.array([w0,w1,w2])
y_mod = y_exp-y_pred
count=0
while(abs(sum(y_mod))>0):
    count = count+1
    for i in range(0,len(data)):
        activation = sum(weights*data[i])
        if (activation>0):
            y_pred[i] = 1
        else:
            y_pred[i] = -1
    
    y_mod = y_exp-y_pred
    for i in range(0,len(x1_data)):
        weights[0] = weights[0]+(y_mod[i])*learning_rate
        weights[1] = weights[1]+(y_mod[i]*x1_data[i])*learning_rate
        weights[2] = weights[2]+(y_mod[i]*x2_data[i])*learning_rate

plt.scatter(x1_data,x2_data)
plt.plot(x1_data,((-weights[0]/weights[2])-(weights[1]/weights[2])*x1_data))

        
