a=int(input("Enter the number: "))
print(f"Multiplication of {a} is: ")
try:
    for i in range(1,11):
        print(f"{int(a)}X{i}={int(a)*i}")
except:
        print("sORRY sOME ERROR OCCURED")

try:
    num=int(input("Enter a number: "))
    a=[6,3]
    print(a[num])

except ValueError:

    print("Error,Enter a number")

except IndexError:

    print("index error")

for num in range(3):
    try:
        num=int(input("Enter the PIN: "))
        break
    except ValueError:
        print("Invalid PIN")

else:
    print("Account is Blocked")
        
