#SYNTAX, VARIABLE,COMMENTS 

print("Hello!")

a=10
b=20

if a<b:
    print("a este mai mic decat b") 
    
#this is a comment
"""
   Here is a comment on more lines !
"""    
carname = "Volvo"

x=50
y=20

print(x+y)

z = x + y
 
print(z) 

myFirst_name = "Cpr"

x=z=y="ORANGE"

"""
 def myfunc()
   global x   -> declare global variable
   x ="fantastic" 
"""

#DATATYPE

x = 5
print(type(x))
# int

x="Hello world"
print(type(x))
#str

x=20.5
print(type(x))
#float

x = ["apple", "banana", "cherry"]
print(type(x))
#list

x = ("apple", "banana", "cherry")
print(type(x))
#tuple

x = {"name": "Jhon" , "age" : "36"}
print(type(x))
#dict

x= True
print(type(x))
#bool

#NUMBERS

x=5
x = float(x)

x=5.5
x = int(x)

x=5
x = complex(x)

#STRINGS

x = "Hello world!"
print(len(x))

txt = "Hello"
x = txt[0] #the first character of the string txt

x = txt[2:5] #the characters from index 2 to index 4 "llo"

x = txt.strip() #return the string withow any whitespace 

txt = txt.upper() #uppercase

txt = txt.lower() #lowercase

txt = txt.replace("H","J") 

age=36
txt="My age is {}"
print(txt.format(age))

#BOOLEANS

print(10>4)
True

print(10==9)
False

#OPERATORS

print(10*2) #multiply
print(10/2) #divide

fruits = ["apple","banana"]
if "apple" in fruits:
     print("Yes, apple is a fruit!")

if 5!=10:
    print("5 is not equal with 10")   
    
if 5==10 or 4==4:
    print("One of conditions are true") 

#LIST    

print(fruits[1]) #print the second item

fruits[0] = "kiwi"  #kiwi has been changed with apple  
      
fruits.append("orange") #orange is added in the list

fruits.insert(1, "lemon") #add lemon as the second item

fruits.remove("banana") #an item is removed from the list

print(fruits[-1]) #print the last item from the list

fruits = ["banana","orange","kiwi","lemon","apple"]
print(fruits[2:4])

print(len(fruits))

#TUPLES

fruits = ("apple","banana","cherry")
print(fruits[0]) #print first item

print(len(fruits)) #print number of items 

print(fruits[-1]) #print last item

print(fruits[2:4])

#SETS

fruits = {"apple", "kiwi","banana"}

if "apple" in fruits:
    print("Yes")

fruits.add("orange") #add in set

more_fruits = ["mango","grape"]

fruits.update(more_fruits) #add multiple items

fruits.remove("banana") #remove an item

fruits.discard("apple") 

#DICTIONARIES

car = {
   "brand" : "ford",
   "model" : "GT",
   "year" : 2023
}

print(car.get("model"))

car["year"] = 2020

car["color"] = "red"

car.pop("model")

car.clear()

#IF....ELSE

a=10
b=1

if a>b:
   print("Hello")
   
if a!=b:
   print("is not")

if a==b:
   print("yes")
else:
   print("no")
   
if a==b:
   print("1")
elif a>b:
   print("2")
else:
   print("3")
   
c=10
d=20

if a==b and c==d:
   print("!") 
   
#WHILE LOOP

i = 6
while i<4:
   print(i)
   i += 1
#in loop you can use break and continue

#FOR LOOP

for x in fruits:
   print(x)
   
for x in range(6):
    print(x)

#FUNCTIONS

def my_function():
    print("Hello") 

my_function()

def my_function(x,fname):
    print(fname)
    return x+5
                                       
def my_function(*kids):          #if u don' t know the number of arguments that will be passed into you're function you use *
    print("Kids are " + kids[2])  
         
def my_function(**lname):
    print("Name " + lname["nume"]) 

                                      