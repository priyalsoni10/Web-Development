""" Modular Programming
Modular Programming ek programming technique hai jisme program ko chhote, independent modules me divide kiya jata hai. Har module ek specific task ya functionality perform karta hai.
Definition: Program ko logically alag-alag modules (functions, classes, files) me todna taki code readable, reusable, aur maintainable ho.
Purpose: Large program ko simpler aur organized banana.

"""
import Fun 
import Fun as F
from Fun import Add # only specific method/function/attribute import kya h 
from Fun import * # fun file pure import krna h
# from Extra.Fun import * # Extra folder h or Fun file name h a.py h

print(Fun.Add(5,6)) # 11
print(F.Add(5,6)) # 11
print(Add(7,7)) # 14

