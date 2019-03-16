#!/usr/bin/env python3.7

"""25_JSON.py.

Twenty FifthProgram of the Socratica Sexy-Hologram-Human/Computer-Hybrid
Python Series.

"""
import logging
import json


LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename="LOG_files/LOG_25.Log",
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode='a')
logger = logging.getLogger()
logger.info("25_JSON.py RUN / START")

'''
>>> dir(json)
['JSONDecodeError', 'JSONDecoder', 'JSONEncoder', '__all__', '__author__',
'__builtins__', '__cached__', '__doc__', '__file__', '__loader__',
'__name__', '__package__', '__path__', '__spec__', '__version__',
'_default_decoder', '_default_encoder', 'decoder', 'dump', 'dumps', 'encoder',
'load', 'loads', 'scanner']
>>>

'''

json_file = open('./files/The_Graduate.txt', "r", encoding="utf-8")
movie = json.load(json_file)
json_file.close()

print(movie['Title'], movie['Released'], "\n", movie['Plot'])
print(movie['won_oscar'], movie['budget'])

dump = (json.dumps(movie, ensure_ascii=False))
print(type(dump))

movie2 = {}
movie2["Title"] = "Minority Report"
movie2["Director"] = "Steven Spielberg"
movie2["Composer"] = "John Williams"
movie2["Actors"] = ["Tom Cruise", "Colin Farrel",
                    "Samantha Morten", "Max von Sydow"]
movie2["is_awesome"] = True
movie2["budget"] = "102000000"
movie2["Cinematigrapher"] = "Janus Kami\u0144ski"

file2 = open('./files/Minority_Report.txt', 'w', encoding="utf-8")
json.dump(movie2, file2, ensure_ascii=False, indent=2, sort_keys=False)
file2.close()
