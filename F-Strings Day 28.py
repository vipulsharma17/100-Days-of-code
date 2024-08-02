# This is the traditonal way of string formatting in python
# but its a little complicated to understand 
letter=("hey my name is {1} and i am from {0} ")
country="india"
name=("vipul")
print(letter.format(country,name))

# F-String helps us to decalre the variable name in the string itself
# so it becomes easier for us to write the code makng it less complex

print(f"Hey my name is{name} and i am from {country}")