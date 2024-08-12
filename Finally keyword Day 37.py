def func1():
    try:
        l=[2,4,2,5]
        i=int(input("Etner the index: "))
        print(l[i])
        return 1
    except IndexError:
        print("some error occured")

    # finally:
    #     print("i am going to get executed anyways haha")

    # def func1(a,b):
    #     c=a+b
    #     return c
    # output=func1(3,5)
    # print(output)