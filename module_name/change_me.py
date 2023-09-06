from . import settings
from .binds import *
import logging

logger = logging.getLogger(settings.PROG_NAME)

def main():
    logger.info("Starting")