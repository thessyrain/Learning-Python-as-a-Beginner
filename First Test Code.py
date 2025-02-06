#Variables and Data Types 

character_name = "Tommy"
character_age = "70"

print ("There once was a man named " +  character_name + ", ")
print ("He was 70 years old. ")
character_name = "Mike"

print ("He really liked the name " + character_name + ",")
print ("but didnt like being " +  character_age + ", " )

#Working with strings
phrase = "Thessyrain Academy"
print (phrase.lower() . islower())
print (len (phrase))
print (phrase [3])
print (phrase.removeprefix ("Thessyrain", ))

print("Thessyrain\n Academy")
print (phrase.index ("T"))
print(phrase.replace ("Thessyrain" , "Puffneyo"))

#Woring with Numbers 

print (3 * (6 + 5))

from math import *
my_num = -5 
print (abs(my_num))
print (pow (4, 2))
print (max (4, 6))
print (min  (4,6 ))
print (round  (3.7))
print (floor (3.535))
print (ceil(3.24))
print (sqrt (36))


#Getting Input From Users

name = input("Enter your name: ")
age = input("Enter your age: ")
print ("Hello "  +   name  + " !   You are " +   age)






