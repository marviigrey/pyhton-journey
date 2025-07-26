from math import pi  #import a single package from a module
import sys
import random as rdm #give an alias to a module
from enum import Enum
import lagos
from rps7 import rock_paper_scissors

print(pi)

print(dir(rdm))

for item in dir(rdm):
    print(item)

print(lagos.capital)
lagos.funfact()

print(__name__) #prints the name of a module

print(lagos.__file__) # prints the location of the module

print(rdm.__file__)

rock_paper_scissors()

