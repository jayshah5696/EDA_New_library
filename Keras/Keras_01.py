# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 22:26:17 2018

@author: Lenovo
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical


(train_images,train_labels), (test_images,test_labels) = mnist.load_data()

networks = models.Sequential()
networks.add(layers.Dense(512,activation='relu',input_shape=(28*28,)))
networks.add(layers.Dense(10, activation='softmax'))
# To make sure network is training ready we need to make 3 things
# Optimizer, loss, metrics
networks.compile(optimizer='rmsprop',
                 loss='categorical_crossentropy',
                 metrics=['accuracy'])

# Preprocessing Images
train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255

test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255

# Preprocessing Labels
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

# Fitting the network
networks.fit(train_images, train_labels, epochs=5, batch_size=128)