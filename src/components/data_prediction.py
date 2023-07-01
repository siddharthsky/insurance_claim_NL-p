import os
import datetime as dt
import numpy as np
import pandas as pd
from dataclasses import dataclass

#Local Components
from src.components.data_viz import VizStore
from src.components.data_transformation import DataTransformation

@dataclass
class DataPredictionConfig():
    # Configuration for final file paths for train, test and raw_data
    artifact_time = "Run " + str(dt.datetime.now().strftime('%m_%d_%Y_%H_%M'))
    raw_data_path = os.path.join((f"artifacts\{artifact_time}"),"data.csv")
    final_model_path = os.path.join("artifacts","model")
    print(raw_data_path)

class DataPrediction():
    def __init__(self,df,viz=False):
        self.pred_config = DataPredictionConfig()
        self.df = df
        self.viz = viz
        
    def initialize_data_prediction_viz(self): 
        data_trans = DataTransformation()
        #y_pred = model.predict(data_trans[0])

                ########################
                #Here using the prediction model saved in artifacts/model folder.
                ########################
       
        if self.viz == True: 
            GUIviz = VizStore(data_trans) # To initialize data visualization
            GUIviz.to_csv(self.pred_config.raw_data_path,index=False) #output CSV file # special predictions with vizualization enabled 
        else:
            print("PASS")



            

            

