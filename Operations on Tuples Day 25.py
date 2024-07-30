countries=("India","England","Spain","France","Portugal")
print(type(countries))
tempc=list(countries)
print(type(tempc))
tempc.append("Italy") # added an item to the list
print(tempc)
tempc.pop(2) # Deleted an item from the list
             # we used () for specifying index because
             #  Square brackets are used for accessing elements in a list by their index, not for specifying the index in the pop method.
print(tempc)
tempc[2]="croatia"
print(tempc)
tempc[3]="Brazil" # Changed an item from the list
print(tempc)
countries=tuple(tempc)
print(type(countries))