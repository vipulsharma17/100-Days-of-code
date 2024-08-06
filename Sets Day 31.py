# Sets are immutable
# they can store multiple items in single variable that too of different data type
# sets are enclosed within curly brackets
# sets do not contain duplicate values

s={2,4,2,6}
print(s)
print(type(s))

# items of sets once printed occur in random order hence
# they cannot be acessed using index number

team={'ronaldo','messi','ronaldo','torres'}
print(team)

# if we want to write a null set then we should write it as set() if we just write {} then its considered as dictonary 
colour=set()
print(colour)
print(type(colour))
