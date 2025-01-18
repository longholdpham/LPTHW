# this one is like your script with argv
def print_two(*args):
	arg1, arg2, arg3, arg4 = args
	print(f"arg1: {arg1}, arg2: {arg2}, arg3: {arg3}, arg4: {arg4}")

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
	print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument
def print_one(arg1):
	print(f"arg1: {arg1}")

# this one takes no argument
def print_none():
	print("I got nothing'.")

in_arg1 = input("Type in your arg1: ")
in_arg2 = input("Type in your arg2: ")
in_arg3 = input("Type in your arg3: ")
in_arg4 = input("Type in your arg4: ")

print_two(in_arg1, in_arg2, in_arg3, in_arg4)
print_two_again(in_arg1, in_arg2)
print_one("First!")
print_none()