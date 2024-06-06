from loguru import logger
logger.catch(message='An exception occurred!', exception=ValueError)
