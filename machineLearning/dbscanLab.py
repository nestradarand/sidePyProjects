# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 13:41:26 2020

@author: noahe
"""

from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


data = pd.read_csv('wholesale_data.csv')
data.drop(['Channel','Region'],axis = 1,inplace = True)

data  =data[['Grocery','Milk']]
data = data.as_matrix().astype("float32", copy = False)

stscaler = StandardScaler().fit(data)
data = stscaler.transform(data)

plt.figure()
for i in range(0,len(data)):
    plt.scatter(data[i][0],data[i][1],c ='blue')
plt.show()
    
dbsc = DBSCAN(eps = .5, min_samples = 15).fit(data)

labels = dbsc.labels_
core_samples = np.zeros_like(labels, dtype = bool)
core_samples[dbsc.core_sample_indices_] = True

plt.figure()
for i in range(0,len(data)):
    if core_samples[i] == True:
        plt.scatter(data[i][0],data[i][1],c = 'blue')
    else:
        plt.scatter(data[i][0],data[i][1],c = 'red')
        
    
####toy example
from sklearn.datasets import make_moons
# moons_X: Data, moon_y: Labels
moons_X, moons_Y = make_moons(n_samples = 2000)

plt.figure()
for i in range(0,len(moons_X)):
    if moons_Y[i] == 1:
        plt.scatter(moons_X[i][0],moons_X[i][1], c = 'red')
    else:
        plt.scatter(moons_X[i][0],moons_X[i][1], c = 'blue')

def add_noise(X,y, noise_level = 0.01):
    #The number of points we wish to make noisy
    amt_noise = int(noise_level*len(y))
    #Pick amt_noise points at random
    idx = np.random.choice(len(X), size = amt_noise)
    #Add random noise to these selected points
    noise = np.random.random((amt_noise, 2) ) -0.5
    X[idx,:] += noise
    return X 
        
moons_X = add_noise(moons_X,moons_Y)

new_dbsc = DBSCAN(eps=.15,min_samples = 7).fit(moons_X)
new_labs = new_dbsc.labels_
cores = np.zeros_like(new_labs,dtype = bool)
cores[new_dbsc.core_sample_indices_] = True

np.unique(new_dbsc.labels_)

plt.figure()
for i in range(0,len(moons_X)):
    label = new_dbsc.labels_
    if label[i] == 1:
        col = 'blue'
    elif label[i] == 0:
        col = 'green'
    else:
        col = 'red'
    plt.scatter(moons_X[i][0],moons_X[i][1], c = col)
    





    


