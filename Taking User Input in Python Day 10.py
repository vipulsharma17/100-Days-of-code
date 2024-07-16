#when we are taking input from the user python takes it as string data type
a=input("What is your name ?")
print("My name is",a)   

# as we discussed that pthon takes the input in form of string data type, so to convert it into int data type we use typecasting
a=input("Enter first number : ")
b=input("enter second number : ")
print (int(a)+int(b))

# Following is a simple calculator which performs diff arathematic function after taking input from the user
a=input("Enter first number : ")
b=input("Enter second number : ")
print("Addition is : ",(int(a)+int(b)))
print("Subtraction is : ",(int(a)-int(b)))
print("Multiplication is : ",(int(a)*int(b)))
print("Division is : ",(float(a)/float(b)))
print("Floor Division is : ",(int(a)//int(b)))
print("Modulus is : ",(int(a)%int(b)))
print("Exponential is : ",(int(a)**int(b)))