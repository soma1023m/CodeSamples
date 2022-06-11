#The zip() function takes iterables (can be zero or more), aggregates them in a tuple, and returns it.
#Python zip() function
#The zip() is a built-in function that takes one or more iterables as input. It returns an object that contains the elements of the input iterables mapped based on the index. The syntax of this function is:

for i in zip(('a','b','c','d'),(1,2,3,4)):
  print(i)
  
groups=["group1","group2","group3"]
agerange=[(0,5),(6,16),(17,21)]
for i,m in zip(groups,agerange):
  print(i)
  print(m)
  print("Age starts {0} ends {1}".format(m[0],m[1]))