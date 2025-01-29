import math
from encodings.rot_13 import rot13

#Part1
name = "chris"
age = 49
height = 5.11
favorite_color = "radish_red"

# Print one variable at a time
print(name)
print(age)
print(height)
print(favorite_color)

# Print with one print statement and commas
print(name, age, height, favorite_color)

# Print with Python formats or format specifiers
print(f"Hello: {name}, my age is {age}, my height is {height} feet, and my favorite color is {favorite_color}!")

# Print with format specifiers within a multi-line string
print(f"""Hello: {name},
my age is {age:d},
my height is {height:.2f} feet,
and my favorite color is {favorite_color}!""")

print(f"""
Name: {name}
Age: {age}
""")
#Part2
r = int(input("Enter a circle radius:"))
circle_area = math.pi * math.pow(r, 2)
print(f"Circle area with radius {r} is {circle_area:.1f}")

# Calculate the following:
#The sum of age and 5.
print(f"Sum of age and 5: {age + 5}")
#The difference between height and 4.
print(f"differnce between height and 4 is: {height - 4})")
#The product of age and height.
print(f"The product of age and height is: {age * height}")
print()

#part3

#The quotient of height and 2.
print(f"The quotient of height and 2 is: {height / 2}")

#The remainder of age divided by 3.
print(f"The remainder of age divided by 3 is: {age % 3}")
#age raised to the power of 2
print(f"age raised to the power of 2 is: {age ** 2}")

#Part 4
#Convert the temperature to Celsius using the formula: Celsius = (Fahrenheit - 32) * 5/9.
temp_farenheight = input(f"Enter a Temp in Fahrenheit: ")
celsius = (float(temp_farenheight) - 32) * 5/9
print(f"Temperature in Celsius: {celsius:.2f}\u00b0c")
