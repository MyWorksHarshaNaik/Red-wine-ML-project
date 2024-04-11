from wineQuality import logger
from wineQuality.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline # noqa
from wineQuality.pipeline.stage_02_data_validation import DataValidationTrainingPipeline # noqa

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
