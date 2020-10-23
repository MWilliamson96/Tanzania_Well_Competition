import pathlib
this_path = pathlib.Path().absolute()
d_path = this_path.parent / "data"

import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import OneHotEncoder

def get_dataframes(data_path = d_path):
    '''
    function to retrieve the data for this project as dataframes
    
    parameters:
    --data_path: optional, string or pathlib.Path() object that describes the location of the data from the
                current working directory
    returns:
    --tuple containing pandas dataframes in the format (x_train, x_test, y_train)
    '''
    x_train_filename = 'Pump_it_Up_Data_Mining_the_Water_Table_-_Training_set_values.csv'
    x_test_filename = 'Pump_it_Up_Data_Mining_the_Water_Table_-_Test_set_values.csv'
    y_train_filename = 'Pump_it_Up_Data_Mining_the_Water_Table_-_Training_set_labels.csv'
    
    x_train = __open_local_csv(x_train_filename, data_path)
    x_test = __open_local_csv(x_test_filename, data_path)
    y_train = __open_local_csv(y_train_filename, data_path)
    
    return (x_train, x_test, y_train)

def data_preprocessing(x_tr, y_tr):
    '''
    performs data preprocessing for the water_well project
    
    parameters:
    --x_tr: x train data as a dataframe
    --y_train: y train data as a dataframe
    
    returns:
    --tuple of preprocessed dataframes in format (x_train, y_train)
    '''
    x_train = x_tr.copy()
    y_train = y_tr.copy()
    x_train.drop(['date_recorded','installer','funder','wpt_name','subvillage',
                  'ward','recorded_by','scheme_name','scheme_management','extraction_type',
                  'extraction_type_class','payment','public_meeting','permit','management',
                  'management_group','source','source_class','waterpoint_type_group',
                  'latitude','longitude','num_private','region_code','district_code'], inplace=True, axis=1)

    x_train_nums= x_train.select_dtypes(exclude="object")
    x_train_cat= x_train.select_dtypes(include="object")
    ohe=OneHotEncoder(drop='first', sparse=False)
    x_train_ohe=pd.DataFrame(ohe.fit_transform(x_train_cat),
                             columns=ohe.get_feature_names(x_train_cat.columns),index=x_train_cat.index)
    si=SimpleImputer()
    x_nums_si=pd.DataFrame(si.fit_transform(x_train_nums), index= x_train_nums.index, columns= x_train_nums.columns)
    scale= StandardScaler()
    x_train_nums_scaled= pd.DataFrame(scale.fit_transform(x_nums_si), index= x_nums_si.index, columns= x_nums_si.columns)
    x_final= x_train_nums_scaled.join(x_train_ohe)
    
    return (x_final, y_train)

def __open_local_csv(filename, data_path):
    '''
    checks that the csv filepath exists for given filename and returns a dataframe containing its
    values if it does exist
    
    parameters:
    
    --filename: should be a string containing the name of the csv to be opened
    --data_path: string or pathlib.Path() object that describes the location of the data from the
                current working directory
    
    returns:
    
    --pandas DataFrame object if csv_path exists, else prints error msg and returns None
    
    '''
    
    csv_path = data_path / filename
    if csv_path.exists():
        return pd.read_csv(csv_path, index_col = 'id')
    else:
        print(f'the specified filepath does not exist: {csv_path}')
        return None
    
    
def get_strict_features():
    '''
    returns list of features used for strict dataset
    '''
    strict_features = ['amount_tsh', 'gps_height', 'basin', 'region',
                            'lga', 'population', 'construction_year', 'extraction_type_group', 'payment_type',
                            'quality_group', 'quantity', 'source_type', 'waterpoint_type']
    return strict_features

def get_loose_features():
    '''
    returns list of features used for loose dataset
    '''
    loose_features = ['amount_tsh', 'gps_height', 'basin', 'region', 'lga', 'ward', 'population',
                      'public_meeting', 'scheme_management', 'permit', 'construction_year', 'extraction_type_group',
                      'payment_type', 'water_quality', 'quantity', 'source', 'waterpoint_type']
    return loose_features

def get_numeric_features(f_names):
    '''
    returns list of numeric features within given feature set
    '''
    numeric = ['amount_tsh', 'population', 'construction_year', 'gps_height']
    num_features = [x for x in f_names if x in numeric]
    return num_features

def get_categorical_features(f_names):
    '''
    returns list of categorical features within given feature set
    '''
    categorical = ['basin', 'region', 'lga', 'ward',
                   'public_meeting', 'scheme_management', 'permit','extraction_type_group',
                   'payment_type', 'water_quality', 'quantity', 'source',
                   'waterpoint_type', 'source_type', 'quality_group']
    cat_features = [x for x in f_names if x in categorical]
    return cat_features