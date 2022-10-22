name = 'Mad Dawg'
age = 35 
height = 165 #cm
weight = 130 #lbs
eyes = 'Brown'
teeth = 'White'
hair = 'Black'
height_in = round(height * 0.393701) # study dril- do some math
weight_kg = round(weight * 0.453592) # study drill- do some math

print(f"Let's talk about {name}") 
print(f"He's {height} cm ({height_in} inches) tall.") #study drill
print(f"He's {weight} lbs ({weight_kg} kg) heavy.") #study drill
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee")

print(f""" Printing all variables
name = {name}
age = {age}
height = {height}
weight = {weight}
eyes = {eyes}
teeth = {teeth}
hair = {hair}
height in inches = {height_in}
weight in kg = {weight_kg}
""") # testing out printing with """. It worked :D