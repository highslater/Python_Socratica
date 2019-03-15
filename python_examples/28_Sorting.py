#!/usr/bin/env python3.7

"""28_Sorting.py.

Twenty-Eighth Program of the Socratica Sexy-Hologram-Human/Computer-Hybrid
Python Series.

"""
import logging


LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename="LOG_files/LOG_28.Log",
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode='a')
logger = logging.getLogger()
logger.info("28_Sorting.py RUN / START")
