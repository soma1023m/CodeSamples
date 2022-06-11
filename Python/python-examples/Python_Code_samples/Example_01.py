# when the dir function is called with the name of an
#imported module in parentheses like this, it returns all the attributes inside that module.
#Some of the names it returns are names you get “for free”: names with leading and
#trailing double underscores (__X__) are built-in names that are always predefined by
#Python and have special meaning to the interpreter
import FirstPython
dir (FirstPython)
print("reading")
exec(open('FirstPython.py').read())