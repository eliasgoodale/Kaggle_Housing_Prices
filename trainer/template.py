import numpy as np
from functools import reduce
import pandas as pd


processing_dict = {
    "first": [
        {
            "op_name": "prod",
            "targets": [10, 2],
        },
        {
            "op_name": "sum",
            "targets": [12]
        }
    ]
}

def compose(*functions):
    return reduce(lambda f, g: lambda x: f(g(x)), functions, lambda x: x)



def process_inputs(self, df_name, processing_dict): 
    for key, value in processing_dict.items():
        pipeline = value
        for idx, op in enumerate(pipeline):
            func = getattr(pd.Series, op["op_name"])
            inputs = op["targets"] if idx == 0 else [result, *op["targets"]]
            result = func(inputs)

# dataset .assign(**kwargs) Assign new columns to dataframe
dataset = pd.read_csv('../data/train.csv')

'''
columns: ['Id', 'MSSubClass', 'MSZoning', 'LotFrontage', 'LotArea', 'Street',
       'BsmtFinType2', 'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF', 'Heating',
       'HeatingQC', 'CentralAir', 'Electrical', '1stFlrSF', '2ndFlrSF',
       'LowQualFinSF', 'GrLivArea', 'BsmtFullBath', 'BsmtHalfBath', 'FullBath',
       'HalfBath', 'BedroomAbvGr', 'KitchenAbvGr', 'KitchenQual',
       'TotRmsAbvGrd', 'Functional', 'Fireplaces', 'FireplaceQu', 'GarageType',
       'GarageYrBlt', 'GarageFinish', 'GarageCars', 'GarageArea', 'GarageQual',
       'GarageCond', 'PavedDrive', 'WoodDeckSF', 'OpenPorchSF',
       'EnclosedPorch', '3SsnPorch', 'ScreenPorch', 'PoolArea', 'PoolQC',
       'Fence', 'MiscFeature', 'MiscVal', 'MoSold', 'YrSold', 'SaleType',
       'SaleCondition', 'SalePrice'],
      dtype='object')

shape: (1460, 81)

size: 118260

values: <class 'numpy.ndarray'>
[[1 60 'RL' ... 'WD' 'Normal' 208500]
 [2 20 'RL' ... 'WD' 'Normal' 181500]
 [3 60 'RL' ... 'WD' 'Normal' 223500]
 ...
 [1458 70 'RL' ... 'WD' 'Normal' 266500]
 [1459 20 'RL' ... 'WD' 'Normal' 142125]
 [1460 20 'RL' ... 'WD' 'Normal' 147500]]


'''


synth_features = {
    "A":[
        {
            'type': 'numeric',
            'func': lambda df, cols: df[cols].product(axis=1),
            'targets': ['C', 'D']
        },
        {
            'type': 'numeric',
            'func': lambda df, cols: df[cols].sum(axis=1),
            'targets': ['E']
        }
    ],
    'D': [
        {
            'type': 'replace',
            'func': lambda df, cols, val_dict: df[cols].replace(val_dict),
            'targets': ['D'],
            'values': {
                1: 'hello',
                2: 'world',
                3: 'how',
                4: 'are',
                5: 'you'
            }
        }
    ]
}

def combine_operations(df, ops, synthfeat):
    for idx, op in enumerate(ops):
        cols = op['targets'] if idx == 0 else [synthfeat, *op['targets']]
        if op['type'] == 'numeric':  
            df[synthfeat] = op['func'](df, cols)
        else:
            df[synthfeat] = op['func'](df, cols, op['values'])

def create_synthetic_features(dataframe, synthfeatures_list):
    for synthfeature, ops_pipeline in synthfeatures_list.items():    
        combine_operations(dataframe, ops_pipeline, synthfeature)

df = pd.DataFrame()

df['C'] = [0, 2, 3, 4, 5]
df['D'] = [1, 2, 3, 4, 5]
df['E'] = [1, 2, 3, 4, 5]

create_synthetic_features(df, synth_features)

print(df.head())