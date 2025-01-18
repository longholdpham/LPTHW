# Trying out ex15 from memory

from sys import argv

script, filename = argv

txt = open(filename)
print(f"You opened file {filename}")
print(f"Here's the content:\n")
print(txt.read())

txt.close()
