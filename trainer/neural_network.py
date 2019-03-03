import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import EarlyStopping, ModelCheckpoint
import numpy as np

class AmesHousingNN:
    def __init__(self):

    def build_network(self, n_features, n_labels):
        model = Sequential()
        model.add(Dense(100, input_dim=n_features, activation='relu'))
        model.add(Dense(20, activation='relu'))
        model.add(Dense(1))
        model.compile(loss='mean_squared_error', optimizer='adam')
        self.model = model

    
    def create_callbacks(self)
        self.monitor = EarlyStopping(monitor='val_loss', min_delta=1e-3, patience=5, verbose=1, mode='auto')
        self.checkpointer = ModelCheckpoint(filepath='./models/best.hdf', verbose=0, save_best_only=True)