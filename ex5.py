name = 'Long Pham'
age = 26
height = 65 # in inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(F"He's {height} inches tall.")
print(f"He's {weight} pounds heavy")
print("Actually that's not too heavy")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

pound_to_kg = weight * .453592
round_kg = round(pound_to_kg)


# This line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}")
print(f"My weight in kg is {round_kg}") # this will print out my rounded weight in kg
