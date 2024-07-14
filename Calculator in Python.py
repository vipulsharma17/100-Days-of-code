num1=int(input("Please Enter first number: "))
num2=int(input("Please Enter Second number: "))
print("1 for Addition")
print("2 for Subtraction")
print("3 for Multiplication")
print("4 for Division")
usi=int(input("Please Select the Operation: "))
if(usi==1):
    print("Addition is: ",num1+num2)
elif(usi==2):
    print("Subtraction is: ",num1-num2)
elif(usi==3):
    print("Multiplication is: ",num1*num2)
else:
    print("Division is: ",num1/num2)