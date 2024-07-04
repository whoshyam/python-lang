# method to print multiple 
print(''' Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

'Tis your bright and tiny spark,
Lights the trav'ller in the dark:
Tho' I know not what you are,
Twinkle, twinkle, little star.''')

a = 1

b = 2

c = 7

name = "harry"

print(a + b)

#! datatypes
a = 1 # a is an integer

b = 5.22 # b is a floating point number

c = "Harry" # c is a string

d = False # d is a boolean variable

e = None # e is a none type variable


#! rules_variables
a = 23

aaa = 435

harry = 34

sameer = 45

_samerr = 34

# @sameer = 56 # Invalid due to @ symbol
# s@meer # Invalid due to @ symbol

#! operators
# Arithmetic Operators
a = 7
b = 4
c = a + b
print(c)

# Assignment Operators
a = 4-2 # Assign 4-2 in a
print(a)
b = 6
# b += 3 # Increment the value of b by 3 and then assign it to b
b -= 3 # Decrement the value of b by 3 and then assign it to b
print(b)

# Comparison Operators

d = 5==5

print(d)


# Logical Operators

e = True or False

# Truth table of 'or' 
print("True or False is ", True or False)
print("True or True is ", True or True)
print("False or True is ", False or True)
print("False or False is ", False or False)

# Truth table of 'and' 
print("True and False is ", True and False)
print("True and True is ", True and True)
print("False and True is ", False and True)
print("False and False is ", False and False)

print(not(True))

#!type
a = "31.2"
b = float(a) # a but the type should be float
t = type(b) 

print(t)

#! input
a = int(input("Enter number 1: "))
# agar int nhi hoga th input string mae input hoga
b = int(input("Enter number 2: "))

print("Number a is: ", a)
print("Number b is: ", b) 
print("Sum is ", a + b)