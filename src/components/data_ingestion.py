# Built-in libraries
import os 
import sys

# Custom modules for exception handling and logging
from src.exception import CustomException
from src.logger import logging

import pandas as pd
from sklearn.model_selection import train_test_split

# Used to create configuration class with less boilerplate
from dataclasses import dataclass

from src.components.data_transformation import DataTransformationConfig
from src.components.data_transformation import DataTransformation

from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer


# =========================
# Configuration Class
# =========================
# This class stores all file paths related to data ingestion.
# Using @dataclass helps us avoid writing __init__ manually.
@dataclass
class DataIngestionConfig:
    # Path where train dataset will be saved
    train_data_path: str = os.path.join('artifacts', 'train.csv')

    # Path where test dataset will be saved
    test_data_path: str = os.path.join('artifacts', 'test.csv')

    # Path where raw (original) dataset copy will be saved
    raw_data_path: str = os.path.join('artifacts', 'raw.csv')


# =========================
# Data Ingestion Class
# =========================
# This class is responsible for:
# 1. Reading the dataset
# 2. Creating artifact folder
# 3. Saving raw data
# 4. Performing train-test split
# 5. Saving split datasets
class DataIngestion:
    
    def __init__(self):
        # Initialize configuration object so paths are available
        self.ingestion_config = DataIngestionConfig()
    

    def initiate_data_ingestion(self):
        """
        This method executes the full ingestion pipeline.
        Returns:
            Tuple containing paths of train, test, and raw datasets.
        """
        logging.info("Entered the Data Ingestion Method/Component")

        try:
            # =========================
            # Step 1: Read Dataset
            # =========================
            # Load CSV into pandas DataFrame
            df = pd.read_csv('notebooks\\data\\stud.csv')

            logging.info('Dataset successfully loaded into DataFrame')


            # =========================
            # Step 2: Create Artifacts Directory
            # =========================
            # Ensures folder exists before saving files.
            # exist_ok=True prevents error if folder already exists.
            os.makedirs(
                os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)


            # =========================
            # Step 3: Save Raw Data Copy
            # =========================
            # This is important for:
            # ✔ Data versioning
            # ✔ Debugging pipeline
            # ✔ Reproducibility
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)


            # =========================
            # Step 4: Train-Test Split
            # =========================
            # Splitting dataset into training and testing parts.
            # random_state ensures reproducibility.
            logging.info("Train-test split initiated")

            train_set, test_set = train_test_split(
                df,
                test_size=0.2,        # 20% data for testing
                random_state=42       # Fixed seed for same split every run
            )


            # =========================
            # Step 5: Save Split Data
            # =========================
            # Export datasets into artifacts folder
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Train and Test datasets saved in 'artifacts' folder")


            # =========================
            # Step 6: Return File Paths
            # =========================
            # Returning paths allows next pipeline component
            # (like Data Transformation) to directly consume them.
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
                self.ingestion_config.raw_data_path
            )

        except Exception as e:
            # Any error is wrapped into our custom exception
            # This helps provide:
            # ✔ File name
            # ✔ Line number
            # ✔ Proper logging
            raise CustomException(e, sys)

if __name__ == '__main__':
    obj = DataIngestion()
    train_data, test_data, raw_data = obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_data, test_data)

    modeltrainer = ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr, test_arr))