#Working with List in Python 

friends = ["Olajumoke", "Olaniyi", "Loveth", "Theresa" , " Tomisin",  " Bolu"]

print( friends)

##Accessing Elements in a list
#Locating my friends by their index

print (friends [2])

#this selects the index 1 and all the characters after it 
print (friends[1:])

#this selects the index 1 to 3, but doesnt grab index 3 in particular
print(friends [1:3])

#Changing a particular index / modifying values in an array
friends[4] = "Funsho"

print (friends[4])

#List Functions 

lucky_numbers = [4, 5, 6, 8, 9, 16, 23, 42]
friends = ["Olajumoke", "Olaniyi", "Loveth", "Theresa" , " Tomisin",  " Bolu"]
friends.extend (lucky_numbers)

#this functions adds to the end of  a list 
friends.append ("Yetunde")

#this function adds to a particular element in a list 

friends.insert(1, "Olabisi")

#this function removes a particular element in a list
friends.remove("Olajumoke")

#this function removes the last element in a list
friends.pop()

#this function clears all the elements in a list
#friends.clear()

#this function tells you the index of a particular element in a list
print (friends.index("Loveth"))

#this function tells you how many times a particular element appears in a list
print (friends.count("Loveth"))

#this function sorts the elements in a list in ascending order
#friends.sort() it couldnt sort because the list contains both strings and integers

#this function reverses the elements in a list
friends.reverse()

#this function copies the elements in a list
friends2 = friends.copy()

print (friends)

#print (friends2) I do not want to pint this because it will print the same thing as friends
