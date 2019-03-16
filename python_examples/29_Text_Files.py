#!/usr/bin/env python3.7

"""29_Text_Files.py.

Twenty-Ninth Program of the Socratica Sexy-Hologram-Human/Computer-Hybrid
Python Series.

"""
import logging


LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename="LOG_files/LOG_29.Log",
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode='a')
logger = logging.getLogger()
logger.info("29_Text_Files.py RUN / START")

# ====== Read Files ======

f = open("./files/help_1.txt")
text = f.read()
f.close()
print(text)


with open("./files/help_2.txt") as fobj:
    text = fobj.read()
print(text)


try:
    with open("Future_Lottery_Numbers.txt") as f:
        text = f.read()
except FileNotFoundError:
    print("File Not Found, Returning: ", end="")
    text = None
print(text)

# ====== Write Files ======

oceans = ["Pacific", "Atlantic", "Indian", "Southern", "Arctic"]
with open("./files/oceans.txt", 'w') as f:
    for ocean in oceans:
        f.write(ocean)
        f.write("\n")

with open("./files/oceans.txt", 'w') as f:
    for ocean in oceans:
        print(ocean, file=f)

with open("./files/oceans.txt", 'a') as f:
    print(23 * "=", file=f)
    print("These are the 5 oceans", file=f)
