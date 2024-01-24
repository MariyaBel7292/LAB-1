#Python SYNTAX
#Ex1
print
("Hello World")

#Ex2
if 5 > 2:
 print("YES")



"""PYTHON COMMENTS
Ex1
"""

#This is a comment

#Ex2
"""
This is a comment
written in 
more than just one line
"""


#PYTHON VARIABLES
#Ex1
carname="Volvo"

#Ex2
x=50

#Ex3
x=5
y=10
print(x+y)

#Ex4
x = 5
y = 10
z= x + y
print(z)

#Ex5
x,y,z = "Orange", "Banana", "Cherry"

#Ex6
x = y = z = "Orange"

#Ex7
def myfunc():
  global x
  x = "fantastic"




#PYTHON DATA TYPES
#Ex1
x = 5
print(type(x))

int

#Ex2
x = "Hello World"
print(type(x))

str


#Ex3
x = 20.5
print(type(x))

float


#Ex4
x = ["apple", "banana", "cherry"]
print(type(x))

list

#Ex5
x = ("apple", "banana", "cherry")
print(type(x))

tuple


#Ex6
x = {"name" : "John", "age" : 36}
print(type(x))

dict

#Ex7
x = True
print(type(x))

bool




#PYTHON NUMBERS
#Ex1
x = 5
x = float(x)

#Ex2
x = 5.5
x = int(x)

#Ex3
x = 5
x = complex(x)




#PYTHON STRINGS
#Ex1
x = "Hello World"
print(len(x))

#Ex2
txt = "Hello World"
x = txt[0]

#Ex3
txt = "Hello World"
x = txt[2:5]

#Ex4
txt = " Hello World "
x = txt.strip()

#Ex5
txt = "Hello World"
txt = txt.upper()

#Ex6
txt = "Hello World"
txt = txt.lower()

#Ex7
txt = "Hello World"
txt = txt.replace("H", "J")

#Ex8
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))







