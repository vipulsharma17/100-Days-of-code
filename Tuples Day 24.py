# Tuples are immutable data type in python, Meaning it can't be changed
# we can say its a tuple data type if there are multiple values in round bracket seperated by a comma  

tuple=("vipul","cristiano")
print(tuple)
print(type(tuple))

# as tuples are immutable, their data cannot be changed
# if we try to add an element using index position it will give us error as "'tuple' object does not support item assignment"

b=(123,43,54)
b[1]=34
print(b)

# as tuple if immutable, if we try to extend another variable into it, it gives error as "'tuple' object has no attribute 'extened'"

a=(123,34,564)
b=(34,54,57)
a.extened(b)
print(a)