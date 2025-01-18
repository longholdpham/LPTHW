from sys import argv #importing argv 

script, input_file = argv

#input_file = "ex20_test.txt" #hardcoding in our text file name as the input_file variable

def print_all(f): #defining the print_all function to print all the lines of text in the text file
	print(f.read())

def rewind(f): #defining the rewind function that uses seek()
	f.seek(0) #sets the reference point of the argument 'f' to the beginning, basically we'll read the file from the beginning

def print_a_line(line_count, f): #print one line from the file 'f'
	print(line_count, f.readline(), end= "")

current_file = open(input_file)

print(f"Now reading file {input_file}")

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file) #set the reference of our current_file back to the beginning

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line += 1 # current_line = 2
print_a_line(current_line, current_file)

current_line += 1 #current_line = 3
print_a_line(current_line, current_file)

#test
print_a_line(4, current_file)
rewind(current_file)
print_a_line(1, current_file)