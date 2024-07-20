# match case is a new feature in python 3.10 and its not very different from if else
# the logic is similar just the code is more easy to understand
x=int(input("Enter the number : "))
match x:
    case 0:
        print("x is zero")
    case 4:
        print("case is 4")
    case None:
        print("invalid")