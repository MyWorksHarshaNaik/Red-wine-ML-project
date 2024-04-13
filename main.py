from wineQuality import logger
from wineQuality.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline # noqa
from wineQuality.pipeline.stage_02_data_validation import DataValidationTrainingPipeline # noqa
from wineQuality.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline # noqa
from wineQuality.pipeline.stage_04_model_trainer import ModelTrainingPipeline # noqa
from wineQuality.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline  # noqa

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>> stage {STAGE_NAME} started <<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>> stage {STAGE_NAME} completed <<<\n\nx=====x")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f">>> stage {STAGE_NAME} started <<<")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>> stage {STAGE_NAME} completed <<<\n\nx=====x")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f">>> stage {STAGE_NAME} started <<<")
    data_ingestion = DataTransformationTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>> stage {STAGE_NAME} completed <<<\n\nx=====x")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Trainer Stage"

try:
    logger.info(f">>> stage {STAGE_NAME} started <<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>> stage {STAGE_NAME} completed <<<\n\nx=====x")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Evaluation Stage"

try:
    logger.info(f">>> stage {STAGE_NAME} started <<<")
    obj = ModelEvaluationTrainingPipeline()
    obj.main()
    logger.info(f">>> stage {STAGE_NAME} completed <<<\n\nx=====x")

except Exception as e:
    logger.exception(e)
    raise e
