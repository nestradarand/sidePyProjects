# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 13:58:20 2020

@author: noahe
"""

from tensorflow import keras 
from tensorflow.keras.utils import to_categorical
import numpy as np

from tensorflow.keras.layers import Dense, Conv2D, Flatten

from tensorflow.keras.utils import to_categorical


####need to load the data here



train_data = []
train_labels = []
test_data = []
test_labels= []


train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

###this is just a basic cnn set up


classes = []

####need to change the input size and the output size

model = keras.Sequential()
model.add(Conv2D(64, kernel_size=3, activation='relu', input_shape=(28,28,1)))
model.add(Conv2D(32, kernel_size=3, activation='relu'))
model.add(Flatten())
model.add(Dense(10, activation='sigmoid'))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(train_data,train_labels,epochs =3)

###to predict 
model.predit(test_data[4])