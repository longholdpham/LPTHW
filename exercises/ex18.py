# this one is like your scripts with argv
def print_two(*args): #defining function print_two
    arg1, arg2 = args #unpacking args
    print(f"arg1: {arg1}, arg2: {arg2}")
    
# ok, that *arg is actually pointless, we can just do this
def print_two_again(arg1, arg2): #defining function print_two_again
    print(f"arg1: {arg1}, arg2: {arg2}")

# this one takes one argument
def print_one(arg1): #defining function print_one
    print(f"arg1: {arg1}")
    
# this one takes no argument
def print_none(): #defining function print_none
    print("I got nothin'.")

#running the functions
print_two("Long","Pham")
print_two_again("Long","Pham")
print_one("First!")
print_none()