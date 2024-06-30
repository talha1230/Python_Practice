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
def Data_tuple():
    x=("Banana", "Apple", "Orange")
    print   (x)
    print (type(x))
Data_tuple()

#list 
def Data_list():
   y=["Banana", "Apple", "Orange"]
   print (y)
   print (type(y))
Data_list()
#dictionary
def Data_Dict():
     x= {"name":"Muhammad", "LastName":"Talha","Age":20}
     index=x["name"]
     print(index)
     print(x)
     print(type(x))
Data_Dict()
#set
def Data_set():
    x={"Banana", "Apple", "Grapes"} 
    print(x)
    print(type(x))
Data_set()
#frozenset
def Data_frozenSet():
    x=frozenset({"ALi", "Ahmed", "Talha"})
    print(x) 
    print(type(x))
Data_frozenSet()
