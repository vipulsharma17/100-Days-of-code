#Here \n is known as escape sequence as it helps us to print the string after the \n on a new line, Hence it is also called as new line escape sequence
print("Today is a good day\nand the weather is also good")

# if we want to comment out certain blocks of code we can use # before the line we want to comment out and do not want to execute
# we can also comment out multiple lines at once by selecting all the lines we want to comment out using cursor and pressing ctrl + forward slash

# print("Hello world")
# print("i hope everyone is doing fine")
# print("what a beautiful day to be alive")

# We can also comment out multiple lines by using triple single quotes at the start and end of the block 

'''
print("Hello world")
print("i hope everyone is doing fine")
print("what a beautiful day to be alive")
'''
# if we want certain word of the string to be in double quotes then we need to enclose the string in single quote 
print('Hey my name is "vipul" and i love to play football')

# Or we can use double quote escape sequence which is a backward slah at the start and end of the word
print("Hey my name is \" vipul \" and i love to play football")

# we can also print multiple values in single print statement which can be string data type and also int
# we can seperate each value by using seperator parameter ie: sep="anything you want to use to seperate the values" EG: sep="/"
print("Hello",7,17,28,sep="-")


# By using end parameter we can display whatever we want to and it would de displayed at the end of the statement
print("Hello",7,17,end=" okay",sep="-")


