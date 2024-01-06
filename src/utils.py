import sys
import os
import pickle

from src.logger import logging
from src.exception import CustomException

import pandas as pd
import numpy as np

def create_file(obj,path):
    try:
        dirname = os.path.dirname(path) # Output will be artifacts
        # To Create the folder "ARTIFACTS"
        os.path.makedir(dirname,exist_ok=True)

        with open(path,"wb") as file_obj:
            pickle.dump(obj,file_obj)

    except Exception as e:
        logging.info("Exception occured at Object Creation")
        raise CustomException(e,sys)


