
import os, sys
from src.ANPR.entity.config_entity import *
from src.ANPR.entity.artifacts_entity import *
from src.ANPR.logger import logging
from src.ANPR.exception import ANPRException
from src.ANPR.constants import *
from src.ANPR.utils.utils import *
from src.ANPR.config.s3_operations import S3Operation

class ModelPusher:
    def __init__(self,model_pusher_config:ModelPusherConfig,
        model_trainer_artifacts : ModelTrainerArtifacts,
        s3_operations: S3Operation):
        self.model_pusher_config = model_pusher_config
        self.model_trainer_artifacts = model_trainer_artifacts
        self.s3_operations = s3_operations

    def initiate_model_pusher(self):
        """
        Method Name :   initiate_model_pusher
        Description :   This method initiates model pusher. 
        
        Output      :    Model pusher artifact 
        """
        logging.info("Entered initiate_model_pusher method of ModelTrainer class")
        try:
            logging.info("Uploaded best model to s3 bucket")
            
            # Uploading the best model to s3 bucket
            self.s3_operations.upload_file(
                self.model_trainer_artifacts.trained_model_path,
                self.model_pusher_config.S3_MODEL_KEY_PATH,
                self.model_pusher_config.BUCKET_NAME,
                remove=False,
            )
            logging.info("Exited initiate_model_pusher method of ModelTrainer class")
        except Exception as e:
            raise ANPRException(e,sys)