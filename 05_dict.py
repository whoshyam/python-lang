d = {} # Empty dictionary
marks = {
    "Harry": 100,
    "Shubham": 56,
    "Rohan": 23
}


# print(marks, type(marks))
print(marks["Harry"])

# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Harry": 99, "Renuka": 100})
# print(marks)

print(marks.get("Harry2")) # Prints None
print(marks["Harry2"]) # Returns an error

# ---------------
d = {}

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})


print(d)