from tensorflow import keras 
from tensorflow.keras.utils import to_categorical
import numpy as np 


train_data = np.genfromtxt("accidents_train.csv",
                            delimiter = ",")
test_data = np.genfromtxt("accidents_test.csv",
                        delimiter = ",")
np.set_printoptions(precision=3, suppress=True)

##run this twice to get rid of temp and distance
train_data = np.delete(train_data,2,1)
test_data = np.delete(test_data,2,1)


train_labels = np.empty([len(train_data),1])
test_labels = np.empty([len(test_data),1])

for i in range(0,len(train_labels)):
    train_labels[i] = train_data[i][0]
for i in range(0,len(test_labels)):
    test_labels[i] = test_data[i][0]
    
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)


train_data = np.delete(train_data,0,1)
test_data = np.delete(test_data,0,1)


classes = ["0","1","2","3","4"]

model = keras.Sequential([
    keras.layers.Dense(6, input_shape=(6,)),
    keras.layers.Activation('sigmoid'),
    keras.layers.Dense(5),
    keras.layers.Activation("sigmoid")
])

model.compile(optimizer = "adam",
              loss = "categorical_crossentropy",
              metrics = ["categorical_accuracy"])

model.fit(train_data,train_labels,epochs =3)
# =============================================================================
# 
# preds = model.evaluate(test_data,test_labels)
# =============================================================================

# =============================================================================
test_loss, test_accuracy = model.evaluate(test_data,test_labels) 
print("Tested accuracy: " + str(test_accuracy))
# =============================================================================
