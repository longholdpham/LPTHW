from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable (argument) is:", first)
print("Your second variable (argument is:", second)
print("Your second variable (argument) is:", third)
print(f"Here are all your arguments:\n{first}\n{second}\n{third}")

my_name = input("What is your name?")
print(f"Ok, so you name is {my_name}")
my_age = int(input("How old are you?"))
print(f"Ok, so you are {my_age} years old")
my_age_add_10 = my_age + 10
print(f"So if i add 10 to your age, you will be {my_age_add_10} years old") 