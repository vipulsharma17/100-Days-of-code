# Methods in Dict
# as you know sets are not ordered but however Dict are ordered as of of python 3.7 version

emp={1232:45,3224:70,4324:60,5345:40}
emp2={2331:67,5436:50}

emp.update(emp2)
print(emp)

# Clear method
emp.clear()
print(emp)

# How to create empty Dict
emp3={}
print(emp3)

# pop method
emp.pop(3224)
print(emp)

# pop item
# it deleted last key value pair from dict

emp.popitem()
print(emp)

#del method
# this would delete the whole dictonary and would give error if we try to print
del emp2
print(emp2)
# we can also delete specefic key value pair by specifying the key
del emp2[5436]
print(emp2)