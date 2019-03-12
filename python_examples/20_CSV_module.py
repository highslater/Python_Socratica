#!/usr/bin/env python3.7

"""20_CSV_module.py.

Twentieth Program of the Socratica Sexy-Hologram-Human/Computer-Hybrid
Python Series.

"""
import logging
import csv
from datetime import datetime


LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename="LOG_files/LOG_20.Log",
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode='w')
logger = logging.getLogger()
logger.info("#20_CSV_module.py RUN / START")

PATH = "stock_data.csv"

print()
print(dir(csv))
print()
print(" CSV")

file = open(PATH, newline='')
reader = csv.reader(file)
header = next(reader)
data = []

for row in reader:
    date = datetime.strptime(row[0], '%m/%d/%Y')
    open_price = float(row[1])
    high = float(row[2])
    low = float(row[3])
    close = float(row[4])
    volume = int(row[5])
    adj_close = float(row[6])

    data.append([date, open_price, high, low, close, volume, adj_close])

print("", '*' * 90, "\n")
print("", header)
print("", data[0])
print('\n', '*' * 90)

RETURNS_PATH = "google_returns.csv"
file = open(RETURNS_PATH, 'w')
writer = csv.writer(file)
writer.writerow(["Date", "Return"])

for i in range(len(data) - 1):
    todays_row = data[i]
    yesterdays_row = data[i + 1]
    todays_date = todays_row[0]
    formatted_date = todays_date.strftime('%m/%d/%Y')
    todays_price = todays_row[-1]
    yesterdays_price = yesterdays_row[-1]
    daily_return = (todays_price - yesterdays_price) / yesterdays_price

    writer.writerow([formatted_date, (daily_return)])
