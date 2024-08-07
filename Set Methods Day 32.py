# Sets are written in curly brackets

s1={1,2,5,6}
s2={3,6,7}

# Union() is used to print distinct items present in the both sets

print(s1.union(s2))

# update method adds items of s2 varibale in s1 distinctly 

s1.update(s2)
print(s1)

# example of union 
cities1={'pune','mumbai','nashik','solapur'}
cities2={'banglore','Delhi','pune','mumbai'}
cities3=cities1.union(cities2)
print(cities3)

# intersection helps us to print items which are similar in both the varibales

# cities1={'pune','mumbai','nashik','solapur'}
# cities2={'banglore','Delhi','pune','mumbai'}
# cities3=cities1.intersection(cities2)
# print(cities3)

# intersection_update
# this is used to update the first variable with similar values and store them

cities1={'pune','mumbai','nashik','solapur'}
cities2={'banglore','Delhi','pune','mumbai'}
cities1.intersection_update(cities2)
print(cities1)

# symmetric difference 
# this will print values which are not similar after comparing both the variable
cities1={'pune','mumbai','nashik','solapur'}
cities2={'banglore','Delhi','pune','mumbai'}
cities3=cities1.symmetric_difference(cities2)
print(cities3)

# difference 
# this will print values which are only present in the original set and not both the set
cities1={'pune','mumbai','nashik','solapur'}
cities2={'banglore','Delhi','pune','mumbai'}
cities3=cities1.difference(cities2)
print(cities3)

# isdisjoin sets
# it checks if given sets are present in another set,method retrun false if present
# returns true is items are not present
# cities1={'pune','mumbai','nashik','solapur'}
# cities2={'banglore','Delhi','pune','mumbai'}
# print(cities1.isdisjoint(cities2))

# issuperset
# it checks whether all items of a set are present in the original set
# it reurns true if all elements are present

cities1={'pune','mumbai','nashik','solapur'}
cities2={'banglore','Delhi','pune','mumbai'}
print(cities1.issuperset(cities2))
cities3={'Delhi','pune'}
print(cities2.issuperset(cities3))

# issubset
# its opposite of superset
# it checks wheter all itmes of original set are present in particular set
cities1={'pune','mumbai','nashik','solapur'}
cities2={'pune','mumbai'}
print(cities2.issubset(cities1))
cities3={'Delhi','pune'}
print(cities2.issubset(cities3))

# add
# it adds an element to the set
cities1={'pune','mumbai','nashik','solapur'}
cities1.add("hyderabad")
print(cities1)

# update
# it updates one set values into another set
cities1={'pune','mumbai','nashik','solapur'}
cities2={'hyderabad','panjim'}
cities1.update(cities2)
print(cities1)

# remove
# used to remove items from the set
cities1={'pune','mumbai','nashik','solapur'}
cities1.remove('solapur')
print(cities1)

# discard
# used to remove items from the set but doesn't throw error if item is not present
cities1={'pune','mumbai','nashik','solapur'}
cities1.discard('goa')
print(cities1)

# pop
# used to remove any random item from the set
# we can check which item is poped by storing it an variable and later printing the variable
cities1={'pune','mumbai','nashik','solapur'}
item=cities1.pop()
print(cities1)
print(item)

# del
# used to delete the entire set

cities1={'pune','mumbai','nashik','solapur'}
del cities1

# clear
# used to delete all items in set but not the set

cities1={'pune','mumbai','nashik','solapur'}
cities1.clear()
print(cities1)
