#Working with Functions in Python

#What is a function?
#A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.

#Creating a function
#indentation is very important in python, it is used to define a block of code.
#def is a keyword used to define a function

def say_hello():
    print("Hello World")

#Calling a function, this is how you call a function in python 
say_hello()

#What is a parameter?
#A parameter is a value that is passed to a function. It is a value that is used to define a function.

#Creating a function with a parameter
def say_hello (name, age):
    print ("Hello" + name,  "you are " + age )
    
say_hello(" Olajumoke" , " 29 ")
say_hello(" Olaniyi" , " 38 ")


# Return Statement
#A return statement is used to end the execution of the function call and "returns" the result (value of the expression following the return keyword) to the caller. 
# The statements after the return statements are not executed. If the return statement is without any expression, then the special value None is returned.

#Creating a function with a return statement

def cube(num):
    return num*num*num

print (cube (3))

#this function returns the cube of a number
#result = cube(4)
#print (result)