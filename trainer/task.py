import numpy as np
import tensorflow as tf
import keras.backend as K
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import EarlyStopping, ModelCheckpoint, TensorBoard
from processing import load_data
from sklearn import metrics 
import time
'''

    1) EDA + jupyter screenshot
    2) "naive" model + tensorboard screenshot
    3) model w missing data handling + tensorboard
    4) missing data and outliers handling + tensorboard
    make sure to submit results to kaggle

'''
def describe_data(X_train, X_valid, y_train, y_valid):
    #print(f"Shape X_train: {X_train.shape}")
    #print(X_train.describe())
    #print(f"Shape X_valid: {X_valid.shape}")
    #print(X_valid.describe())
    #print(f"Shape y_train: {y_train.shape}")
    #print(y_train.describe())
    print(y_train)
    #print(f"Shape y_valid: {y_valid.shape}")
    #print(y_valid.describe())
    print(y_valid)

def build_network_and_compute_RMSE(model_name, test_processing_level, X_train, X_valid, y_train, y_valid):
    def soft_acc(y_true, y_pred):
        return K.mean(K.equal(K.round(y_true / 10), K.round(y_pred / 10)))

    def print_dict(d):
        for key, value in d.items():
            print(f"{key} => {value}")

    tensorboard = TensorBoard(log_dir=f"logs/{model_name}")

    model = Sequential([
        Dense(128, input_dim=X_train.shape[1], activation='relu'),
        Dense(64, activation='relu'),
        Dense(32, activation='relu'),
        Dense(1)
    ])
    model.compile(loss='mean_squared_error', optimizer='adam', metrics=[soft_acc])
    
    model.fit(
        X_train,
        y_train,
        validation_data=(X_valid, y_valid),
        callbacks=[tensorboard],
        verbose=0,
        epochs=3000)
    #model.load_weights('./models/best.hdf5')
    
    pred = model.predict(X_valid)
    score = np.sqrt(metrics.mean_squared_error(pred, y_valid))
    print(f'Score (RMSE): {score}')
'''
    X_test, id_list = load_data('numeric', test_processing_level, dataset='test')

    test_pred = model.predict(X_test)
    test_pred = test_pred.flatten()
    pd.DataFrame({
            "Id": id_list,
            "SalePrice": test_pred 
        }).to_csv(f'predictions/{model_name}.csv', index=False, header=True)
'''
    #config = model.get_config()
    #print_dict(config)
    

NAIVE = f"Ames-Dataset-Sequential-NAIVE-{int(time.time())}"
NAIVE_PROCESSING_LEVEL = "DROP_ALL_NA"

WITH_NAFEATURE_HANDLING = f"Ames-Dataset-Sequential-WITH_NAFEATURE_HANDLING-{int(time.time())}"
WITH_NAFH_PROCESSING_LEVEL = 'HANDLE_NA_WITH_MEDIAN'

WITH_NAFEATURE_AND_OUTLIER_HANDLING = f"Ames-Dataset-Sequential-WITH_NAFEATURE_AND_OUTLIER_HANDLING-{int(time.time())}"
FULL_PROCESSING_LEVEL = 'FULL'

#X_train, X_valid, y_train, y_valid = load_data('numeric', 'DROP_ALL_NA')
#describe_data(X_train, X_valid, y_train, y_valid)
#build_network_and_compute_RMSE(NAIVE, NAIVE_PROCESSING_LEVEL, X_train, X_valid, y_train, y_valid)

X_train, X_valid, y_train, y_valid = load_data('numeric', 'HANDLE_NA_WITH_MEDIAN')
describe_data(X_train, X_valid, y_train, y_valid)
build_network_and_compute_RMSE(
    WITH_NAFEATURE_HANDLING, WITH_NAFH_PROCESSING_LEVEL, X_train, X_valid, y_train, y_valid)


#X_train, X_valid, y_train, y_valid = load_data('numeric', 'FULL')
#describe_data(X_train, X_valid, np.expm1(y_train), np.expm1(y_valid))
#X_test, id_list = load_data('numeric', 'FULL', dataset='test')
#print('----------------TEST SET-----------------',X_test )
#print('________________VALIDATION_SET____________',X_valid)
#build_network_and_compute_RMSE(
#    WITH_NAFEATURE_AND_OUTLIER_HANDLING, FULL_PROCESSING_LEVEL, X_train, X_valid, y_train, y_valid)
#print("X_train : " + str(X_train.shape))
#print("X_valid : " + str(X_valid.shape))
#print("y_train : " + str(y_train.shape))
#print("y_valid : " + str(y_valid.shape))

# RMSE39104.82612105051
# 37864.35116762256