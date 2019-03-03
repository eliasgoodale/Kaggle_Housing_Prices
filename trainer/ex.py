from keras.models import Sequential
from keras.layers import Dense
from keras.datasets import mnist

from tensorboard_customization import TrainValTensorBoard


# Run /Applications/Python\ 3.6/Install\ Certificates.command in terminal if mnist.load_data() fails
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255

model = Sequential()
model.add(Dense(64, activation='relu', input_shape=(784,)))
model.add(Dense(10, activation='softmax'))
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(x_train, y_train, epochs=10,
          validation_data=(x_test, y_test),
          callbacks=[TrainValTensorBoard(write_graph=False)])