import pathlib
this_path = pathlib.Path().absolute()
data_path = this_path.parent / "data"

import pandas as pd

def get_dataframes():
    '''
    function to retrieve the data for this project as dataframes
    
    --returns:
    a tuple containing pandas dataframes in the format (x_train, x_test, y_train)
    '''
    x_train_filename = 'Pump_it_Up_Data_Mining_the_Water_Table_-_Training_set_values.csv'
    x_test_filename = 'Pump_it_Up_Data_Mining_the_Water_Table_-_Test_set_values.csv'
    y_train_filename = 'Pump_it_Up_Data_Mining_the_Water_Table_-_Training_set_labels.csv'
    
    x_train = __open_local_csv(x_train_filename)
    x_test = __open_local_csv(x_test_filename)
    y_train = __open_local_csv(y_train_filename)
    
    return (x_train, x_test, y_train)

def __open_local_csv(filename):
    '''
    checks that the csv filepath exists for given filename and returns a dataframe containing its
    values if it does exist
    
    --parameters:
    
    filename: should be a string containing the name of the csv to be opened
    
    --returns:
    
    pandas DataFrame object if csv_path exists, else prints error msg and returns None
    '''
    
    csv_path = data_path / filename
    if csv_path.exists():
        return pd.read_csv(csv_path, index_col = 'id')
    else:
        print(f'the specified filepath does not exist: {csv_path}')
        return None