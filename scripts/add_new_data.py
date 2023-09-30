import os
import pandas as pd

parent_path = os.path.dirname('../')

from utils.JsonClassUtils import JsonClassUtils


def add_new_raw_data_to_clean_data(filename, n_files):

    temp_data_df = JsonClassUtils().transform_data_into_csv(
        parent_folder='/app/raw_files', n_files=n_files)
    filename_complete = '/app/clean_data/'+filename+'.csv'

    if n_files:
        data_df = pd.read_csv(filename_complete)
        data_df = pd.concat([data_df, temp_data_df])
        data_df = data_df.drop_duplicates(['date', 'city'])
    else:
        data_df = temp_data_df
    data_df.to_csv(filename_complete, index=False)
