#You can use the type method to check the value of an object
type(3)
type(3.14)
pi = 3.14
type(pi)
#basic mathematical operators
3+3
3-3
3/3
3*3
3**3
9 / 4#Gives 2 in versions below 3
#In order to get a fraction change one of the numbers into float
9.0/4
9/4.0
10%3 #Returns the remainder
#Python recognizes single and double quotes as the same thing, the beginning and ends of the strings
a="this is a string"
b='this is another string'
print(a+b)
#There are also different string methods for you to choose from as well - like upper , lower , replace , and count 
print(a.upper())

#Count lets you know how many times x appears in the string (can be numbers ora string of words as well).
numbers=['1','2','1','2','2']
print(numbers.count('2'))

#You can also format strings with the format method
print("{0} is a lot of {1}".format("Python", "fun!"))
#List
fruits = ['apple','lemon','orange','grape']
#Dictionary
dict={'one':1,'two':2}
#for loop and if 
for fruit in fruits:
    if fruit=="apple":
        print("This is an apple")
    elif fruit=="orange":
        print("This is an orange")
    else:
        print("This is a fruit.It is a {0}".format(fruit))
print(dict.keys())
for item in dict.keys():
    print("key :{0},value :{1}".format(item,dict[item]))
 
    