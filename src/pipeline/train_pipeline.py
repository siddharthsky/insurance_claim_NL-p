import os
import numpy as np
import pandas as pd


#Local Components
from src.components.data_viz import VizStore
from src.components.data_transformation import DataTransformation
from src.utils import load_object




class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, df):
        try:
            model_path = "artifacts\\final_model\\model.pkl"
            preprocessor_path = "artifacts\\final_model\\preprocessor.pkl"
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)
            data_scaled = preprocessor.transform(df)
            preds = model.predict(data_scaled)
            return preds
        
        except Exception as e:
            print(e)

   
    



