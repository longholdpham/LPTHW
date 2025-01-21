from sys import argv
from os.path import exists

script, filename = argv

print(f"Opening up file {filename}. Hit RETURN to print the file's content, CTRL-C to abort.")
input()
indata= open(filename).read()
print(f"Printing out content from {filename}:")
print(indata_from_open_file)
new_file = "new_test.txt"

print(f"Does output file (new_test.txt) exist? {exists(new_file)}")
write_file = open(new_file, 'w')
write_file.write()