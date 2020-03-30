import json
import datetime
import re

thought = input()

timestamp = datetime.datetime.now()
timestamp = timestamp.strftime('%a %x %X')

print('Add tags?', end=' ')
tags = input()
tags = re.findall('[^,\s][^\,]*[^,\s]*', tags)

newInstance = {
    'thought': thought,
    'timestamp': timestamp,
    'tags': tags
}

file = '/Users/mica/Projects/PDB/data.json'
with open(file,'r') as f:
    data = json.load(f)
    data.append(newInstance)
with open(file, 'w') as f:
    json.dump(data, f, indent=2) 

