types_of_people = 100 # define variable types_of_people
x = f"There are {types_of_people} types of people" #define variable x 

binary = "binary" #defining variable binary
do_not = "don't" #defining variable do_not
y = f"Those who know {binary} and those who {do_not}." #defining variable y

print(x) #print variable x
print(y) #print variable y

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = True
joke_evaluation = "Isn't that joke so funny! {}" 

print(joke_evaluation.format(hilarious)) #print using .format()

w = "This is the left side of ..."
e = "a string with a right side"
 
print(w + e)

some_var_string = "zerebro going $5" 
wishful_optimism = "I hope that {}"

print(wishful_optimism.format(some_var_string))

x = f"{some_var_string} is wishful thinking"
print(x)