from src.components.data_ingestion import DataIngestion

obj=DataIngestion()
train_data,test_data=obj.initialize_data_ingestion()
#data_trasformer=DataTransformation()
#train_arr,test_arr,_=data_trasformer.initialize_data_transformation(train_data,test_data)