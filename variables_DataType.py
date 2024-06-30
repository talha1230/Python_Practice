# function for variables
def variables():
	# Variables
	name="Muhammad "
	Gender="Male "
	Age = 22
	Country=" Pakistan "
	print(name + Gender + str(Age) + Country)
variables()
# Function within a function
# Global and Local Variables
name="Muhammad" # Global Variable
def greating():
    x="Ali" # Local Variable
    print("Hello "+x)
greating()
print("Hello "+name)
print (type(name))
# Data Types
# tuple 
# Tuple is a collection which is ordered and unchangeable, allows duplicated members,FOr example, you can use a tuple to store a list of names but you can't change it.
def Data_tuple():
    x=("Banana", "Apple","Banana ", "Orange")
    print   (x)
    print (type(x))
Data_tuple()

#list 
# List is a collection which is ordered and changeable, allows duplicated members,For example, you can use a list to store a list of names.
def Data_list():
   y=["Banana", "Apple", "Orange"]
   print (y)
   print (type(y))
Data_list()
#dictionary
# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.For example, you can use a dictionary to store the number of times that each word appears in a piece of text.
def Data_Dict():
     x= {"name":"Muhammad", "LastName":"Talha","Age":20}
     index=x["name"]
     print(index)
     print(x)
     print(type(x))
Data_Dict()
#set
# Set is a collection which is unordered and unindexed. No duplicate members.
def Data_set():
    x={"Banana", "Apple", "Grapes"} 
    print(x)
    print(type(x))
Data_set()
#frozenset
# Frozenset is a collection which is unordered and unindexed. No duplicate members.
# The difference between a frozenset and a set is that a frozenset is immutable, meaning that it cannot be changed after it is created.but set can be changed
def Data_frozenSet():
    x=frozenset({"ALi", "Ahmed", "Talha"})
    print(x) 
    print(type(x))
Data_frozenSet()
#bool
# Boolean is a data type that can only take the values True or False. For example, you can use a boolean to store whether a statement is true or false.
def Data_bool():
    x=True
    print(x)
    print(type(x)) 
Data_bool()
#Numbers
def Data_numbers():
    x=1
    y=2.8
    z=1j
    print("Numbers:")
    print(type(x))
    print(type(y))
    print(type(z))  
Data_numbers()
#changing data type
def Data_change():
    x=1
    y=2.8
    z=1j
    a=float(x)
    b=int(y)
    c=complex(x)
    print("Changing Data Types:")
    print(a)
    print(b)
    print(c)
    print(type(a))
    print(type(b))
    print(type(c))  
Data_change()
#Random Number
import random
def Data_random():
    print("Random Number:")
    x = random.randrange(0, 100)
    if x % 2 == 0:
         print("Even")
    else:
         print("Odd")
    print(x)
Data_random()
#Casting
def Data_casting():
    print("Python Casting:")
    x=int(1)   # x will be 1
    y=int(2.8) # y will be 2
    z=int("3") # z will be 3
    a=str("s1") # a will be 's1'
    print(x)
    print(y)
    print(z)
    print(a)
    print(type(x))
    print(type(y))
    print(type(z))
    print(type(a))
Data_casting()
#Slicing Strings
def Data_slicing():
    print("Slicing Strings:")
    a= "Hello, World!"
    print(a[2:5])  #this will print "llo" because it will start from 2 and end at 5 and 5th index will not be included because it is exclusive
    print(a[:5])   #this will print "Hello" because it will start from 0 and end at 5 and 5th index will not be included because it is exclusive
    print(a[2:])   #this will print "llo, World!" because it will start from 2 and end at the end of the string
    print(a[-5:-2]) #this will print "orl" because it will start from -5 and end at -2 and -2nd index will not be included because it is exclusive
Data_slicing()
