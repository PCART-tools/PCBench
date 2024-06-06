from loguru import logger
logger.catch(exception=ValueError, message='An exception occurred!')
