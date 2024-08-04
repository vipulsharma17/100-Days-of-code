# python doc string are strings used right after the definition of a function,method class or module
# they are used to document our code
# we can access these docstrings using the doc attribute
# if doc strings are written above the function name they are not docstrings anymore
# they can be only seen in output if they are written below function name and above the body of function

def square(z):
    '''This function gives the sqaure root of the number'''
    print(z**2)
square(5)
print(square.__doc__)

# PEP 8 and import this
# PEP-8, is a document that provides guidelines and best practices on how to write Python code
# if you write import this in terminal or run it in your vs code
# you will see Among well known Easter eggs, Python embeds a library for displaying its famous PEP 20, called Zen of Python
# which consists in 19 aphorisms giving guidelines to Python programmers.

import this
print(this)