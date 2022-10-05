from sys import argv

script, filename = argv #unpacking argv

txt = open(filename) #open the file

print(f"Here's your file {filename}:")
print(" ")
print(txt.read()) #print the content in the txt file

print("Type the filename again:")
file_again = input("> ") #prompting > 
print(" ")
txt_again = open(file_again)#open the file again

print(txt_again.read())#print the content in the txt file again

txt.close()
txt_again.close()

# Study Drill 7 notes
#
# Once in python shell
# Define the variable first, such as "txt", then open the txt file,
# " txt = open('file_name.txt') ",
# then use the function read, " txt.read() "
#
# To print, " print(txt.read()) "
