#!/usr/bin/env python3.7

"""32_Urllib_GET_Requests.py.

Thirty-Second Program of the Socratica Sexy-Hologram-Human/Computer-Hybrid
Python Series.

"""
import logging
from urllib import request


LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename="LOG_files/LOG_32.Log",
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode='w')
logger = logging.getLogger()
logger.info("#32_Urllib_GET_Requests.py RUN / START")

resp = request.urlopen("https://www.wikipedia.org")
print("Response Code is:", resp.code)
print("Response Length is:", resp.length, "bytes")
print("Response Peak is:\n", resp.peek())

data = resp.read()
print("The datatype is:", type(data), "The size is:", len(data))
html = data.decode("UTF-8")
print("The datatype is:", type(html),
      "The Length is:", len(html),
      "\nThe First 500 characters are:\n", html[:500])
