# List can store multiple items in same varibale
# List items are seperated by comma and stored within Sqaure brackets
# List is a Mutuable Data Type,Tuples are Immutable
# data with multiple data types can be written inside a list

a=[4,6,7,"vipul",4.5,True]
print(a)
print(type(a))
print(a[3])
print(len(a))

# When it comes to negative indexing position
# you can len(a)-(negative position) to find out the desired position

a=[4,6,7,"vipul",4.5,True]
print(a)
print(type(a))
print(a[-3])

# We can use a if condition to check wether an element is present in the list

a=[4,6,7,"vipul",4.5,True]
print(a)
if 7 in a:
    print("yes it is present")
else:
    print("no")

# we can check if any specefic letter is present in the specefic string in the list    
# same thing applies for string as well
if "i" in "vipul":
    print("yes,present")
else:
    print("no,not present")

# Jumping index
# by adding the 3rd element in the indexing it is considered as jumping
# if we add 2 then the 1 number is skipped one after another
    
a=[2,4,6,"vipul",True,5.76,4,7]
print(a)
print(a[3:8:2])

# List comprehension
name=["vip","ish","paul","lendon","cristiano"]
names4=[i for i in name if (len(i) < 4)]
print(names4)