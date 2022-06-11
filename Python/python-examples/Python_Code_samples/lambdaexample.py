#Python function definition using the keyword def as follows:

import time
import random
  
listObj=[]
for i in range(100):
  listObj.append(random.randint(1,100))
  
listObj2 = listObj
 
#sorting list using sorted() built-in function
st = time.time()
sorted(listObj)
print("Time taken by sorted(): %s seconds" % (time.time() - st))
 
#sorting list using using list sort() method
st = time.time()
listObj2.sort()
print("Time taken by sort(): %s seconds" % (time.time() - st))

  