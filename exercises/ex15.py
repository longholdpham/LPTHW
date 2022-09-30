from sys import argv

script, filename = argv

txt = open(filename) #open the file

print(f"Here's your file {filename}:")
print(" ")
print(txt.read()) #print the content in the txt file

#print("Type the filename again:")
#file_again = input("> ") #prompting > 
#print(" ")
#txt_again = open(file_again)#open the file again

#print(txt_again.read())#print the content in the txt file again
