import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#from processing import FILL_NA_DICT, NUMERIC_COLUMNS_AS_CATEGORIES, CATEGORICAL_COLUMNS_AS_NUMBERS
import time
pd.set_option('display.float_format', lambda x: '%.3f' % x)

# https://pbpython.com/categorical-encoding.html


class Plotter:
    def __init__(self):
        pass
    
    def scatter(self, df, config):
        plt.scatter(df[config['xlabel']], df[config['ylabel']], c=config['color'], marker=config['marker'])
        plt.title(config['title'])
        plt.xlabel(config['xlabel'])
        plt.ylabel(config['ylabel'])
        plt.show()


class Preprocessor:
    operations = {
        'product': lambda df, cols: df[cols].product(axis=1),
        'replace': lambda df, cols, val_dict: df[cols].replace(val_dict)
    }

    def __init__(self, paths):
        self.train_path = paths['train']
        self.test_path = paths['test']
        self.read_in_data()

    def read_in_data(self):
        self.dataframes = {}
        self.dataframes['train'] = pd.read_csv(self.train_path)
        self.dataframes['test'] =  pd.read_csv(self.test_path)

    def check_duplicate_IDs(self):
        for _, value in self.dataframes.items():
            idsUnique = len(set(value.Id))
            idsTotal = value.shape[0]
            idsDupli = idsTotal - idsUnique
            print("There are " + str(idsDupli) + " duplicate IDs for " + str(idsTotal) + " total entries")
    
    def drop_column_from(self, df_name, column_name):
        self.dataframes[df_name].drop(column_name, axis=1, inplace = True)

    def fill_na_rows(self, df_name, fill_dict):
        df = self.dataframes[df_name]
        for key, value in fill_dict.items():
            time.sleep(1/10)
            print(f"Filling empty {key} values in {df_name} with {value}....")
            df.loc[:, key] = df.loc[:, key].fillna(value)
   
    def combine_operations(self, df, ops, synthfeat):
        for idx, op in enumerate(ops):
            cols = op['targets'] if idx == 0 else [synthfeat, *op['targets']]
            if op['name'] == 'product':  
                df[synthfeat] = self.operations['product'](df, cols)
            elif op['name'] == 'replace':
                df[synthfeat] = self.operations['replace'](df, cols, op['values'])
            else:
                print(f'No operation {op['name']} available')

    def create_synthetic_features(self, df_name, synthfeatures_list):
        dataframe = self.dataframes[df_name]
        for synthfeature, ops_pipeline in synthfeatures_list.items():    
            self.combine_operations(dataframe, ops_pipeline, synthfeature)




SYNTHETIC_FEATURES = {
    "HasMasVnr": [
        {
            'name': "replace",
            'targets': ["MasVnrType"],
            "values": {
                "BrkCmn" : 1, 
                "BrkFace" : 1, 
                "CBlock" : 1, 
                "Stone" : 1, 
                "None" : 0
            }
        },
    ],
    # House completed before sale does the same but for only Partial values
    "BoughtOffPlan": [
        {
            'name': 'replace',
            'targets': ['SaleCondition'],
            'values': {
                "Abnorml" : 0,
                "Alloca" : 0,
                "AdjLand" : 0,
                "Family" : 0,
                "Normal" : 0,
                "Partial" : 1
            }
        },
    ],
    # Condense values for overall grade to reduce feature redundancy
    "OverallGrade":[
        {
            "name": 'product',
            'targets': ["OverallQual", "OverallCond"],
        },
    ],
    # Write function to cache partially computed values
    "TotalBath":[
        {
            "op": 'multiply',
            "targets": [0.5, "BsmtHalfBath"]
        },
        {
            "op": "multiply",
            "targets": [0.5, "HalfBath"]
        },
        {
            "op": "add",
            "targets": ["0", "1", "BsmntFullBath", "FullBath"]
        }
}  

paths = {
    'train': '../data/train.csv',
    'test': '../data/test.csv'
}

# row_name : fill_val


prep = Preprocessor(paths)
prep.check_duplicate_IDs()
prep.create_synthetic_features('train', SYNTHETIC_FEATURES)
print(prep.dataframes['train']['OverallGrade'])
print(prep.dataframes['train']['BoughtOffPlan'])
#pre.drop_column_from('train', 'Id')





'''

#print(pre.dataframes['train'].head())

#print(pre.dataframes['train'].head(5))

scatter1_config = {
    'title': 'Looking for outliers',
    'xlabel': 'GrLivArea',
    'ylabel': 'SalePrice',
    'color': 'blue',
    'marker': 's'
}


plotter = Plotter()

plotter.scatter(pre.dataframes['train'], scatter1_config)

'''