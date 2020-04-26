# Note: Has to be run from Code folder

# Decrypt files
import decrypt # removing the .py fixed the error, but I don't know why?

# Create/open index
import os.path
from whoosh.fields import Schema, TEXT, ID, KEYWORD
from whoosh import index

schema = Schema(content=TEXT, path=ID(stored=True), tags=KEYWORD(scorable=True))

#print(os.getcwd())
homeDir = os.path.realpath(__file__).replace('Code/search.py','')
if not os.path.exists('Index'):
    os.mkdir('Index')
    ix = index.create_in("Index", schema)
else:
    ix = index.open_dir("Index")


# Add new files to index
import json
database = os.path.realpath(__file__).replace('Code/search.py','database.json')
writer = ix.writer()

with open(database,'r') as f:
    data = json.load(f)
    for item in data:
        if item['indexed'] == False:
        
            with open(item['file']) as f:
                content = f.read()   

            keywords = ''
            for word in item['tags']:
                keywords = keywords + word + ' '

            writer.add_document(content=content, path=item['file'], tags=keywords)
            item['indexed'] = True

with open(database, 'w') as f:
    json.dump(data, f, indent=2)

writer.commit()

# Alow user to search
from whoosh.qparser import QueryParser
from whoosh.highlight import UppercaseFormatter

with ix.searcher() as searcher:
    print('Enter search phrase:', end=' ')
    querystring = input()

    parser = QueryParser('content', ix.schema)
    query = parser.parse(querystring)
    results = searcher.search(query)

    results.formatter = UppercaseFormatter()
    def prCyan(skk): print("\033[96m{}\033[00m" .format(skk))
 
    for hit in results:
        with open(hit['path']) as f:
            contents = f.read()
       
        fragment = hit.highlights('content', text=contents)
        print('\n' + fragment)
        prCyan(hit['path'])
        


        


