# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
#input the data set
#data = np.array([1,1,1,1,1,0,0,0,0,0])
#the theta values
trials = 2;
#theta = np.linspace(0,1,num = 1000)
theta = np.array([[0],[0.25],[0.5],[0.75],[1]])
p_theta = np.ones(len(theta))
p_theta = p_theta/len(theta)

x = np.column_stack((theta, p_theta))
ax1 = fig.add_subplot(311)
ax1.stem(theta,p_theta)

#p_theta_n = np.linalg.inv(p_theta)
#take number of heads as inpu10
h = 1;
t = trials-1;

like_fun = (pow(theta,h))*(pow((1-theta),t))

ax2 = fig.add_subplot(312)
ax2.stem(theta,like_fun)

post_prob = np.zeros(len(theta))
post_prob = like_fun*(p_theta)

ax3 = fig.add_subplot(313)
ax3.stem(theta,post_prob,'-')
p_d1 = 0

plt.show()


