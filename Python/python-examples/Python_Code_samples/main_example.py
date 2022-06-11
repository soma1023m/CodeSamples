#Main function is like the entry point of a program. However, Python interpreter runs the code right from the first line. The execution of the code starts from the starting line and goes line by line. It does not matter where the main function is present or it is present or not.
#Since there is no main() function in Python, when the command to run a Python program is given to the interpreter, the code that is at level 0 indentation is to be executed. However, before doing that, it will define a few special variables. __name__ is one such special variable. If the source file is executed as the main program, the interpreter sets the __name__ variable to have a value __main__. If this file is being imported from another module, __name__ will be set to the module’s name.
#__name__ is a built-in variable which evaluates to the name of the current module.
#Example:
# Python program to demonstrate
# main() function
def sayhello():
   print("Hello")
  
# Defining main function
def main():
    print("hey there")
    sayhello()
  
# Using the special variable 
# __name__
if __name__=="__main__":
    main()