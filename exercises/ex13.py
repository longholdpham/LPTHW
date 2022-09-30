from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv

print("The script is calledL", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

print(f"""The script is called {script}
Your first variable is {first}
Your second variable is {second}
Your third variable is {third}
""")