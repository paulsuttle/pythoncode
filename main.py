#https://www.linkedin.com/learning/python-essential-training-2018

#!/usr/bin/env python3  <- NB: this is supposed to be the very first line of comment code for it to work for Macs
#After the "shebang" (#!) is the path to the executable that will run your script, along with any other optional arguments. In this case, we're using the Unix env command to find the path to the Python interpreter. This is a common usage. 

#Generally speaking, a statement is a unit of execution, and an expression is a unit of evaluation. In Python, an expression is any combination of literals, identifiers, and operators. A statement is a line of code. It's not clear why this is important, although implied that it is…. 🙄🙄🙄



#Method of the String object, common in Python 3 before f string introduced in 3.6.3
x = 69
print("Hello, World. {}".format(x))
print(f"Hello, World. {x}")


#BLOCKS & scope: allegedly blocks don't define scrope of variables? But from using the same examples it seems to be now no longer be a thing

x = 42
y = 69

if x > y:
  print(f"{x} is greater than {y}")
elif x < y:
  print(f"{x} is less than {y}")
else:
  print("I dunno, maybe they're equal")

#Loops
words = ['one', 'two', 'three', 'four', 'five']

n = 0
while(n < 5):
    print(words[n], end = ' ')
    n += 1
print()

#Does the same thing...
for i in words:
  print(i, end = ' ')
print()

# simple fibonacci series
# the sum of two elements defines the next set

a, b = 0, 1
while b < 1000:
    print(b, end = ' ', flush = True)
    a, b = b, a + b

print() # line ending



#FUNCTIONS: Setting n= to a value sets a default in case one is not provided and avoids an error
def function(n=69):
  return n * 2

x = function(21)
print(x)



#OBJECTS: In Python a class is a definition and an object is an instance of a class. 


#An introduction to the __name__ variable and its usage in Python
#https://www.freecodecamp.org/news/whats-in-a-python-s-name-506262fe61e8/


class Duck:
    sound = "Quaaack!"
    walking = "Walks like a duck."
  
    def quack(self):
        print(self.sound)

    def walk(self):
        print(self.walking)

def main():
    donald = Duck()
    donald.quack()
    donald.walk()

if __name__ == '__main__': main()


#TYPES AND VALUES
x= "seven"
print(f"x is {x}")
print(type(x))

print(x.capitalize())
print(x.lower())
print(x.upper())

#Can use FORMAT to add other values/variables in 0,1,etc order within {} brackets
#the :<9 and :>9 are left-align within 9 spaces and right-align within 9 space. Use a leading zero on the number to fill the remaining spaces with zeros.

y = 'seven "{0:<9}" "{1:>9}"'.format(8,9)
print(y)

print('seven "{1:<09}" "{0:>09}"'.format(8,9))

#Do the same with F-STRINGS
print(f'seven "{8:<09}" "{9:>09}"')

#NUMERIC TYPES
x= 7
y= 3
print(f"{x} / {y} = {x / y}")
print(f"{x} // {y} = {x // y} (ie. no remainder includede)")
print(f"{x} % {y} = {x % y} modulo - what's remaining from {x} after the {y}\'s have been removed - it's not the same as 'remainder' as we're used to thinking of it")

#PRECISION VS ACCURACY
print(f"What even is maths? Python thinks that (.1 + .1 + .1) - .3 = {(.1 + .1 + .1 ) -.3}")

#So don't use FLOATS for money or when accuracy is required

from decimal import *
a= Decimal(".10")
b= Decimal(".30")
x = a + a + a - b
print(f"x is {x}")
print(type(x))

#BOOLEAN / BOOL
#Try setting x to 0, True, False, None, "", some number/text

x= ""
print(f"x is {x}")
print(type(x))

if x:
  print("True")
  #x as True or any number/text will print "True"
else:
  print("False")
  #x as 0, "", None, False will all print "False"



#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

#Square brackets are LISTS
x = [ 1, 2, 3, 4, 5 ]
x[2] = 42 # Count starts at 0, so this is actually re-setting the third item

for i in x:
    print('i is {}'.format(i))
  
#Rounded brackets are TUPLES
y = ( 1, 2, 3, 4, 5 )
#y[2] = 42 <-- this is Commented out as it isn't allowed with TUPLES

for j in y:
    print('j is {}'.format(j))

z = range(5) #Starts at 0
for k in z:
    print(f'k is {k}')

z2 = range(0,10,2) #Starts at 0, finish at 10, in steps of 2
for k2 in z2:
    print(f'k2 is {k2}')

z3 = list(range(0,10,2)) #Make ir a LIST if you need to change values
z3[2] = 69 #Can change LISTS (not RANGES) 
for k3 in z3:
    print(f'k3 is {k3}')

#DICTIONARIES

dictionary={"one":1,"two":2, "three":3, "four":4, "five":5}

dictionary['three'] = 69

for k, v in dictionary.items():
  print(f"k: {k}, v: {v}")



#TYPE() and ID()


#tuple
x = ( 0, 'one', 2.0, [3,"three"], 4 )
print(f"x is {x}")
print(type(x))

for i in range(5):
  print(f"{x[i]} is a {type(x[i])}")
  if isinstance(x[i], float):
    print(" - but does it even float tho, bro?")
print()    
y = ( "zero", 'one', 4, [3,"three"], 2.0 )
print("Different tuples, different IDs (diff objects)")
print(f"id of x: {id(x)}")
print(f"id of y: {id(y)}")
print()
print("Different same-pos values different tuples, different IDs (diff objects)")
print(f"id of x[0]: {id(x[0])}")
print(f"id of y[0]: {id(y[0])}")
print()
print("Same values (same-pos), different tuples, same ID (same object)")
print(f"id of x[1]: {id(x[1])}")
print(f"id of y[1]: {id(y[1])}")
print()
print("Same values (different positions), different tuples, same ID (same object)")
print(f"id of x[4]: {id(x[4])}")
print(f"id of y[2]: {id(y[2])}")


# CONDITIONAL SYNTX
# x is y  and x is not y to give boolean T/F
#if x is not y: <- True or False
#if x is in y:  <- Membership

#TERNARY
hungry = True
x = 'Feed the bear now!' if hungry else 'Do not feed the bear.' # <- must include the ELSE, but can set it to None
print(x)


#OPERATORS 
# **  Exponent (not ^ which is XOR)
# x=-x  <- to swap the sign (NB: x=+x doesn't do anything)
#BITWISE for manipulating binary maths
# AND &, | OR, ^ XOR, << SHIFT LEFT, >> SHIFT RIGHT
# no XOR in Python :(

#WHILE and FOR loops have BREAK and CONTINUE options
#a BREAK shortcuts the loop
#an ELSE statement after a loop only executes if the loop exits normally.

secret = 'password'
pw = ''
auth = False
count = 0
max_attempt = 5

while pw != secret:
  count += 1
  if count > max_attempt: break
  if count == 3: continue # <- skip the 3rd attempt
  pw = input(f"{count}: What's the secret word? ")
else:
  auth = True

print("Authorised" if auth else "Calling the cops...")
  


#I don't understand argument lists, or keyword arguments
# FUNCTIONAL ARGUMENTS and mutable Types
x= [5]
y=x # <- because [5] is mutable, you're assigning a reference to the object, not the same value
y[0] =3 # <- so you're actually changing both here
print(x)
print(y)



#You can define variable length argument lists - the "convention" is to use (*args) when you do this

#def main():
#    kitten('meow', 'grrr', 'purr')
#def kitten(*args):
#    if len(args):  <<- ie. however many arguments were provided at the DEF stage


#def main():
#    kitten(Buffy = 'meow', Zilla = 'grr', Angel = 'rawr')
#def kitten(**kwargs):
#    if len(kwargs): # <<- for keyword (DICTIONARY) arguments use: (**kwargs)


#GENERATORS and DECORATORS
#Geneators use YIELD instead of return ...?

#DECORATORS use @FUNCTION_NAME to send the followinf DEF function as an argument to that 1st @ mentioned function

#def elapsed_time(f):
#  f() # <- calls the function passed to it
#...
#
#@elapsed_time #<- passed to this function
#def big_sum(): #<- this is the function being passed

#CLASSES
#https://realpython.com/python3-object-oriented-programming/
#everything is an object in Python, and a class is how an object is defined - A class is a blueprint for how something should be defined - It doesn’t actually contain any data.  Python class names are written in CapitalizedWords notation by convention
#An instance of a CLASS is called an OBJECT/ an "instance" is an OBJECT that is built from a CLASS and contains real data. Objects are created by calling the Class like a function ("objectname=ClassName()")
#functions associated with a Class are called Methods, this provide the behaviors and actions that an object created from the class can perform with its data.
#We have data in the form of variables, and methods in the form of  function definitions. You'll notice that the first parameter of a METHOD is always self. Self is not a keyword, but it's used by convention. SELF refers to a specific OBJECT, not the CLASS itself

class Animal:
    def __init__(self, **kwargs):  #<- __init__ is a special name for class function that operates as an initialiser, or constructor. NB: "Self" points at the object
        self._type = kwargs["type"] if "type" in kwargs else "kitten"#<- use of "_" is meant to discourage direct calling of the variable
        self._name = kwargs["name"] if "name" in kwargs else "fluffy"
        self._sound = kwargs["sound"] if "sound" in kwargs else "rawr"

    def type(self):
        return self._type  #<- "accessors" or "getters" to retrurn the value of the object variables 

    def name(self):
        return self._name

    def sound(self):
        return self._sound

def print_animal(o):
    if not isinstance(o, Animal):
        raise TypeError('print_animal(): requires an Animal')
    print('The {} is named "{}" and says "{}".'.format(o.type(), o.name(), o.sound()))


def main():
    a0 = Animal(type='kitten', name='fluffy', sound='rwar') #Create a0 Object from Animal Class
    a1 = Animal(type='duck', name='donald', sound='quack') #Create a1 Object from Animal Class
    print_animal(a0)
    print_animal(a1)
    print_animal(Animal(type='velociraptor', name='veronica', sound='hello'))
    print_animal(Animal())

if __name__ == '__main__': main()



# SUPER calls the Parent Class for inheritance . eg. super().__init__(**kwargs)

#YIELD was created in Python more recently, but before then there were ITERATOR functions setup by "def _iter_(self):" functions
#These also use _next_ functions to show how they iterate, pluys use "raise StopIteration" to drop out of the loop



#EXCEPTIONS - predicting and working around errors

try:
  x=int('poop') #<- not valid as the text given can't be converted into an integer
except ValueError:
  print("I caught a value error!")
except:
  print("unknown error")
else:
  print("no error!")

