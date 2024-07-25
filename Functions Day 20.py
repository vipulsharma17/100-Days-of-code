# Function can be called as a block of code which can be performed whenever it is called   

a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))

def gmean(a,b):
    mean=(a*b)/(a+b)
    print("Geometric Mean is",mean)

def gnum(a,b):
    if(a>b):
        print("A is Greater")
    else:
        print("B is Greater")

gmean(a,b)
gnum(a,b)