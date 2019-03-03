import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from scipy.stats import skew
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

    def __init__(self, paths, processing_fn):
        self.train_path = paths['train']
        self.test_path = paths['test']
        self.processing_fn = processing_fn
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

    def process_data(self, df_name):
        df = self.dataframes[df_name]
        self.dataframes[df_name] = self.processing_fn(df)

    def feature_corr(self, df_name, target):
        corr = self.dataframes[df_name].corr()
        corr.sort_values([target], ascending=False, inplace=True)
        print(getattr(corr, target))
    
    def feature_types(self, df_name, split_dataframe=False):
        df = self.dataframes[df_name].copy()
        categorical_features = df.select_dtypes(include = ["object"]).columns
        numerical_features = df.select_dtypes(exclude = ["object"]).columns
        print("Numerical features : " + str(len(numerical_features)))
        print("Categorical features : " + str(len(categorical_features)))
        if split_dataframe:
            self.dataframes[f"{df_name}_num"] = df[numerical_features]
            self.dataframes[f"{df_name}_cat"] = df[categorical_features]

    def fill_na_numerical_columns(self, df_name, value_fn):
        df = self.dataframes[df_name]
        print(f'Before fill: {str(df.isnull().values.sum())}')
        value = getattr(df, value_fn)
        df = df.fillna(value())
        print(f'After fill: {str(df.isnull().values.sum())}')

    def fill_na_categorical_columns(self, df_name):
        df = self.dataframes[df_name].copy()
        print(f"Before fill: {str(df.isnull().values.sum())}")
        self.dataframes[df_name] = pd.get_dummies(df)
        print(f"After fill: {str(df.isnull().values.sum())}")
    
    def join_dataframes(self, new_df_name, df_names, axis=1):
        join_dfs = [self.dataframes[df_name] for df_name in df_names]
        print(f"Joining Dataframes: {', '.join(df_names)}")
        new_df = pd.concat(join_dfs, axis)
        r, c = new_df.shape
        print(f"Features in new dataframe : {c}")
        print(f"Rows in new dataframe: {r}")
        self.dataframes[new_df_name] = new_df

    
    def drop_column_from(self, df_name, column_name):
        self.dataframes[df_name].drop(column_name, axis=1, inplace = True)
    
    def skew_features(self, df_name):
        df = self.dataframes[df_name]
        skewness = df.apply(lambda x: skew(x))
        skewness = skewness[abs(skewness) > 0.5]
        skewed_features = skewness.index
        print(skewed_features)
        df[skewed_features] = np.log1p(df[skewed_features])

    def load_data(self, from_df_name, y_target, test_size, random_state=0):
        df = self.dataframes[from_df_name].copy()
        print(type(y_target))
        return train_test_split(df, y_target, test_size, random_state)
        
    def combine_operations(self, df, ops, synthfeat):
        for idx, op in enumerate(ops):
            cols = op['targets'] if idx == 0 else [synthfeat, *op['targets']]
            if op['name'] == 'product':  
                df[synthfeat] = self.operations['product'](df, cols)
            elif op['name'] == 'replace':
                df[synthfeat] = self.operations['replace'](df, cols, op['values'])
            else:
                print('No operation')

    def create_synthetic_features(self, df_name, synthfeatures_list):
        dataframe = self.dataframes[df_name]
        for synthfeature, ops_pipeline in synthfeatures_list.items():    
            self.combine_operations(dataframe, ops_pipeline, synthfeature)




