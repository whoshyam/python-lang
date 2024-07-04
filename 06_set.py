e = set() # Dont use s = {} as it will create an empty dictionary
s = {1, 5, 32, 54,5, 5, 5} 


print(s)

s1 = {1, 45, 6, 78}  
s2 = {7, 8, 1, 78}

print(s1.union(s2))
print(s1.intersection(s2))


# ---------------
s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?

print(len(s))
# in python 20==20.0 true