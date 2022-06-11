import re
match = re.match('Hello[ \t]*(.*)world', 'Hello Python world')
print(match.group(1))
match = re.match('[/:](.*)[/:](.*)[/:](.*)', '/usr/home:lumberjack')
print(match.groups())
print(re.split('[/:]', '/usr/home/lumberjack'))

L = [123, 'spam', 1.23] # A list of three different-type objects
print(len(L)) # Number of items in the list

#we can index, slice, and so on, just as for strings:
print(L[0]) # Indexing by position
print(L[:-1]) # Slicing a list returns a new list

L + [4, 5, 6] # Concat/repeat make new lists too
print(L * 2)
[123, 'spam', 1.23, 123, 'spam', 1.23]
print(L) # We're not changing the original list
[123, 'spam', 1.23]
L.append('NI') # Growing: add object at end of list
print(L)
print(L.pop(2)) # Shrinking: delete an item in the middle
print(L) # "del L[2]" deletes from a list too
[123, 'spam', 'NI']

M = ['bb', 'aa', 'cc']
M.sort()
print(M)
['aa', 'bb', 'cc']
M.reverse()
print(M)
['cc', 'bb', 'aa']
#Dictionary
D = {'a': 1, 'b': 2, 'c': 3}
print(D)
Ks = list(D.keys())
print(Ks)
Ks.sort()
for key in Ks: # Iterate though sorted keys
 print(key, '=>', D[key]) # <== press Enter twice here (3.X print)
x = 4
while x > 0:
 print('spam!' * x)
 x -= 1
#printing squares
squares = [x ** 2 for x in [1, 2, 3, 4, 5]]
print(squares)

#tuples
T = (1, 2, 3, 4) # A 4-item tuple
print(len(T)) # Length
T + (5, 6) # Concatenation
print(T)
print("here")
print(T[0]) # Indexing, slicing, and more
print("index")
print(T.index(4)) # Tuple methods: 4 appears at offset 3
print("Count")
print(T.count(4)) # 4 appears once
#T[0] = 2 # Tuples are immutable
T = (2,) + T[1:] # Make a new tuple for a new value
print(T)
