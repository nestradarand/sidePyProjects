# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 14:36:36 2020

@author: noahe
"""
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from debacl import geom_tree as gtree
from debacl import utils as utl


###### using DeBaCL
def knn_estimate(data, k, point):
    n,d = data.shape
    #Reshape the datapoint, so the cdist function will work
    point = point.reshape((1,2))
    #Find the distance to the kth nearest data point
    knn = sorted(reduce(lambda x,y: x+y,cdist(data, point).tolist()))[k+1]
    #Compute the density estimate using the mathematical formula
    estimate = float(k)/(n*np.power(knn, d)*np.pi)
    return estimate
    
##to make dense inner data and sparse outter ring use
def makeCraters(inner_rad = 4, outer_rad = 4.5, donut_len = 2, inner_pts = 1000, outer_pts = 500):
    #Make the inner core
    radius_core = inner_rad*np.random.random(inner_pts)
    direction_core = 2*np.pi*np.random.random(size = inner_pts)
    #Simulate inner core points
    core_x = radius_core*np.cos(direction_core)
    core_y = radius_core*np.sin(direction_core)
    crater_core = zip(core_x, core_y)
    #Make the outer ring
    radius_ring = outer_rad + donut_len*np.random.random(outer_pts)
    direction_ring = 2*np.pi*np.random.random(size = outer_pts)
    #Simulate ring points
    ring_x = radius_ring*np.cos(direction_ring)
    ring_y = radius_ring*np.sin(direction_ring)
    crater_ring = zip(ring_x, ring_y)
     
    return np.array(crater_core), np.array(crater_ring)