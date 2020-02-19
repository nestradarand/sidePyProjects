# -*- coding: utf-8 -*-
"""
Hoepfully the NASA CNN
"""
import matplotlib.pyplot as plt
from tensorflow.keras.utils import to_categorical
from tensorflow import keras
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten


xtrain = []
train_labels = []

model  = keras.Sequential()

model.add(Conv2D(64, kernel_size=3, activation='relu', input_shape=(28,28,1)))
model.add(Conv2D(32, kernel_size=3, activation='relu'))
model.add(Flatten())
model.add(Dense(10, activation='softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy', 
              metrics=['accuracy'])

model.fit(xtrain,train_labels , validation_data=(X_test, y_test), epochs=3)

