"""
DocString in python:
Docstring programming me ek special kind ka string hota hai jo code ke documentation ke liye use hota hai. Mostly Python me use hota hai.
Ye code ke andar likha jata hai taaki function, class, ya module ka purpose easily samjha ja sake.
Docstring triple quotes me likhi jati hai, single line ya multi-line dono ke liye.
Ye runtime me accessible hoti hai via .__doc__.
Python me ye best practice hai har function, class, aur module ke liye docstring likhna.
"""
def add_numbers(a, b): 
    """
    Ye function do numbers ko add karta hai.
    
    Parameters:
    a (int or float): Pehla number
    b (int or float): Dusra number
    
    Returns:
    int or float: Dono numbers ka sum
    """
    return a + b

# Docstring access karna
print(add_numbers.__doc__) # ye jo docstring me lekha h vo print kr dega 

# Package in python
"""Programming ya software development context me “package” ka matlab hota hai ek organized collection of modules, classes, functions, ya resources jo ek saath kaam karte hain aur reuse ke liye ready hote hain. 
Ye concept alag-alag programming languages me thoda alag ho sakta hai. 
Definition: Python me package ek directory/folder hota hai jisme __init__.py file hoti hai aur ek ya zyada Python modules hote hain.
Purpose: Code ko organize karne ke liye aur reuse ke liye.
Package = Organized collection of code/resources
Python: folder with __init__.py
PyPI ka full form hai Python Package Index. Ye Python ka official repository hai jahan pe Python packages available hote hain.
1 PyPI kya hai
Ek online platform jahan developers apne Python packages publish karte hain.
Users pip (Python package installer) ke through packages easily install kar sakte hain.
Basically, Python ka app store hai.
2 PyPI ka purpose
Code ko reuseable aur shareable banana
Popular Python libraries ko central repository me maintain karna
Package installation ko easy aur standardized banana
# Math library
"""
import math
print(math.sqrt(25)) # 5.0
print(math.pi) # 3.141592653589793
print(math.pow(3,2)) # 9.0

# Random module
import random 
print(random.randint(1,10))
l = [6,4,9,3,10,4,8]
print(random.choice(l))

# Pyttsx3 module for text to speech 
# import pyttsx3 # python text to speech version 3
# a = pyttsx3.init()
# a.say("Hello World ,How are you  ")
# a.runAndWait()
# -----------------------------

# import pyttsx3
# def speak(txt):
#     b = pyttsx3.init()
#     b.say(txt)
#     b.runAndWait()
# speak("Hy Guys")    
# speak("How's going") 
# -----------------------------
import pyttsx3
import webbrowser
def say (text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()  

while True:
    choice = input("Type Anything:")
    if choice == "hello":
        say("Hello Boss ! ") 
    elif choice == "good morning":
        say("Good Morning !") 
    elif choice == "open youtube":
        say("Okk Boss !") 
        webbrowser.open("https://www.youtube.com/")
    elif choice == "bye":
        say("Bye Boss !")
        break
    else:
        say("Sorry,I don't understand! ") 
        
             



