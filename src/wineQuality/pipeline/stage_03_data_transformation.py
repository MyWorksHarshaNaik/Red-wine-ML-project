from wineQuality.config.configuration import ConfigurationManager
from wineQuality.components.data_transformation import DataTransformation
from wineQuality import logger # noqa
from pathlib import Path


STAGE_NAME = "Data Transformation Stage"


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), "r") as f:
                status = f.read().split(" ")[-1]

            if status == "True":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config() # noqa
                data_transformation = DataTransformation(config=data_transformation_config) # noqa
                data_transformation.train_test_spliting()

            else:
                raise Exception("Your data shema is not valid")

        except Exception as e:
            print(e)
