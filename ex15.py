from sys import argv

script, filename = argv

txt = open(filename) #open the txt file, txt file's name is specifically passed as the script's argument
# the argument is passed to the open() function, the 'txt' variable stored the content opened by the open() function
print(f"Here's your file {filename}: ")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again =open(file_again)
print(txt_again.read())