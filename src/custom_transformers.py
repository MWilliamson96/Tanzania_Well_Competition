import pandas as pd

from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline

import data_functions
import numpy as np

from datetime import datetime

class BinInstaller(TransformerMixin, BaseEstimator):
    def __init__(self):
        pass
    
    def fit(self, X, y=None):
        return self
    
    def _to_df(self, X):
        if type(X) != pd.DataFrame:
            if type(X) != list:
                if type(X) == pd.Series:
                    data = pd.DataFrame(X)
                elif type(X) == dict:
                    data = pd.DataFrame([X])
                else:
                    raise ValueError('X must be a dataframe, list, series, or dictionary  object.')
            else:
                data = pd.DataFrame(X)
        else:
            data = X.copy()
        return data
        
    def transform(self, X):
        data = self._to_df(X)
        others = data['installer'].value_counts().index[data['installer'].value_counts() < 10]
        is_other = lambda x: 'Other' if x in others else x
        data['installer'] = data['installer'].map(is_other)
        data['installer'] = data['installer'].fillna('Unknown')
        return data

    
class TransformConstructionYear(TransformerMixin, BaseEstimator):
    def __init__(self):
        self.current_year = datetime.now().year
    
    def fit(self, X, y=None):
        return self
    
    def _to_df(self, X):
        if type(X) != pd.DataFrame:
            if type(X) != list and type(X) != np.ndarray:
                if type(X) == pd.Series:
                    data = pd.DataFrame(X)
                elif type(X) == dict:
                    data = pd.DataFrame([X])
                else:
                    raise ValueError('X must be a dataframe, list, series, or dictionary  object.')
                    
            else:
                data = pd.DataFrame(X)
        else:
            data = X.copy()
        return data
    
    def _bin_data(self, x):
        if x == 0:
            return 0 
        else:
            return self.current_year - x 
        
    def transform(self, X):
        data = self._to_df(X)
        data['construction_year'] = data['construction_year'].apply(self._bin_data)
        return data
    
class ChooseStrictFeatures(TransformerMixin, BaseEstimator):
    def __init__(self):
        pass
    
    def fit(self, X, y=None):
        return self
    
    def _to_df(self, X):
        if type(X) != pd.DataFrame:
            if type(X) != list:
                if type(X) == pd.Series:
                    data = pd.DataFrame(X)
                elif type(X) == dict:
                    data = pd.DataFrame([X])
                else:
                    raise ValueError('X must be a dataframe, list, series, or dictionary  object.')
            else:
                data = pd.DataFrame(X)
        else:
            data = X.copy()
        return data
        
    def transform(self, X):
        data = self._to_df(X)
        data = data[data_functions.get_strict_features()]
        return data
    
class ChooseLooseFeatures(TransformerMixin, BaseEstimator):
    def __init__(self):
        pass
    
    def fit(self, X, y=None):
        return self
    
    def _to_df(self, X):
        if type(X) != pd.DataFrame:
            if type(X) != list:
                if type(X) == pd.Series:
                    data = pd.DataFrame(X)
                elif type(X) == dict:
                    data = pd.DataFrame([X])
                else:
                    raise ValueError('X must be a dataframe, list, series, or dictionary  object.')
            else:
                data = pd.DataFrame(X)
        else:
            data = X.copy()
        return data
        
    def transform(self, X):
        data = self._to_df(X)
        data = data[data_functions.get_loose_features()]
        return data