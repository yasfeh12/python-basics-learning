# Importing all math functions
from math import *

# Defining character details
char_name = "obi"
char_age = 35
is_male = True

# Display ASCII art
print("   /!")
print("  / !")
print(" /  !")
print("/___!")

# Changing character name
char_name = "theo"

# Printing statements and using string functions
print("Bow wow! We’re getting it all right now!\nAre we getting it right now?")
phrase = "oooooooooo weeeeeeeeeeeeeeeeeee!"
print(phrase + " I am Mr. Meeeeeeeeeeseeks... *cough* " + char_name.upper())

# Checking if the uppercase version of char_name is uppercase
print(char_name.upper().isupper())

# String functions
print("Length of phrase:", len(phrase))
print("First character of phrase:", phrase[0])
print("Position of '!' in phrase:", phrase.index("!"))
print("Replacing 'weeeeeeeeeeeeeeeeeee' with 'my':", phrase.replace("weeeeeeeeeeeeeeeeeee", "my"))

# Working with numbers
age = 12.5
print("Age:", age)

# Calculating age in months
age_in_months = age * 12
print("Age in months:", age_in_months)

# Basic math operations
print("We can make more complex math like this:", 3 * (4 + 5))
print("Modulus (remainder of division):", 10 % 3)

# Converting numbers to strings
print("Hello, " + char_name + ", " + str(char_age))

# Using math functions
print("Absolute value:", abs(-5))
print("Power function (5^6):", pow(5, 6))
print("Maximum of 3 and 1200:", max(3, 1200))
print("Minimum of 3 and 1200:", min(3, 1200))
print("Rounding 4.3:", round(4.3))
print("Square root of 36:", sqrt(36))

# using user input
name=input("whats youre name son ? ")
print(name + " woooow really? ")
age=input("how old are you my child? ")
print(str(age)+ "! this cannot be true ! " + "the proficy is true ")
