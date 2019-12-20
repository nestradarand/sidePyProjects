import numpy as np
import tensorflow as tf 
from tensorflow import keras

np.set_printoptions(precision=3, suppress=True)


####data loading and making labels
train_data = np.genfromtxt("steam_train.csv",delimiter=",")
test_data = np.genfromtxt("steam_test.csv",delimiter=",")
train_labels = np.empty([len(train_data),1])
test_labels = np.empty([len(test_data),1])
print(np.amax(test_labels))
for i in range(0,len(train_labels)-1):
    train_labels[i] = train_data[i][4]
for i in range(0,len(test_labels)-1):
    test_labels[i] = test_data[i][4]
###getting rid of the values in the previously contained columns
train_data = np.delete(train_data,4,1)
test_data = np.delete(test_data,4,1)
####normalize all values in train and test
for i in range(0,len(train_data)):
    train_data[i][0] = train_data[i][0]/18
    train_data[i][1] = train_data[i][1]/9821
    train_data[i][2] = train_data[i][2]/38805
    train_data[i][3] = train_data[i][3]/49.9072
for i in range(0,len(test_data)):
    test_data[i][0] = test_data[i][0]/18
    test_data[i][1] = test_data[i][1]/9821
    test_data[i][2] = test_data[i][2]/38805
    test_data[i][3] = test_data[i][3]/49.9072

class_names = ["not_successfull","successful"]
colnames = ["required_age","achievements","average_playtime","price","success"]

model = keras.Sequential([
    keras.layers.Dense(4, input_shape=(4,)),
    keras.layers.Activation('sigmoid'),
    keras.layers.Dense(2),
    keras.layers.Activation('softmax'),
])

model.compile(optimizer = "adam",loss = "sparse_categorical_crossentropy",metrics = ["accuracy"])

model.fit(train_data,train_labels,epochs = 4)

# test_loss, test_accuracy = model.evaluate(test_data,test_labels)

# print("Tested accuracy: " + str(test_accuracy))

### to make prediction


preds = model.predict(test_data)
print(preds)
print("Le done")