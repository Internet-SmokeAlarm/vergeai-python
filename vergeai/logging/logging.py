from loguru import logger
import sys

def initialize_logger(log_lvl):
    logger.remove()
    logger.add(sys.stdout, level=log_lvl)

def log_debug(msg):
    logger.debug(msg)

def log_info(msg):
    logger.info(msg)

def log_warning(msg):
    logger.warning(msg)

def log_error(msg):
    logger.error(msg)
