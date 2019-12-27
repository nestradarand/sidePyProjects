# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 21:04:15 2019
This is for pre processing
@author: noahe
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import iqr
from sklearn.model_selection import train_test_split





iris = pd.read_csv('Iris.csv')
iris.describe()
iris.drop(['Id'],axis = 1,inplace = True)

####normalizations

plt.boxplot(iris['SepalLengthCm'])
iris['SepalLengthCm'] = (iris['SepalLengthCm']-min(iris['SepalLengthCm']))/(max(iris['SepalLengthCm'])-min(iris['SepalLengthCm']))

##### fix outliers and nromalization
plt.boxplot(iris['SepalWidthCm'])
iris['SepalWidthCm'] = np.where(iris['SepalWidthCm']> (1.5*iqr(iris['SepalWidthCm'])+3.3),
                                (1.5*iqr(iris['SepalWidthCm'])+3.3),iris['SepalWidthCm'])
iris['SepalWidthCm'] = np.where(iris['SepalWidthCm']< (2.8 - 1.5*iqr(iris['SepalWidthCm'])),
                                (2.8 - 1.5*iqr(iris['SepalWidthCm'])),iris['SepalWidthCm'])

iris['SepalWidthCm'] = (iris['SepalWidthCm'] - min(iris['SepalWidthCm']))/(max(iris['SepalWidthCm'])-min(iris['SepalWidthCm']))


plt.boxplot(iris['PetalLengthCm'])
iris['PetalLengthCm'] = (iris['PetalLengthCm']-min(iris['PetalLengthCm']))/(max(iris['PetalLengthCm'])-min(iris['PetalLengthCm']))

plt.boxplot(iris['PetalWidthCm'])
iris['PetalWidthCm'] = (iris['PetalWidthCm']-min(iris['PetalWidthCm']))/(max(iris['PetalWidthCm'])-min(iris['PetalWidthCm']))

#####make labels into numeric categories
classes = iris['Species'].unique()
iris['Species'] = np.where(iris['Species'] == classes[0],int(0),
                           np.where(iris['Species'] == classes[1],int(1),int(2)))

train_data,test_data = train_test_split(iris)




train_data.to_csv('irisTrain.csv',index = False)
test_data.to_csv('irisTest.csv',index = False)

