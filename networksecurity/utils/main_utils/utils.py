import yaml
from networksecurity.exception.exception import NetworkSecurityException
import sys
import os
import numpy as np
import pickle

def read_yaml_file(file_path:str)->dict:
    """
    Reads a YAML file and returns its contents as a dictionary.
    
    Args:
        file_path (str): The path to the YAML file.
    Returns:
        dict: The contents of the YAML file as a dictionary.
    """
    try:
        with open(file_path, 'rb') as file:
            return yaml.safe_load(file)
    except Exception as e:
        raise NetworkSecurityException(e, sys)
def write_yaml_file(file_path :str,content:object,replace:bool=False)->None:
    """
    Writes a dictionary to a YAML file.
    
    Args:
        file_path (str): The path to the YAML file.
        data (dict): The data to write to the YAML file.
    """
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
            os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file_path,'w') as file:
            yaml.dump(content,file)
        
    except Exception as e:
        raise NetworkSecurityException(e, sys)