from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w') # passing 'w' parameter to open the file
# for writing, this would truncate the file first
# Check documentation for more parameter details

print("Truncating the file. Goodbye!")
target.truncate() # This line isnt neccessary since the open function
# above is in 'w' mode, would truncate the file first before writing

print("Now I'm going to ask you for three lines.")

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print("I'm going to write these to the file. ")

someString = f"{line1}\n{line2}\n{line3}" #study drill
# combining line1, line2, and line3 into one string instead of having
# to multiple target.write lines, see below commented block of code

target.write(someString)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

print("And finally, we close it.")
target.close()
