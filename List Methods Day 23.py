# By using Append we can add any value at the end of the list

a=[2,4,5,6]
print(a)
a.append ("vipul")
print(a)

# using sort() we can arrange the numeric values in ascending order

a=[24,54,5,6,6]
a.sort()
print(a)

# using sort(reverse=true) we can arrange the numeric values in descending order

a=[24,54,5,6]
a.sort(reverse=True)
print(a)

# using reverse() we can print the list in reverse form 

a=[24,54,5,6]
a.reverse()
print(a)

# using index() we can speceify the value of which we want to find the index position of
# if there are two similar values then it will return the index position of value which is first in the list

c=[24,54,5,6]
print(c.index(5))


# Count method is use to count the how many specified values are present in the list 

c=[24,54,5,6,5,5]
print(c.count(5)) 

# Copy() is used to copy the list as is by defining the previous variable 

d=c.copy()
print(d)

# if we want to insert an element in the list we can do it by specifying the index position first and then the value we want to insert

e=[24,54,5,6,5,5]
e.insert(1,233)
print(e)

# if there are two lists and we want to add the values of second list to the first list then we can do that using extend ()

a=[12,34,76]
b=[43,54,76]
a.extend(b)
print(a)

# if there are two lists and we want to create a third list with details of 1st and 2nd list its possible using concatination

x=[32,453,54]
y=[34,54,34]
z=x+y
print(z)