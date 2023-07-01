
import os
import dill
import pandas as pd
import numpy as np

def save_object(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path,exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        print(e)
    
def evaluate_model(X_train,y_train,X_test,y_test,models,param):
   pass    


def load_object(file_path):
    try:
        with open(file_path,"rb") as file_obj:
            return dill.load(file_obj)
    except Exception as e:
        print(e)
    