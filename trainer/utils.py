import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from processing import FILL_NA_DICT
pd.set_option('display.float_format', lambda x: '%.3f' % x)




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

    def __init__(self, paths):
        self.train_path = paths['train']
        self.test_path = paths['test']
        self.read_in_data()

    def read_in_data(self):
        self.dataframes = {}
        self.dataframes['train'] = pd.read_csv(self.train_path)
        self.dataframes['test'] =  pd.read_csv(self.test_path)

    def check_duplicate_IDs(self):
        for key,value in self.dataframes.items():
            idsUnique = len(set(value.Id))
            idsTotal = value.shape[0]
            idsDupli = idsTotal - idsUnique
            print("There are " + str(idsDupli) + " duplicate IDs for " + str(idsTotal) + " total entries")
    
    def drop_column_from(self, df_name, column_name):
        self.dataframes[df_name].drop(column_name, axis=1, inplace = True)
    
    def fill_na_rows(self, df_name, fill_dict):
        df = self.dataframes[df_name]
        
        for key, value in fill_dict.items():
            print(f"Filling empty {key} values in {df_name} with {value}....")
            df.loc[:, key] = df.loc[:, key].fillna(value)    


    

paths = {
    'train': '../data/train.csv',
    'test': '../data/test.csv'
}

# row_name : fill_val


pre = Preprocessor(paths)
pre.check_duplicate_IDs()
pre.drop_column_from('train', 'Id')

pre.fill_na_rows('train', FILL_NA_DICT)

print(pre.dataframes['train'].head())
'''
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