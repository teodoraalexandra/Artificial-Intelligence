#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 15:29:11 2020

@author: teodoradan
"""


import numpy as np 
import keras  
from keras.datasets import mnist 
from keras.models import Model 
from keras.layers import Dense, Input
from keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten 
from keras import backend as k 

    
def checkDataFormat(x_train, y_train, x_test, y_test):
    img_rows, img_cols = 28, 28
    
    if k.image_data_format() == 'channels_first': 
       x_train = x_train.reshape(x_train.shape[0], 1, img_rows, img_cols) 
       x_test = x_test.reshape(x_test.shape[0], 1, img_rows, img_cols) 
       inpx = (1, img_rows, img_cols) 
      
    else: 
       x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 1) 
       x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1) 
       inpx = (img_rows, img_cols, 1) 
  
    #We can normalize the x_train and x_test data by dividing it with 255
    x_train = x_train.astype('float32') 
    x_test = x_test.astype('float32') 
    x_train /= 255 
    x_test /= 255

    #Since output of the model can comprise of any of the digits between 0 to 9,
    #we need 10 classes in output.
    y_train = keras.utils.to_categorical(y_train) 
    y_test = keras.utils.to_categorical(y_test)  
    
    return inpx, x_train, y_train, x_test, y_test


def createModel(inpx, x_train, y_train):
    inpx = Input(shape=inpx) 
    layer1 = Conv2D(32, kernel_size=(3, 3), activation='relu')(inpx) 
    layer2 = Conv2D(64, (3, 3), activation='relu')(layer1) 
    layer3 = MaxPooling2D(pool_size=(3, 3))(layer2) 
    layer4 = Dropout(0.5)(layer3) 
    layer5 = Flatten()(layer4) 
    layer6 = Dense(250, activation='sigmoid')(layer5) 
    layer7 = Dense(10, activation='softmax')(layer6)
    
    #compile and fit the model
    #[inpx] is the input in the model and layer7 is the output of the model
    model = Model([inpx], layer7) 
    model.compile(optimizer=keras.optimizers.Adadelta(), 
                  loss=keras.losses.categorical_crossentropy, 
                  metrics=['accuracy']) 
      
    model.fit(x_train, y_train, epochs=12, batch_size=500)
 
    return model

    
if __name__ == '__main__':
    #Create the train data and test data
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    
    #While proceeding further, img_rows and img_cols are used as the image dimensions. 
    #In mnist dataset, it is 28 and 28
    inpx, x_train, y_train, x_test, y_test = checkDataFormat(x_train, y_train, x_test, y_test)
    
    #Dataset is ready so we can move towards the CNN model
    model = createModel(inpx, x_train, y_train) 
    
    #Evaluate the model
    score = model.evaluate(x_test, y_test, verbose=0) 
    print('loss=', score[0]) 
    print('accuracy=', score[1])   


    
    
    
    
    