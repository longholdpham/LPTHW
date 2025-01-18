# Reading Files

from sys import argv

script, filename = argv #get the file name

txt = open(filename) #open the ex15_sample.txt file, txt file's name is specifically passed as the script's argument
# the argument is passed to the open() function, the 'txt' variable stored the content opened by the open() function
print(f"Here's your file {filename}: ") #print out the script name
print(txt.read()) #print out the content of our opened file txt

txt.close()

print("Type the filename again:") #prompting to input the text file name again.
file_again = input("> ") #store the name of the file, which is input by the user, to the variable file_again

txt_again = open(file_again) #another variable, txt_again, is used to open the actual text file

print(txt_again.read()) #print out the content of the text file
txt_again.close()