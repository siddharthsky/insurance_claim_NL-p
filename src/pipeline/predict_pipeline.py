import os
import numpy as np
import pandas as pd
import datetime as dt

#Local Components
from src.components.data_viz import VizStore
from src.utils import load_object

class PredictPipeline:
    def __init__(self,raw_filez):
        self.raw_filez = raw_filez
        if ".csv" in str(self.raw_filez) or ".xlsx" in str(self.raw_filez):
           self.predict_visualize()
           self.sub = True 
        else:
            self.sub = "File Uploaded is not in valid format."
        

    def predict_visualize(self):
        artifact_time = "Run " + str(dt.datetime.now().strftime('%m_%d_%Y_%H_%M'))
        raw_data_path = os.path.join((f"artifacts\{artifact_time}"),"data.csv")
        os.makedirs(os.path.dirname(raw_data_path),exist_ok=True)
        try:
            if ".csv" in str (self.raw_filez):
                df = pd.read_csv(self.raw_filez) 
                df.to_csv(raw_data_path) 
            elif ".xlsx" in str (self.raw_filez):
                df = pd.read_excel(self.raw_filez) 
                df.to_csv(raw_data_path)
            else:
                return None
            VizStore(df) # To initialize data visualization
            
            '''
            model_path = "artifacts\\final_model\\model.pkl"
            preprocessor_path = "artifacts\\final_model\\preprocessor.pkl"
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)
            data_scaled = preprocessor.transform(df)
            preds = model.predict(data_scaled)
            preds_df = pd.DataFrame(preds)
            frames = [df,preds_df]
            final_df= pd.concat(frames,axis=1)
            '''

            #VizStore(df) # To initialize data visualization
            

        except Exception as e:
            print(e)

   
    



