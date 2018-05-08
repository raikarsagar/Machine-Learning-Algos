# -*- coding: utf-8 -*-
"""
Created on Tue May  8 20:02:52 2018

@author: Sagar
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv

x = np.array([1,2,3,4])
y = np.array([2,4,4,5])

x0 = np.ones(len(x))
X = np.column_stack((x,x0))

X_t = X.transpose()
a = np.matmul(X_t,X)
a_inv = inv(a)
b = np.matmul(a_inv,X_t)

w = np.matmul(b,y)

plt.scatter(x,y)
plt.plot(x,w[0]*x+w[1],'r')
plt.show()