from tensorflow.keras.datasets import mnist
import matplotlib.pyplot as plt
from tensorflow.keras.utils import to_categorical
from tensorflow import keras
import tensorflow as tf

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten
#download mnist data and split into train and test sets
(X_train, y_train), (X_test, y_test) = mnist.load_data()


plt.imshow(X_train[40])
X_train[0].shape


####some preprocessing
##reshaping them /flattening them
#first num is number of instnaces and the next two are height/width, then 1 = grayscale
X_train = X_train.reshape(,28,28,1)
X_test = X_test.reshape(-1,28,28,1)

y_train = to_categorical(y_train)
y_test = to_categorical(y_test)
y_train[0]

##start model
#sequential is to build a model layer by layer
model  = keras.Sequential()

model.add(Conv2D(64, kernel_size=3, activation='relu', input_shape=(28,28,1)))
model.add(Conv2D(32, kernel_size=3, activation='relu'))
model.add(Flatten())
model.add(Dense(10, activation='softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy', 
              metrics=['accuracy'])

model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=3)

####need to specify the input amount in the first parameter then 
#the next two parameters are the height/width and the last is for grayscale
#in this case needed to cast everything to a float for some reason
model.predict(tf.cast(X_test[4].reshape(1,28,28,1),tf.float32))
###have to resize it back down to get the image of the pixels
plt.imshow(X_test[4].reshape(28,28))
