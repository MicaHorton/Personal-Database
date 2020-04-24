import subprocess
import json
import datetime
import re
import time
import os

# Get timestamp for file name & to put in database.json
timestamp = datetime.datetime.now()
timestamp = timestamp.strftime('%a %x %X').replace('/','.')
fileDirectory = '/Users/mica/Projects/PDB/Files/'
fileName = timestamp.replace(' ','-')

# Create the file
command = 'nano ' + '\'' + fileDirectory + fileName + '\''
subprocess.run(command, shell=True)

# Add tags
print('Add tags?', end=' ')
tags = input()
tags = re.findall('[^,\s][^\,]*[^,\s]*', tags)

# Add all of the info to database.json
fileDir = os.path.realpath(__file__).replace('Code/input.py','Files/')
filePath = '/Users/mica/Projects/PDB/Files/' + fileName
newInstance = {
    'file': filePath,
    'timestamp': timestamp,
    'tags': tags
}

database = os.path.realpath(__file__).replace('Code/input.py','database.json')
with open(database,'r') as f:
    data = json.load(f)
    data.append(newInstance)
with open(database, 'w') as f:
    json.dump(data, f, indent=2) 

# Encrypt the files
import encrypt

