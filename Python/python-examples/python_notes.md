# Python module to operate excel
**openpyxl** is a Python library to read/write Excel 2010 xlsx/xlsm/xltx/xltm files.
It was born from lack of existing library to read/write natively from Python the Office Open XML format.
Refer to <https://openpyxl.readthedocs.io/en/stable/> for details

# Python Distributions
## Anaconda:
<https://www.anaconda.com>

# Python Libraries

## NumPy Library:
NumPy is the fundamental package for scientific computing in Python. It is a Python library that provides a multidimensional array object, various derived objects (such as masked arrays and matrices), and an assortment of routines for fast operations on arrays, including mathematical, logical, shape manipulation, sorting, selecting, I/O, discrete Fourier transforms, basic linear algebra, basic statistical operations, random simulation and much more.
<http://www.numpy.org>

## SciPy Library:
SciPy (pronounced “Sigh Pie”) is an open-source software for mathematics, science, and engineering.
<https://www.scipy.org>

## Matplotlib Library:
Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python. Matplotlib makes easy things easy and hard things possible.

Create publication quality plots.
Make interactive figures that can zoom, pan, update.
Customize visual style and layout.
Export to many file formats .
Embed in JupyterLab and Graphical User Interfaces.
Use a rich array of third-party packages built on Matplotlib.

<https://matplotlib.org>

# Python Editors

## Spyder:
<https://www.spyder-ide.org>

## Visual studio Code:
<https://code.visualstudio.com>

## Visual Studio:
<https://visualstudio.microsoft.com>
https://docs.microsoft.com/visualstudio/python

## PyCharm:
<https://www.jetbrains.com/pycharm/>

## Wing:
<https://wingware.com>

## Jupyter Notebook:
<http://jupyter.org>

# Python Tutorials
## Python Tutorial - w3schools.com
<https://www.w3schools.com/python/>

## The Python Guru
<https://thepythonguru.com>

## Wikibooks - A Beginner’s Python Tutorial:
<https://en.wikibooks.org/wiki/ABeginner>

## TutorialsPoints - Python Tutorial:
<https://www.tutorialspoint.com/python/>

## The Hitchhiker’s Guide to Python:
<https://docs.python-guide.org>

## Google’s Python Class:
<https://developers.google.com/edu/python/>


# Difference between tuple and list

## List
*Lists can be created using square brackets []
listName = [value1, value2, value3, ... ]
myList = ["Archana", "Vaidya" ]

*In python we can use type function which gives data type of objects.
type(listName)

*List has more built in function than tuple
dir(listname)
 

*List are dynamic and mutable
In python there are three pre-defined method fro adding elements to list they are append(), insert() and extend().
listName.insert(0,"Aman")
listName.append(["Aman","Vaidya"])
listname.extend(["Madam Rosmerta","Ginny Weasley"])
a=[1,2,3,4,5,6,7,8,9,10]
print('a=',a.__sizeof__())

## Tuple
*tuples can be created in two ways first way is using parenthesis () and the second way is without using any parenthesis()
tupleName = (value1, value2, value3, ...)
myTuple =("Belal","Khan")
Other way
tupleName = value1, value2, value3, ...
numbers =1,2,3,4,5
type(tupleName)
dir(tupleName)

*Tuple is static and immutable

*One of the major advantage of using tuple over List is that tuple operation takes smaller size than that of list. Which makes tuple execution bit faster than lists. We can get size of an object by using  _sizeof()_ method.
b=(1,2,3,4,5,6,7,8,9,10)
print('b=',b.__sizeof__())

*Since List has more functionality than tuples. But tuples can be used over lists in many scenarios. such as-
We can use tuple instead of list where we don’t want to change our data dynamically.
Tuple can be used inside a list to store data. Reading data is simpler when it is stored inside a list.
[(2,3),(3,4),(4,5),(6,6)]

*Tuples are useful for grouping static data. It is useful for representing what other languages often call records .

*Tuple assignment: Python has a very powerful tuple assignment feature that allows a tuple of variables on the left of an assignment to be assigned values from a tuple on the right of the assignment.
For example In other language like C and C++ we have to write a much complex code to swap the values of two variable. For example
temp=a;
a=b;
b=temp;



## Python Tuple vs List – Points to remember

*Lists are mutable while Tuples are immutable.

*Lists have variable length while tuple has fixed length.

*Lists has more functionality than tuple.

*List object size is comparatively larger than Tuple.

*Execution of tuple is faster than Lists.
