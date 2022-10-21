#Demo
from pathlib import Path


print(__file__)
print(Path(__file__))
print(Path(__file__).resolve())
print(__name__)

def hello():
    print("Hello")
