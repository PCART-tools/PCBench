from loguru import logger
logger.catch(ValueError, message='An exception occurred!')
