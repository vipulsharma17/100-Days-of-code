# dictionaries are ordered collection of data items
# they can store multiple items in a single variable

dic={
    "Vipul":"Human Being",
    "Spoon":"Object"
}
print(dic["Vipul"])

# Dictonary items are key value pairs
# They are separated by commas and enclosed within curly brackets {}

empid={
    1232:"Rahul",
    4243:"Ketan",
    6334:"Vipul",
    3833:"Hari"
}
print(empid[6334]) 

#

info={'name':'vipul','age':25,'eligible':True}
# print(info)
# we can print the values of items in dic using their key,if we want to throw error then we can use this synatx
# print(info["name"])
# if we want to return none if wrong info is typed we can use this syntax
# print(info.get('name'))

# if we want to print only keys of dict we can use this synatx same for values

print(info.keys())
