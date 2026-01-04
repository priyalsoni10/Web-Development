# import ShiftingItem.Books # Hy From Books module!
import ShiftingItem.Clothes.Jeans # Hy From Jeans Modules
ShiftingItem.Clothes.Jeans.display() # This module/cartoon contains all my jeans!
# b = ShiftingItem.Books.MyClass()
# b.bookType() #Its has all my non fiction books!
from ShiftingItem import Books # Hy From Books module!
Books.display() #This module/cartoon contains all my books!
#  description.py ko hum PakageMain.py se call nhi krskte kyuonki dono file ek sath module folder ke undeer h isko call krne ke leeye main file ko bahar pythonCode me krna hoga tb access krskte h
# from ShiftingItem.Footwears import Flats,Heels # usme jitne bhi function h subkuch
# Flats.display() # Hy From Flats Modules
# Heels.display() #This module/cartoon contains all my heels!
from ShiftingItem.Footwears.Flats import display ,Flat_color ,a
display() # Hy From Flats Modules,This module/cartoon contains all my flats!
Flat_color() # Red , Pink ,Blue, White , Black!
print(a) # 1
from ShiftingItem.Footwears.Flats import *
display() # Hy From Flats Modules,This module/cartoon contains all my flats!
Flat_color() # Red , Pink ,Blue, White , Black!
Flat_type() # This flat is Kolhapuri!
# hum particular module kee sare ffunction methods ko call krskte h but hum package se saree modulee ko call nhi krsktee kyunki vo bhot sare ho skte h

from ShiftingItem.Footwears import * 
Heels.display()  #This module/cartoon contains all my heels!
Flats.display() #This module/cartoon contains all my flats!