a = int(input("Enter your age: "))

# If else statement
if(a>=18):
    print("You are above the age of consent")
    print("Good for you")

else:
    print("You are below the age of consent")


print("End of Program")
# --------------
a = int(input("Enter your age: "))

# If elif else ladder
if(a>=18):
    print("You are above the age of consent")
    print("Good for you")

elif(a<0):
    print("You are entering an invalid negative age")

elif(a==0):
    print("You are entering 0 which is not a valid age")    

else:
    print("You are below the age of consent")


print("End of Program")
# ----------------
a = int(input("Enter your age: "))

# If statement no: 1
if(a%2 == 0):
    print("a is even")
# End of If statement no: 1

# If statement no: 2
if(a>=18):
    print("You are above the age of consent")
    print("Good for you")

elif(a<0):
    print("You are entering an invalid negative age")  

else:
    print("You are below the age of consent")
# End of If statement no: 2

print("End of Program")