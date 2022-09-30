from sys import argv
# read the WYSS section for how to run this
script, first_variable, second_variable, third_variable = argv

#When running on the command prompt, the code will look like this when
# typed in: python ex13.py first second third
#                  script  first_variable second_variable third_variable

print("The script is called:", script)
print("Your first variable is:", first_variable)
print("Your second variable is:", second_variable)
print("Your third variable is:", third_variable)

print(f"""\nThe script is called {script}
Your first variable is {first}
Your second variable is {second}
Your third variable is {third}
""")
# Testing printing + argv. worked
