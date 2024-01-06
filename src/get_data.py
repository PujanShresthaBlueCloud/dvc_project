# read parameters
# process
# return dataframe

import os
import yaml 
import pandas as pd

# get the arguments in the cli command we need argparse
import argparse 

def read_params(config_path: str) -> dict:
    """ 
    Read the configuration yaml file and returns the configuration
    Args:
        config_path: path to the configuration file i.e, params.yaml
    returns:
        config: all the key value pairs in the configuration file
    """

    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)

    return config

def get_data(config_path: str) -> pd.DataFrame:
    """ 
    Get the data from data source mentioned in params.yaml 
    Args:
        config_path: path to configuation file i.e, params.yaml
    Returns:
        df: dataset 
    """

    config = read_params(config_path)
    data_path = config["data_source"]["s3_source"]
    df = pd.read_csv(data_path, sep=",", encoding="utf-8")

    return df

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    get_data(config_path=parsed_args.config)


