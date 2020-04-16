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

# Create File
# Add Tags
# Add Timestamp
# Option 1: Create JSON Database with link to file with tags and timestamp. Ahh, this also solves the encryption problem! Fantastic.
# Option 2: Include tags & timestamp in header of file (maybe create a new file type with metadata?)




'''
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

subprocess.run('nano')





file = '/Users/mica/Projects/PDB/data.json'
with open(file,'r') as f:
    data = json.load(f)
    data.append(newInstance)
with open(file, 'w') as f:
    json.dump(data, f, indent=2) 

import os
import shutil
import subprocess

output_file = join_file.replace('.txt','.mp4')
createMP4 = 'ffmpeg -f concat -safe 0 -i {join_file} -c copy {output_file}'.format(join_file=join_file, output_file=output_file)
subprocess.run(createMP4, shell=True)

os.remove(join_file)
shutil.rmtree(path)

'''
