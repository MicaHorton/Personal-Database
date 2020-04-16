import subprocess
import json
import datetime
import re
import time

timestamp = datetime.datetime.now()
timestamp = timestamp.strftime('%a %x %X').replace('/','.')

fileDirectory = '/Users/mica/Projects/PDB/Files/'
fileName = timestamp

command = 'nano ' + '\'' + fileDirectory + fileName + '\''
subprocess.run(command, shell=True)

print('Add tags?', end=' ')
tags = input()
tags = re.findall('[^,\s][^\,]*[^,\s]*', tags)

filePath = '/Users/mica/Projects/PDB/Files/' + fileName
newInstance = {
    'file': filePath,
    'timestamp': timestamp,
    'tags': tags
}

database = '/Users/mica/Projects/PDB/dataBase.json'
with open(database,'r') as f:
    data = json.load(f)
    data.append(newInstance)
with open(database, 'w') as f:
    json.dump(data, f, indent=2) 



