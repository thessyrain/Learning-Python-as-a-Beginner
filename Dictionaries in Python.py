#Dictionaries in Python

#What is a dictionary?
#A dictionary is a collection of key-value pairs, used to store information. Each key is connected to a value, and you can use a key to access the value associated with that key. A key’s value can be a number, a string, a list, or even another dictionary. In fact, you can use any object that you can create in Python as a value in a dictionary.
#In Python, a dictionary is wrapped in braces, {}, with a series of key-value pairs inside the braces, as shown in the earlier example:
#alien_0 = {'color': 'green', 'points': 5}


#Creating a dictionary

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"

}


#Accessing items in a dictionary

#print(monthConversions["Dec"])
#print(monthConversions.get means the same thing as the bracket notation above)
print(monthConversions.get("Dec"))