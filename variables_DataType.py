# Function to demonstrate the use of variables
def variables():
    # Variables
    name = "Muhammad "  # String variable
    Gender = "Male "  # String variable
    Age = 22  # Integer variable
    Country = " Pakistan "  # String variable
    
    # Concatenating strings and converting integer to string
    print(name + Gender + str(Age) + Country)

# Calling the function to demonstrate variable usage
variables()

# Global and Local Variables
name = "Muhammad"  # Global Variable

def greeting():
    x = "Ali"  # Local Variable
    # Local variable 'x' is used only within this function
    print("Hello " + x)

# Calling the function to demonstrate local variable usage
greeting()

# Accessing the global variable
# Global variables can be accessed anywhere in the code
print("Hello " + name)

# Printing the type of the variable 'name'
# Demonstrating the use of type() function to check variable type
print(type(name))

# Data Types

# Tuple
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# For example, you can use a tuple to store a list of names but you can't change it.
def Data_tuple():
    x = ("Banana", "Apple", "Banana", "Orange")  # Defining a tuple
    print(x)  # Printing the tuple
    print(type(x))  # Printing the type of x, which is tuple

# Calling the function to demonstrate tuple usage
Data_tuple()

# List
# List is a collection which is ordered and changeable. Allows duplicate members.
# For example, you can use a list to store a list of names.
def Data_list():
    y = ["Banana", "Apple", "Orange"]  # Defining a list
    print(y)  # Printing the list
    print(type(y))  # Printing the type of y, which is list

# Calling the function to demonstrate list usage
Data_list()

# Dictionary
# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# For example, you can use a dictionary to store the number of times that each word appears in a piece of text.
def Data_Dict():
    x = {"name": "Muhammad", "LastName": "Talha", "Age": 20}  # Defining a dictionary
    index = x["name"]  # Accessing an item by key
    print(index)  # Printing the value of the key "name"
    print(x)  # Printing the dictionary
    print(type(x))  # Printing the type of x, which is dictionary

# Calling the function to demonstrate dictionary usage
Data_Dict()

# Set
# Set is a collection which is unordered and unindexed. No duplicate members.
def Data_set():
    x = {"Banana", "Apple", "Grapes"}  # Defining a set
    print(x)  # Printing the set
    print(type(x))  # Printing the type of x, which is set

# Calling the function to demonstrate set usage
Data_set()

# Frozenset
# Frozenset is a collection which is unordered and unindexed. No duplicate members.
# The difference between a frozenset and a set is that a frozenset is immutable, meaning that it cannot be changed after it is created, but a set can be changed.
def Data_frozenSet():
    x = frozenset({"Ali", "Ahmed", "Talha"})  # Defining a frozenset
    print(x)  # Printing the frozenset
    print(type(x))  # Printing the type of x, which is frozenset

# Calling the function to demonstrate frozenset usage
Data_frozenSet()

# Boolean
# Boolean is a data type that can only take the values True or False. For example, you can use a boolean to store whether a statement is true or false.
def Data_bool():
    x = True  # Defining a boolean variable
    print(x)  # Printing the boolean variable
    print(type(x))  # Printing the type of x, which is bool

# Calling the function to demonstrate boolean usage
Data_bool()

# Numbers
# Demonstrating different types of numbers: integer, float, and complex
def Data_numbers():
    x = 1  # Integer
    y = 2.8  # Float
    z = 1j  # Complex number
    print("Numbers:")
    print(type(x))  # Printing the type of x, which is int
    print(type(y))  # Printing the type of y, which is float
    print(type(z))  # Printing the type of z, which is complex

# Calling the function to demonstrate different number types
Data_numbers()

# Changing Data Type
# Demonstrating how to change data types
def Data_change():
    x = 1  # Integer
    y = 2.8  # Float
    z = 1j  # Complex number
    a = float(x)  # Converting integer to float
    b = int(y)  # Converting float to integer
    c = complex(x)  # Converting integer to complex
    print("Changing Data Types:")
    print(a)  # Printing the float
    print(b)  # Printing the integer
    print(c)  # Printing the complex number
    print(type(a))  # Printing the type of a, which is float
    print(type(b))  # Printing the type of b, which is int
    print(type(c))  # Printing the type of c, which is complex

# Calling the function to demonstrate changing data types
Data_change()

# Random Number
# Demonstrating how to generate a random number
import random

def Data_random():
    print("Random Number:")
    x = random.randrange(0, 100)  # Generating a random number between 0 and 99
    if x % 2 == 0:
        print("Even")  # Printing if the number is even
    else:
        print("Odd")  # Printing if the number is odd
    print(x)  # Printing the random number

# Calling the function to demonstrate random number generation
Data_random()

# Casting
# Demonstrating type casting in Python
def Data_casting():
    print("Python Casting:")
    x = int(1)  # Casting float to int
    y = int(2.8)  # Casting float to int
    z = int("3")  # Casting string to int
    a = str("s1")  # Casting string to string (no change)
    print(x)  # Printing the integer
    print(y)  # Printing the integer
    print(z)  # Printing the integer
    print(a)  # Printing the string
    print(type(x))  # Printing the type of x, which is int
    print(type(y))  # Printing the type of y, which is int
    print(type(z))  # Printing the type of z, which is int
    print(type(a))  # Printing the type of a, which is str

# Calling the function to demonstrate type casting
Data_casting()

# Slicing Strings
# Demonstrating how to slice strings in Python
def Data_slicing():
    print("Slicing Strings:")
    a = "Hello, World!"  # Defining a string
    print(a[2:5])  # Slicing from index 2 to 5 (not including 5)
    print(a[:5])  # Slicing from start to index 5 (not including 5)
    print(a[2:])  # Slicing from index 2 to end
    print(a[-5:-2])  # Slicing from -5 to -2 (not including -2)

# Calling the function to demonstrate string slicing
Data_slicing()

# Modify Strings
# Demonstrating how to modify strings in Python
def Data_modify():
    print("Modify Strings:")
    a = " Hello, World!"  # Defining a string
    print(a.upper())  # Converting to uppercase
    print(a.lower())  # Converting to lowercase
    print(a.strip())  # Removing whitespace from beginning and end
    print(a.replace("H", "J"))  # Replacing H with J
    print(a.split(","))  # Splitting the string into a list

# Calling the function to demonstrate string modification
Data_modify()
#string concatenation
def Data_contatenation():
    print ("String Concatenation:")
    a="Talha"
    b="Muhammad"
    c=a+ " " + b
    print(c)    
Data_contatenation()
#String Format
def Data_format():
    print("String Format:")
    age = 22
    price=55
    txt = f"My name is Muhammad, and I am {age}" #here f is used to format the string
    bill=f"To buy this product you need {price} rupees"# mostly string format is used where we need to print the value of variable in the string,such as in the bill
    additonal=f"Additional charges are {price+5}"
    print(txt)
    print(bill)
    print(additonal)
Data_format()
#Escape Characters
def Data_escape():
    print("Escape Characters:")
    txt = "We are the so-called \"Vikings\" from the north." #using escape character to print double quotes
    print(txt)
Data_escape()
#String Methods



