from sys import argv

script, filename = argv

target_file = open(filename, 'r')
print(f"Opened File: {filename}")
print("Would you like to read the file. If yes, hit RETURN")
input("> ")

print(target_file.read())
target_file.close()
print("Now I'm asking you for three new lines to write to the file (truncate and write)")
line1 = input("Line1: ")
line2 = input("Line2: ")
line3 = input("line3: ")

target_file = open(filename, 'w')
target_file.write(f"{line1}\n{line2}\n{line3}\n")
target_file.close()

print("All three lines are written in the file. If you want to print out the three lines, hit RETURN.")
input("? ")

target_file = open(filename, 'r')
print(target_file.read())