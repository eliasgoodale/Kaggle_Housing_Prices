import numpy as np
import tensorflow as tf
import keras.backend as K 
from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import EarlyStopping, ModelCheckpoint, TensorBoard
from processing import load_data
from sklearn import metrics 
import time

NAME = f"Ames-Dataset-Sequential-{int(time.time())}"

X_train, X_valid, y_train, y_valid = load_data()

print("X_train : " + str(X_train.shape))
print("X_valid : " + str(X_valid.shape))
print("y_train : " + str(y_train.shape))
print("y_valid : " + str(y_valid.shape))


def soft_acc(y_true, y_pred):
    return K.mean(K.equal(K.round(y_true), K.round(y_pred)))

#monitor = EarlyStopping(monitor='val_loss', min_delta=1e-3, patience=5, verbose=1, mode='auto')
checkpointer = ModelCheckpoint(filepath='./models/best.hdf5', verbose=0, save_best_only=True)
tensorboard = TensorBoard(log_dir=f"logs/{NAME}")

model = Sequential([
    Dense(128, input_dim=X_train.shape[1], activation='relu'),
    Dense(64, activation='relu'),
    Dense(32, activation='relu'),
    Dense(1)
])



model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy', 'mean_squared_error'])
model.fit(
    X_train,
    y_train,
    validation_data=(X_valid, y_valid),
    callbacks=[checkpointer, tensorboard],
    verbose=1,
    epochs=10000)

#model.load_weights('./models/best.hdf5')

pred = model.predict(X_valid)
score = np.sqrt(metrics.mean_squared_error(pred, y_valid))
print(f'Score (RMSE): {score}')
