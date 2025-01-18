formatter = "{} {} {} {}" #create a formatter variable that holds 4 {}, these will be used to pass 4 argument to the .format function

print(formatter.format(1, 2, 3, 4)) #passing 1, 2, 3, and 4 as arguments to the .format function
print(formatter.format("one", "two", "three", "four")) #passing one, two, three, and four as arguments 
print(formatter.format(True, False, False, True)) #passing True, False, False, and True as arguments
print(formatter.format(formatter, formatter, formatter, formatter)) #passing the formatter variable from line 1 as arguments
print(formatter.format("Zerebro", "Going", "To", "$5!")) #Pretty self-explainatory (im too lazy to type the explaination out)

#***