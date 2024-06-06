from loguru import logger
logger.catch(reraise=False, level='ERROR', exception=ValueError)
