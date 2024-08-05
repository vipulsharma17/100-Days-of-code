#Recursion in Python is a programming technique where a function calls itself to solve smaller instances of the same problem.
#factoial of number

num=int(input("Enter the number: "))
def factorial (num):
    if (num==0 or num==1):
        return 1
    else:
        return num*factorial(num-1)

print(factorial(num))

#fibonacci sequence

num=int(input("Enter the Number: "))
def fibonacci(num):
    if(num==0):
        return 0
    elif(num==1):
        return 1
    else:
        return fibonacci(num-1)+fibonacci(num-2)
print(fibonacci(num))

# this will print itslef infinite times
def hi ():
    print("HELLO")
    hi()
        