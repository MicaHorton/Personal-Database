# Personal Database
Python files that allows you to store your thoughts safetly and search them.

- Flexible: The add tags options allows you to create lists on demand.
- Safe from Snoops: The code will encrypt your entries by generating a hash based off a string password. The hash is then used to encrypt your entries using Fernet encryption.
- Easy to Access: Copy and paste this into your .bashprofile to be able to easily access entries.
- Searchable: Uses the python whoosh library to efficiently organize your thoughts

# Installation Guide

```
mkdir('Code')
git clone https://github.com/MicaHorton/Personal-Database.git Code
cd('..')
mkdir('PDB')
```
This will create a file structure like this:
- PDB
  - Code
  - Files
  - database.json



The code is kept in a seperate folder from "Files" and "database.json" to make difficult to acidentally upload those to Github since those are used to store your thoughts. 



# Resources
https://stackoverflow.com/questions/2572099/pythons-safest-method-to-store-and-retrieve-passwords-from-a-database
https://stackoverflow.com/questions/489861/locking-a-file-in-python
