# Note: Has to be run from Code folder

import decrypt # removing the .py fixed the error, but I don't know why?
import os.path
import json

print('Enter the tag:', end=' ')
query = input()

database = os.path.realpath(__file__).replace('Code/sort.py','database.json')
with open(database,'r') as f:
    data = json.load(f)
    for item in data:
        if query in item['tags']:
            print(item['file'])
    


        


