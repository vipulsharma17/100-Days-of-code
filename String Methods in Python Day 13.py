# There are many methods of string which exists in python,few of them with their functions are listed below

a="vipul !!!!"
# Counts the length of the string
print(len(a))

# converts all the characters to upper case
print(a.upper())

# converts all the characters to lower case
print(a.lower())

# Removes all the words or special characters which you specify while writing the method from the right side vise versa for lstrip()
print(a.rstrip("!"))

# Replace method will replace the variable string with whatever we specify in the method
print(a.replace("Vipul","Cristiano"))

# Split function will create a list between words if there is a space in the string
print(a.split(" "))

# Capitalize is used to make first letter of the word capital
b="blog hEadiNg"
print(b.capitalize())

# center method is used to shift whole string to the center based on the number you specify
c="Welcome to my channel"
print(c)
print(c.center(30))

# Countmethod will count how many letters are there in the string,You have to specify the character in the method
d="Cristiano Ronaldo"
print(d.count("o"))

# endswith will return a boolean value (true/false) if the string ends with whatever you pass in the method 
e="what an amazing day to be alive !!!!"
print(e.endswith("!!!!"))

# Find method is used to find the word or letter you specify and returns the index position,
# if the letter/word does not exits it will return -1
f="Let's Go and Play Football"
print(f.find("and"))

# Index method works similar to find method but index method returns error if the word/letter is not found
f="Let's Go and Play Football"
print(f.index("z"))

# isalnum method returns boolean value, checks if A-Z,a-z,0-9 exits in the string,if there are any special charecter or space
# in the string it would return false
g="PleaseEnterthePassword"
print(g.isalnum())

# isalpha method returns boolean value, checks if A-Z,a-z exits in the string, if there are any numbers,special char or space
# in the string it would return false
h="pleaseenterpssword"
print(h.isalpha())

# Checks if all the letters are in lowercase
print(h.islower())

# as \n is not printable it would return false
i="Happy Diwali \nEveryone"
print(i.isprintable())

# if there is any white space in string it would return boolean value
j=" "
print(j.isspace())

# istitle checks wether first letter of the word is uppercase and retruns boolean value
k="turn Up The Music"
print(k.istitle())

# swapcase converts uppercase to lowercase and lowercase to uppercase
l="Lets go For a DrIve"
print(l.swapcase())

# title converts every letter of the world to capital
m="welcome to the world of python"
print(m.title())