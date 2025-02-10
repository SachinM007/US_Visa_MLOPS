import os
import sys


import yaml
import dill
import numpy as np
from pandas import DataFrame

from us_visa.logger import logging
from us_visa.exception import USvisaException


#read data from a yaml file and return a dict
def read_yaml_file(file_path: str) -> dict:
    try:
        with open(file_path, "rb") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise USvisaException(e, sys) from e

#accepts a python object and produces a yaml document
def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as file:
            yaml.dump(content, file)
    except Exception as e:
        raise USvisaException(e, sys) from e
    

#read a serialized object from a file - desirialize
def load_object(file_path: str) -> object:
    try:
        with open(file_path, "rb") as file:
            obj = dill.load(file)

        return obj
    except Exception as e:
        raise USvisaException(e, sys) from e
    
#save a object as a serialized object- serialization Pickle an object to a file.
def save_object(file_path: str, obj: object) -> None:
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file:
            dill.dump(file)
    except Exception as e:
        raise USvisaException(e, sys) from e
    
#save numpy array data to a file
def save_numpy_array_data(file_path: str, array: np.array) -> None:
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file:
            np.save(file, array)
    except Exception as e:
        raise USvisaException(e, sys) from e
    
#load numpy array data from a file
def load_numpy_array_data(file_path: str) -> np.array:
    try:
        with open(file_path, "rb") as file:
            return np.load(file)
    except Exception as e:
        raise USvisaException(e, sys) from e

def drop_columns(df: DataFrame, cols: list) -> DataFrame:
    try:
        return df.drop(columns=cols, axis=1)
    except Exception as e:
        raise USvisaException(e, sys) from e