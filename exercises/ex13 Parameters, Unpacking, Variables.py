from sys import argv
# read the WYSS section for how to run this
script, first_variable, second_variable, third_variable, randomparameter = argv
# "unpacking" argv variable
# rather than holding all the arguments, it gets assigned to  four 
# variables you can work with: script, first, second, and third.

print(f"You passed a random parameter call {randomparameter}.")
print("The script is called:", script)
print("Your first variable is:", first_variable)
print("Your second variable is:", second_variable)
print("Your third variable is:", third_variable)
fourth_variable = input("What is the fourth variable? ")
print("Your fourth variable is:", fourth_variable)


print(f"""\nThe script is called {script}
Your first variable is {first_variable}
Your second variable is {second_variable}
Your third variable is {third_variable}
Your fourth variable is {fourth_variable}
""")
# Testing printing + argv. worked
