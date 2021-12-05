# Variables

applesSold = 10

a = 5
b = a
a = 7
print(a)
print(b) 


# you cannot use a variable name until its been assigned a value
# print(x)
# x = 12
# put the print after the variable and it will run
x = 12
print(x)

a = 5
print(a)
print(type(a)) 
# output - 5 / <class 'int'> integer

a = 5.0
print(a)
print(type(a))
# output - 5.0 / <class 'float'>

a = True
print(a)
print(type(a))
# output - True / <class 'bool'> boolean

a = "True"
print(a)
print(type(a))
# output - True / <class 'str'> string

# Input & Output

print('Hello World')

print('Mary Shelley wrote "Frankenstein" in 1818') # Single quotation marks allow you to use a double quotation in the middle

print("Mary Shelley wrote \"Frankenstein\" in 1818")

applesSold = 10
applePrice = 0.20

print("We sold",applesSold," apples at $",applePrice,"each for a total of $",(applesSold * applePrice))

print("We sold",applesSold,"apples at $",applePrice,"each for a total of $",(applesSold * applePrice), sep="") #sep = separater of spaces

#-----------------------------------------------------------------------------------------------------------------------------------------------------

applesSold = 5000
applePrice = 0.20
# to get the decimals showing 
print("We sold ",applesSold," apples at $",
format(applePrice,',.2f'),\
" each for a total of $",\
format((applesSold * applePrice),',.2f'),\
sep="")

#-----------------------------------------------------------------------------------------------------------------------------------------------------

applesSold = int(input("How many apples did you sell this week? "))
applePrice = float(input("What the price of each apple sold? "))
print("You sold ",applesSold," apples at $",applePrice," each for a total of $",(applesSold * applePrice), sep="")

# Operators

# Python offers the following math operator.

# Symbol		Operation			Description
# ----------------------------------------------
# + 			Addition 			Adds two numbers
# _ 			Subtraction 		Subtracts one number from another
# * 			Multiplication 		Multiplies one number by another
# / 			Division 			Divides one number by another and gives the result as a
# 								floating-point number
# // 			Integer division 	Divides one number by another and gives the result as
# 								an integer
# % 			Remainder 			Divides one number by another and gives the remainder
# ** 			Exponent 			Raises a number to a power

# Addition
print(10 + 5) # Output 15
# Subtraction
print(11 - 5) # Output 6
# Multiplication
print(4 * 3) # Output 12
# Division
print(6 / 2) # Output 3.0 (Float)
# Integer Division
print(15 // 6) # Output 2
# Remainder
print(15 % 6) # Output 3
#Exponent
print(2 ** 3) # Output 8

applesSold = 50
applePrice = 0.20
print(applesSold * applePrice)

# combining all strings into a single string
x = "Hello"
y = "World"
z = x + " " + y

print(z)

#--------------------------------------------------------------------------------------------------------------------------------------------------

# If/Else

# Operator Meaning
# > Greater than
# < Less than
# >= Greater than or equal to
# <= Less than or equal to
# == Equal to
# != Not equal to

def buy2Get1Free(qnty):
	if qnty >= 6:
		print("You qualify for multiple Buy 2 Get 1 Free Discounts")
	elif (qnty >= 3) and (qnty < 6):
		print("You get one Apple for Free!")
	else:
		print("You do not quality for the discount") 

applesSold = 3

buy2Get1Free(applesSold)

#-----------------------------------------------------------------------------------------------------------------------------------------------------

# For Loops

# for <variable> in [sequence of data]: // general for loop code

def countDown():

	for currentCount in [5, 4, 3, 2, 1]:
		print(currentCount)
			
	print("BLAST OFF!")
	

countDown()

# ---

def welcomeGuests(guestNames):

	for guest in guestNames:
		print("Welcome",guest)
		

guests = []
guests.append(input("Please enter the name of a guest: "))
guests.append(input("Please enter the name of a guest: "))
guests.append(input("Please enter the name of a guest: "))

welcomeGuests(guests)


# range(start, stop[, step])

# start
# The value of the start parameter (or 0 if the parameter was not supplied)

# stop
# The value of the stop parameter

# step
# The value of the step parameter (or 1 if the parameter was not supplied)

# will count to 9
def count(stop):
	for number in range(stop):
		print(number)
		
stoppingNum = int(input("Count to? "))
count(stoppingNum)

# will count to 10
def count(stop):
	for number in range(1, stop+1, 1):  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
		print(number)

#---------------------------------------------------------------------------------------------------------------------------------------------

stoppingNum = int(input("Count to? "))
count(stoppingNum)

def countDown(start):

	for currentCount in range(start,0,-1):
		print(currentCount)
			
	print("BLAST OFF!")
	

startingNum = int(input("Enter the countdown starting number: "))
countDown(startingNum)

#--------------------------------------------------------------------------------------------------------------------------------------------

# While Loops (Conditon/Control Loops)
# Condition - True/False condition to control the number of times it repeats
# Control - Repeats a specific number of times

def countDown(start):

	while start > 0:
		print(start)
		start -= 1
			
	print("BLAST OFF!")
	

startingNum = int(input("Enter the countdown starting number: "))
countDown(startingNum)

#---------------------------------------------------------------------------------------------------------------------------------------------

def countDown(start):
	continueLoop = True
	while continueLoop:
		print(start)
		start -= 1
		if (start == 0):
			print("BLAST OFF!")
			continueLoop = False	
	

startingNum = int(input("Enter the countdown starting number: "))
countDown(startingNum)

#-----------------------------------------------------------------------------------------------------------------------------------------------

def countDown(start):
	while True:
		print(start)
		start -= 1
		if (start == 0):
			print("BLAST OFF!")
			break	
	

startingNum = int(input("Enter the countdown starting number: "))
countDown(startingNum)

#-----------------------------------------------------------------------------------------------------------------------------------------------

# Functions

# A function is a block of code that exist within a program designed to perform a specifc task.

# When defining the name of a function, you must follow the same naming rules as those for variables.

# There are rules when naming functions / variables and include:
# • You cannot use one of Python’s key words as a functions / variable name. 
# • A functions / variable name cannot contain spaces.
# • The first character must be one of the letters a through z, A through Z, or an underscore character (_).
# • After the first character you may use the letters a through z or A through Z, the digits 0 through 9, or underscores.
# • Uppercase and lowercase characters are distinct. 

def classMessage():
	print("AFS-210", end=" : ")
	print("Data Structures and Algorithms")

print("Welcome to:")
classMessage()
print("I hope you enjoy your next eight weeks of class.")

#--------------------------------------------------------------------------------------------------------------------------------------------------

applesSold = 10
applePrice = 0.20

def showAppleTax():
	taxRate = 0.06
	appleTax = (applesSold * applePrice) * taxRate
	print("The tax on the sale of",applesSold,"apples is",appleTax)
	
showAppleTax()

#-------------------------------------------------------------------------------------------------------------------------------------------------

applesSold = 10
applePrice = 0.20

def showAppleTax():
	taxRate = 0.06
	applesSold = 50
	appleTax = (applesSold * applePrice) * taxRate
	print("The tax on the sale of",applesSold,"apples is",appleTax)
	
showAppleTax()	

print(applesSold)

#-------------------------------------------------------------------------------------------------------------------------------------------------

def showSum(a,b):
	print(a+b)
	
x = 1
y = 3
showSum(x,y)


def sum(a,b):
	return a+b
	
y = sum(1,2)
print(y)


def add_subtract(a,b):
	return a+b,a-b
	
sum, sub = add_subtract(1,2)
print(sum)
print(sub)	

#----------------------------------------------------------------------------------------------------------------------------------------------------

# Classes & Methods

# The simplest form of class definition looks like this:
# class ClassName:
#     <statement-1>
#     .
#     .
#     .
#     <statement-N>


class dog:

	def __init__(self, name, breed, age, color, size):
		self.name = name
		self.breed = breed
		self.age = age
		self.color = color
		self.size = size
		
	def bark(self):
		print("Woof..Woof")
		
	def getName(self):
		return self.name
		
	def setName(self, name):
		self.name = name
		
	def getAge(self):
		return self.age
		
	def setAge(self,age):
		self.age = age

dog1 = dog("Max","German Shepherd",2,"brown","large")
dog2 = dog("Cooper","Labrador",4,"black","large")
dog3 = dog("Bella","Chihuahua",1,"tan","small")

print(dog1.getName())
print(dog1.bark())
print(dog1.setAge(3))
print(dog1.getAge())

#----------------------------------------------------------------------------------------------------------------------------------

# Lists

# List items are ordered, changeable, and allow duplicate values.

# List items are indexed with the first item having an index of [0], the second item has an index of [1] etc.

# The list is mutable (ie: changeable), meaning that we can change, add, and remove items in a list after it has been created.

# A list may contain multiple different DataTypes include integers, strings, floats, booleans, lists and objects

# Lists are created by placing a sequence of values inside square brackets []

progLang = ["python", "c#", "javascript", "java", "c++"]
moreLang = ["rust", "php", "perl", "ruby", "go"]
myNumbers = [1,2,3,4,5]
myFloats = [1.0, 2.1, 3.2, 4.3]
myMixed = ["Hello", True, 6, ["item1", "item2", "item3"], 3.14]

print(progLang)

#add to list
progLang.append("c")
print(progLang)

progLang.extend(moreLang)
print(progLang)

# insert in a particular spot
progLang.insert(1, "pascal")
print(progLang)

# remove from a list
progLang.remove("pascal")
print(progLang)

#if there is no value it will remove the last item from the list (remove a random item)
progLang.pop()
print(progLang)

progLang.pop(6) # Removes "rust" from the list
print(progLang)

# figure out where something is at in the list

print(progLang.index("php"))

# how many items are on the list
print(len(progLang))

# how many times a word appears in the list
print(progLang.count("php"))

# sort a list 
progLang.sort()
print(progLang)

# in reverse order
progLang.sort(reverse=True)
print(progLang)

# print 3rd item on the list
print(myMixed[3])
# get 2 item in sub-list
print(myMixed[3][2])

#----------------------------------------------------------------------------------------------------------------------------------------------------

# Tuples

# Tuple items are ordered, unchangeable, and allow duplicate values.

# Tuple items are indexed with the first item having an index of [0], the second item has an index of [1] etc.

# The Tuple is unmutable (ie: unchangeable), meaning that we can not change, add, and remove items in a tuple after it has been created.

# A Tuple may contain multiple different DataTypes include integers, strings, floats, booleans, lists and objects

# Tuples are created by placing a sequence of values separated by a comma inside round brackets ()


progLang = ("python", "c#", "javascript", "java", "c++")

myNumbers = (1,2,3,4,5)
myFloats = (1.0, 2.1, 3.2, 4.3)

myMixed = ("Hello", True, 6, ["item1","item2","item3"], 3.14)

# how many times python shows up inside a Tuple
print(progLang.count("python"))

# Find position in the tuple of a particular value
print(progLang.index("javascript"))

# Length of how many items in tuple
print(len(progLang))

# cannot change a value of a tuple but can change values of mutuable objects that are stored within a tuple
print(myMixed)
myMixed[3][0] = "A" # changes "item1" to "A"
print(myMixed)

#------------------------------------------------------------------------------------------------------------------------------------------------------------

# Sets

# In a Set, items are unordered, unindexed and do not allow duplicate values.

# Unordered means that the items in a set do not have a defined order.

# This means that items in a Set can appear in a different order every time you use them, and cannot be referenced by an index or key.

# Sets cannot have two items with the same value.

# A Set is created by placing a sequence of values separted by a comma inside curly brackets {}

progLang = {"python", "c#", "javascript", "java", "c++"}
moreLang = {"rust", "php", "perl", "ruby", "go", "java", "python"}

myNumbers = {1,2,3,4,5}

myFloats = {1.0, 2.1, 3.2, 4.3}

# add a language
progLang.add("c")
print(progLang)

# remove items
removedItem = progLang.pop()
print(progLang)
print(removedItem)

# specify specific item to remove
progLang.discard("c#")
print(progLang)

progLang.remove("c")
print(progLang)

# return a set of the difference in items
print(progLang.difference(moreLang))
print(moreLang.difference(progLang))

# where do the sets intersect (the same between the two sets)
print(progLang.intersection(moreLang))

#-------------------------------------------------------------------------------------------------------------------------------------------------------

# Dictionaries

# Dictionaries are used to store data in key:value pairs where the keys must be unique.

# A dictionary is a collection which is ordered, as of Python version 3.7, changeable (mutable) and does not allow duplicate key values.

# Storing a value using a key that is already in use, results in the old value being replaced with the new value.

# A Dictionary is created by placing a sequence of keys:values pairs, separted by a comma, inside curly brackets {}

# If you are familiar with Javascript, the notation of key:value pairs should be familiar to you as they are similar to JSON data format.

worldCapitals = {
	"Afghanistan" : "Kabul",
	"Bangladesh" : "Dhaka",
	"Canada" : "Ottawa",
	"Cuba" : "Havana",
	"France" : "Paris",
	"Germany" : "Berlin",
	"Philippines" : "Manila",
	"United Kingdom" : "London",
	"United States" : "Washington D.C."
}

# Capital city of France
print(worldCapitals.get("France"))

# list of all keys
print(worldCapitals.values())

# list of all keys
print(worldCapitals.keys())

# cleaner list of all keys
for country, capital in worldCapitals.items():
	print(country + " = " + capital)

# remove an item
worldCapitals.pop("Germany")
print(worldCapitals)

# change/update a value
worldCapitals.update({"United States" : "New York"})
print(worldCapitals)

# add items (if it does not exist it will add to the end of the list)
worldCapitals.update({"Japan" : "Tokyo"})
print(worldCapitals)

# set-default (combo of get method and update method) returns the value of a specified key
print(worldCapitals).setdeault("Canada")
print(worldCapitals.get("Canada")) # returns the same value

print(worldCapitals.setdefault("Switzerland","Berlin")) # doesnt exist in the list and will add to the list
print(worldCapitals)




