# when we don't want to execute a code after certain logic we can use break statement which would exit the loop/block and execute
# the further lines of code

for i in range(11):
    print("5 X",i,"=",5*i)
    if(i==5):
        break
print("itna hi aata hae meko")

# i=1
# candy=int(input("How Many candies do you want ? : "))
# while(i<=candy):
#     print("candy")
#     i=i+1

# if we dont want to execute a certain part of the logic and continue executing the things after that we use continue
# if we do not want to print values divisible by 2 but want to print other values we can use continue statemnt after num%2==0

for num in range (1,25+1):
    if(num%2==0 and num%5==0):
        continue
    print(num)

# Here using the continnue statement python will skip multiplication of number for 5, as mentioned in the if condition and will
# multiply other number as we used continue
num=int(input("Enter the number : "))
for i in range(1,11):
    if(i==5):
        continue
    print(f"{num} X {i} = {num*i}")
    
# there is no do while loop in python as it is C
# do while executes a peice of code until the condition is true/false and if condition is not satisfied, it will exit the loop
# but we can use do while loop with specifying While and a boolean value
while True:
    num=int(input("Enter a Positive Number : "))
    print(num)
    if(num<0):
        break
            