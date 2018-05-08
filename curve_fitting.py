# -*- coding: utf-8 -*-
"""
Created on Tue May  8 20:16:37 2018

@author: Sagar
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv

x = np.array([1,2,3,4])
y = np.array([1,5,1,16])

 
x0 = np.ones(len(x))
X = np.column_stack((x**2,x,x0))

X_t = X.transpose()
a = np.matmul(X_t,X)
a_inv = inv(a)
b = np.matmul(a_inv,X_t)

w = np.matmul(b,y)

plt.scatter(x,y)
plt.plot(x,w[2]+w[1]*x+w[0]*x**2,'r')
plt.show()