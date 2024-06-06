from loguru import logger
logger.add(serialize=False, sink='error.log')
