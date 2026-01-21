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
def save_numpy_array_data(file_path:str,array:np.array)->None:
    """
    Save numpy array data to file
    file_path : str : file path to save numpy array
    array : np.array : numpy array data to save
    """
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,'wb') as file_obj:
            np.save(file_obj,array)
    except Exception as e:
        raise NetworkSecurityException(e, sys)
def save_object(file_path:str,obj:object)->None:
    """
    Save a python object to a file using pickle
    file_path : str : file path to save the object
    obj : object : python object to be saved
    """
    try:
        
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,'wb') as file_obj:
            pickle.dump(obj,file_obj)
    except Exception as e:
        raise NetworkSecurityException(e, sys)