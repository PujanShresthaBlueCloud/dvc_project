# get the data from data source
# save it in the data_raw for further processing

import os
from get_data import read_params, get_data
import argparse

def load_and_save(config_path):
    """
    Loads the data from config file data source and saves it inside data/raw folder for further 
    processing.
    Args:
        config_path: path to the config file
    Returns:
        None
    """

    config = read_params(config_path)
    df = get_data(config_path)
    new_cols = [col.replace(" ", "_") for col in df.columns]
    raw_data_path = config["load_data"]["raw_dataset_csv"]
    df.to_csv(raw_data_path, sep=",", index=False, header=new_cols)

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--config', default='params.yaml')
    parsed_args = args.parse_args()
    load_and_save(config_path=parsed_args.config)
