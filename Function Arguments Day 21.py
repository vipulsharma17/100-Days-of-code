#-----------------DEFAULT ARGUMENTS------------------------
# Here we have a simple way to create and call the function
# where a,b are required arguments   

def average (a,b):
    print("Average is: ",(a+b)/2)
average(4,8)

# Here in the function we have passed 'Default Arguments'
# so when we call the function it would accept the default argument and give the output

def average (a=5,b=5):
    print("Average is: ",(a+b)/2)
average()

# Even if we pass any default arguments when making the function
# it will give output for the arguments which we passed during calling the function 

def average (a=5,b=5):
    print("Average is: ",(a+b)/2)
average(10,8)

# If we give a single argument during calling the function
# It will take the second value from the deafult argument 

def average (a=5,b=5):
    print("Average is: ",(a+b)/2)
average(10)

#-------------------------KEYWORD ARGUMENTS-------------------

#  Here the order in which we pass the arguments doesn't matter
# unless we are providing arguments with kry values =

def average(a=9,b=6):
    print("Average is: ",(a+b)/2)
average(b=5,a=7)

#-------------------------VARIABLE LENGTH ARGUMENTS-------------------

def average(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    print("Average is: ",sum/len(numbers))
average(25,25)

#-------------------------RETURN STATEMENT----------------------------

# return statement is used to return the value of expression back to the callng function
def average(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    return sum/len(numbers)
    
c=average(15,15,10)
print(c)    
    
