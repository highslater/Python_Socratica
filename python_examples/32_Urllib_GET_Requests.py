#!/usr/bin/env python3.7

"""32_Urllib_GET_Requests.py.

Thirty-Second Program of the Socratica Sexy-Hologram-Human/Computer-Hybrid
Python Series.

"""
import logging


LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename="LOG_files/LOG_32.Log",
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode='w')
logger = logging.getLogger()
logger.info("#32_Urllib_GET_Requests.py RUN / START")
