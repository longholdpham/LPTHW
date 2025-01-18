from sys import argv
from os.path import exists

script, filename = argv

print(f"Opening up file {filename}. Hit RETURN to continue, CTRL-C to abort.")
input()
indata_from_open_file = open(filename).read()
print(f"Printing out content from {filename}:")
print(indata_from_open_file)