# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 21:20:06 2019

@author: noahe
"""

from tensorflow import keras 
from tensorflow.keras.utils import to_categorical
import numpy as np 



train = np.genfromtxt('irisTrain.csv',delimiter = ',',skip_header = 1)
test = np.genfromtxt('irisTest.csv',delimiter = ',',skip_header = 1)


train_labels = np.empty([len(train),1])
test_labels = np.empty([len(test),1])

classes = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']

for i in range(0,len(train_labels)):
    train_labels[i] = train[i][4]
for i in range(0,len(test_labels)):
    test_labels[i] = test[i][4]


train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

train = np.delete(train,4,1)
test = np.delete(test,4,1)

model = keras.Sequential([
    keras.layers.Dense(4, input_shape=(4,)),
    keras.layers.Activation('sigmoid'),
    keras.layers.Dense(3),
    keras.layers.Activation("sigmoid")
])


model.compile(optimizer = "adam",
              loss = "categorical_crossentropy",
              metrics = ["accuracy"])

model.fit(train,train_labels,epochs = 500)

test_loss, test_accuracy = model.evaluate(test,test_labels) 
print("Tested accuracy: " + str(test_accuracy))

preds = model.predict(test)
max_index = np.argmax(preds[14])
print("Tested: %s" % classes[np.argmax(test_labels[14])] )
print("Predicted: %s" % classes[np.argmax(preds[14])])
