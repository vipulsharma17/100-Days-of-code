# if else Program

a=int(input("Please Enter You age : "))
if(a>=18):
    print("You are eligible for Driving")
else:
    print("Sorry,You are Underage")
    
# if else Program

budget=200
appleprice=250
if(appleprice>budget):
    print("You do not have enoguh money")
else:
    print("added to Cart")

# if else elif Program
    
num=int(input("Enter the Number : "))
if(num>0):
    print("The number is positive")
elif(num==0):
    print("Number is Zero")
else:
    print("Number is Negative")

# if else elif program without using nested if else
    
num=int(input("Enter a number : "))
if(num<0):
    print("Number is Negative")
elif(num!=0 and num<=10):
    print("Number is Between 1 to 10")
elif(num>10 and num<=20):
    print("Number is Between 10 to 20")
elif(num>=21):
    print("Number is Greater than 20")
else:
    print("Number is zero")

# if else program using nested if else
num=int(input("Enter a number : "))
if(num<0):
    print("number is negative")
elif(num>0):
    if (num<=10):
        print("number is between 1 to 10")
    elif(num>10 and num<=20):
        print("number is between 10 to 20")
    else:
        print("number is greater than 20")
else:
    print("numer is zero")