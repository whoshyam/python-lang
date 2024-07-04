i = 1

while(i<51):
    print(i)
    i +=1 # or i = i + 1
'''
Output:
1
2
3
4
5
'''

# ----------------------------------
l = [1, "Harry", False, "This", "Rohan", "Shubham", "Shubhi"]

i = 0

while(i<len(l)):
    print(l[i])
    i +=1

# ----------------------------------
    ## For Loop with Lists
l = [1, 4, 6, 234, 6, 764]
for i in l:
    print(i)

## For Loop with Tuples
t = (6, 231, 75, 122)
for i in t:
    print(i)

## For Loop with Strings
s = "Harry"
for i in s:
    print(i)

# ----------------------------------
    
l= [1,7,8] 

for item in l:
    print(item)

else:
    print("done") # this is printed when the loop exhausts!

# -----------------------
    
for i in range(100):
    if(i == 34):
        break # Exit the loop right now
    print(i)

for i in range(100):
    if(i == 34):
        continue # Skip this iteration
    print(i)    

# ----------------
for i in range(645):
    pass
# pass instructs to do nothing 



i = 0
while(i<45):
    print(i)
    i += 1


# ----------------
'''
For n = 3
  *
 ***
*****

For n = 5
    *
   ***
  *****
 ********
**********

'''

n = int(input("Enter the number: "))
for i in range(1, n+1):
    print(" "* (n-i), end="") 
    #print by default new line deta h th wo na de th we use end=""
    print("*"* (2*i-1), end="")
    print("")