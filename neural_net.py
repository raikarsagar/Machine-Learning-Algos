# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 08:52:08 2018

@author: Sagar
"""

import numpy as np

X = np.array([[0.05],[0.10]])

Y = np.array([[0.01],[0.99]])

weight_hidden = np.array([[0.15,0.20],[0.20,0.30]])
bias_hidden = np.array([[0.35],[0.35]])

weight_out = np.array([[0.40,0.45],[0.50,0.55]])
bias_out = np.array([[0.60],[0.60]])

lr = 0.5

def activation(x):
    return (1/(1+np.exp(-x)))

def gradient(x):
    return x*(1-x)

weight_fir = np.array([[0],[0]])
weight_first = weight_fir.astype(float)

weight_sec = np.array([[0],[0]])
weight_second = weight_sec.astype(float)

weight_one = np.array([[0],[0]])
weight_1 = weight_one.astype(float)

weight_two = np.array([[0],[0]])
weight_2 = weight_two.astype(float)

i = 1
for i in range(1,2):
    
    #forward propagation
    net_hid = bias_hidden + np.matmul(weight_hidden,X)
    out_hid = activation(net_hid)
    net_out = bias_out+ np.matmul(weight_out,out_hid)
    out_out = activation(net_out)
    E_out = 0.5*((Y-out_out)**2)
    E_total = sum(E_out)
    E_error = Y-E_out
    
    #backward propagation
    
    out_gradient = out_out-Y
    net_gradient = gradient(out_out)
    inter = weight_out
    
    #
    weight_out = weight_out-(lr)*(out_gradient*net_gradient*out_hid)
    #
    net_hid_gradient = gradient(out_hid)
    weight_first[0] = inter[0][0]
    weight_first[1] = inter[1][0]
    weight_second[0] = inter[0][1]
    weight_second[1] = inter[1][1]
    other = out_gradient*net_gradient
    weight_1[:,0] = sum(other*weight_first)
    weight_2[:,0] = sum(other*weight_second)
    
    weight_hid_first = np.reshape(weight_hidden[:,0],(2,-1))
    weight_hid_second = np.reshape(weight_hidden[:,1],(2,-1))
    weight_hid_1 = weight_hid_first - (lr)*(net_hid_gradient*X*(weight_1))
    weight_hid_2 = weight_hid_second - (lr)*(net_hid_gradient*X*(weight_2))
    
    weight_hidden[0,:] = weight_hid_1.T
    weight_hidden[1,:] = weight_hid_2.T
    i = i+1


E_out = 0.5*((Y-out_out)**2)
E_total = sum(E_out)
E_error = Y-E_out
#output after i iterations
print("Output = ",out_out)
#total error after i iterations
print("E total = ",E_total)






