import os
import datetime as dt
import numpy as np
import pandas as pd
from dataclasses import dataclass

#Local Components
from src.components.data_viz import VizStore
from src.components.data_transformation import DataTransformation
from src.components.data_ingestion import DataIngestion
                #df.to_csv(self.ingestion_config.raw_data_path) 
@dataclass
class DataPredictionConfig():
    # Configuration for final file paths for train, test and raw_data
    artifact_time = "Run " + str(dt.datetime.now().strftime('%m_%d_%Y_%H_%M'))
    raw_data_path = os.path.join((f"artifacts\{artifact_time}"),"data.csv")
    final_model_path = os.path.join("artifacts","model")
    print(raw_data_path)

class DataPrediction(DataIngestion):
    def __init__(self,df,viz):
        self.pred_config = DataPredictionConfig()
        self.df = df
        DataIngestion.__init__(self, viz)

    def initialize_data_prediction(self):
            data_trans = DataTransformation()
            #y_pred = model.predict(data_trans[0])

            ########################
            #Here using the predciton model saved in artifacts/model folder.
            ########################

            if self.viz==True:
                data_trans.to_csv(self.pred_config.raw_data_path)
                GUIviz = VizStore(data_trans) # To initialize data visualization
                GUIviz.to_csv(self.ingestion_config.raw_data_path,index=False) 
            else:
                 print("--Training Data--")
            

            

