#Here both the numbers "7" and "12" are defined as string as they are quoted in comma, using typecasting we can change 
#the data type of the variable data which is defined, Here string is converted to int

a="7"
b= "12"
print(int(a)+int(b))

#Here the variable string is defined as string data type but is a number,so when 3rd variable string_number is defined
#by using Explicit typecasting we can change the data type to integer, Typecasting where we ourself change the data type
#according to our will is known as Explicit typecasting 

string="7"
number=15
string_number=int(string)
sum=number+string_number
print("Sum of both the numbers is",sum)

# Here we take two numbers 5 and 5.5 and perform addition,Number 5 is int data type and 5.5 is float, 
#Python interpreter Automatically changes the number 5 data type from int to float
#this Automatic conversion of data type is known as implicit conversion
#Conversion depends upon the level of the datatype it is automatically converted to higher data type

a=5
b=5.5
sum=a+b
print(sum)
print(type(sum))
