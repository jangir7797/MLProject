import os
import sys
import dill
import numpy as np
import pandas as pd
from src.exception import CustomException

def save_object(file_path: str, obj: object):
    """
    Save an object to a file using pickle.
    :param file_path: Path to the file where the object will be saved.
    :param obj: The object to save.
    """
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)