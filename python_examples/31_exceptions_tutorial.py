#!/usr/bin/env python3.7

"""31_exceptions_tutorial.py.

Thirty-First Program of the Socratica Sexy-Hologram-Human/Computer-Hybrid
Python Series.

"""
import logging
import time


LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename="LOG_files/LOG_31.Log",
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode='w')
logger = logging.getLogger()
logger.info("#31_exceptions_tutorial.py RUN / START")


def read_file_timed(path):
    """Return the contents of a file at 'path' and measure time required."""
    start_time = time.time()

    try:
        f = open(path, mode='rb')
        data = f.read()
        return data
    except FileNotFoundError as err:
        logger.error(err)
        raise
    else:
        f.close()
    finally:
        stop_time = time.time()
        dt = stop_time - start_time
        logger.info(("Time Required for"
                     "{file} = {time}").format(file=path, time=dt))

data1 = read_file_timed("../python_examples/files/ImperialMarch60.wav")

data2 = read_file_timed("../python_examples/files/Implementing_MPLS.mp4")

data3 = read_file_timed("../python_examples/files/ImaginaryFile.wav")
