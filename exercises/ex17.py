from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
in_file = open(from_file) #open the 1st file
indata = in_file.read() #'indata' now contains the opened file data
# the 'indata' variable is created to hold the data for copying



print(f"The input file is {len(indata)} bytes long")
#'len()' function output indata's size 
print(f"This is what the file content looks like:\n\n{indata}\n")
#printing the data from 'indata' variable

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w') #open up the 2nd file in "write mode" 
out_file.write(indata) #write the data from 'indata' to the 2nd file

print("Alright, all done.")

out_file.close()
in_file.close()

