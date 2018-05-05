'''
This script allows you to find the max number of simultanious calls.

Data for calculation should be in CSV file in the following format:

"1433713154","1433713180"
"1433763429","1433763439"

Where:
- each row is a call
- first column is a unixtime when the call was connected
- second column is a unixtime when the call was disconnected

How to run:
$ python max_simul_calls.py data.csv
'''

import sys
import csv
import operator
import datetime

ifile = open(sys.argv[1], "rb")
reader = csv.reader(ifile)

sortedlist = sorted(reader, key=lambda x: int(x[0]))

maximum = 1
current_calls = []
current_number = 1
index = 0

for row in sortedlist:
  if index == 0:
    current_calls.append(row)
  else:
    current_index = 0
    for call in current_calls:
      if call[1] < row[0]:
        current_calls.pop(current_index)
        current_number -= 1
      current_index += 1
    current_calls.append(row)
    current_number += 1
  if current_number > maximum:
    maximum = current_number
  index += 1
  print '%s: %s %s = %s' % (index, datetime.datetime.utcfromtimestamp(float(row[0])),datetime.datetime.utcfromtimestamp(float(row[1])),current_number)

print 'max: %s' % maximum  
ifile.close()
