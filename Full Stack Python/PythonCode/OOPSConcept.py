# OOPS-> OOPS (Object-Oriented Programming System) ek programming approach hai jisme hum real-world cheezon ko code ke form me represent karte hain.
# OOPS ka matlab hai program ko “objects” ke through banana,jaise real life me cheezein hoti hain.
# To map with real world scenerios we started usin object in code this is called oops
# Class-> Class is a blueprint for creating objects.
# Object -> Object class ka real instance hota hai
# Creating class
class Student: # class
    name = "Kiran"
#creating objects(instance)
s1 = Student() # object(instance)(yha constructer internally bnjaega or call bhi ho jaaega )
s2 = Student() # object(instance)
print(s1)   # <__main__.Student object at 0x000001436F1A6A50> is location pr h
print(s1.name) # Kiran   
print(s2.name) # Kiran same ayega saare object ke leye
# ------------------------------------
class Car:
    color = "Blue"
    brand = "Mercedes"
car1 = Car()
print(car1)    
print(car1.color)    
print(car1.brand) 
# -----------------------------------
""" '''Constructor -> Constructor ek special function hota hai jo object bante hi automatically call ho jaata hai.
 Matlab jaise hi tum class ka object banate ho,
constructor khud chal jaata hai.

🧠 Real-life example
Socho tumne mobile liya 📱
Mobile ON hote hi kuch settings auto set ho jaati hain
(language, date, time)
Ye hi kaam constructor karta hai.
__init__() isse denote krte
Constructor ka kaam
Object ke data ko initialize karna
Default values set karna
Object ready karna

All classes have a function called __init__() which is always executed when the claass is being initiated 
The self parameter is a reference to the current instance of the class and is used to access variables that belongs to the class 
self Python me current object ko refer karta hai.
Matlab:
Class ke andar jo object ka data ya function use ho raha hai, self usi object ko point karta hai.
Simple example (real life)
Socho class = Student
Object = Amit
 Jab Amit apna naam bole:
“main Amit hoon”
Programming me ye self hai
(main = self)

# Types of Attributes
# Class attribute -> jo sb object ke leye common hote h
# Object attribute -> hr object ke according alg alg hote h  
''' """
# Consttructor
class Students:
    college_name = "ABC College " # class attribute
    name = "Anonymous " # class attribute (phle object me check krega mil gya to print kr dega nhi to ye print krega)
    # default constructer
    def __init__(): # jisse parameter match honge vo hi chalega
        pass 
    # Parameterised constructer
    def __init__(self ,name,marks):
        print(self) # <__main__.Students object at 0x0000029FB95D6CF0> self current object ko reference karta hai.
        print("Adding new student in database...")
        self.name = name
        self.marks = marks
    # def __init__(abcd ,fullname): ## self = abcd(self ka name de deya h)
    #     print("Adding new student in database...")
    #     abcd.name = fullname 
    # name = "Kiran"
st1 = Students("Raghav" ,87) # instance attribute    
st2 = Students("Ravina" ,78)  # instance attribute  

print(st1.name) # Raghav
print(st1.name,st1.marks) # Raghav  87
print(st1.college_name) # ABC College
# print(st1.name) # Raghav
print(st2.name) # Ravinaa
print(st2.name,st2.marks) # Ravina  78
print(st2.college_name) # ABC College
print(Students.college_name) # ABC College
# -------------------------------------

# Methods -> Methods are functions that belong to object
class Student1:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks 
    def hello(self): # Methods
       print("hello",self.name) 
    def get_marks(self):
        return self.marks   

s = Student1("Priya",78)
print(s.name) # Priya          
s.hello()  # hello Priya  
print(s.get_marks()) # 78    

# Create student class that takes name and marks of 3 subjects as arguments in constructor then create a method to print the average
class Student2:
    def __init__(self, name ,marks):
        self.name = name
        self.marks = marks
    def get_avg(self) :
        sum = 0
        for i in  self.marks:
            sum+=i
        avg = ((sum)/3)    
        print("Hi",self.name , " Your average score is : ", avg)
s4 = Student2("Priyal",[94,86,88])
s4.get_avg() # Hi Priyal  Your average score is :  89.33333333333333
s4.name = "Princi"
s4.get_avg()
# print(s4.name)    
# ---------------------------------
# Static Method -> Method that don't use the self parameter(work at class level)
# Decorator allow us to wrap another function in order to extend the behavior of the wrapped function,without permanently modifying it
# Static method wo method hota hai jo
#  na object se related hota hai
#  na self use karta hai
# Ye class se related logic ke liye hota hai.
class Student3():
    @staticmethod # decorator
    def college():
        print("ABC College ")  
s5 = Student3()
s5.college()  
#----------------------------------   
 
"""Abstraction -> Hidding the implementation details of  a class and only showing the essential features to the user.
Abstraction ka matlab hai:
Sirf important cheez dikhana
Andar ka complicated kaam chhupa dena
TV Remote
Tum buttons dabate ho (ON, OFF, Volume)
Andar signal kaise ja raha hai pata nahi
 Ye hi abstraction hai
 """
class Car:
    def __init__(self):
          # Internal working (hidden from user)
        self.acc = False # accelator
        self.brk = False # break
        self.clutch = False # clutch
    def start(self): # start() method abstraction hai kyunki ye internal working chhupa kar sirf result dikhata hai.
        # Abstraction: user ko sirf "car start" dikhata hai
        # Andar ka logic (acc, clutch) hide hota hai
        self.clutch = True 
        self.acc = True
        print("Car started...")
car1 = Car()
car1.start()   # User sirf start() call karta hai → abstraction 

#-----------------------------------
"""Encapsulation -> Wrapping the data and function into a single unit(object)
Encapsulation ka matlab hota hai:
Data (variables) aur methods ko ek hi class ke andar bandh kar rakhna
Data hide hota hai
Direct access ko restrict karna
Access sirf methods ke through
Bank Account
Tum balance directly change nahi kar sakte
Sirf methods use karte ho:
deposit()
withdraw()
Data protected hai → ye encapsulation hai
"""
# Create Account class with 2 attributes - balance &  account no.create methods for debit,credit and printing the balance
class Account:
    def __init__(self,bal,acc):
       self.balance = bal
       self.account_no = acc
       # debit method
    def debit(self,amount):
        self.balance -= amount 
        print("Rs.", amount ,"was debited" )
        print("Total Balance:" ,self.getBalance()) 
    def credit(self,amount):
        self.balance += amount
        print("Rs." ,amount,"was credited") 
        print("Total Balance:" ,self.getBalance()) 
    def getBalance(self):
        return self.balance      

acc1 =Account(10000,12345)
print(acc1.balance)
print(acc1.account_no)
acc1.debit(1000)
acc1.credit(500)

"""del keyword -> Used to delete object properties or object itself
del Python ka keyword hai jo object, variable, list item, ya object ke attribute ko delete karne ke kaam aata hai.
del = hata dena / remove kar dena (memory reference se)
"""
class Student6:
    def __init__(self,name):
        self.name = name # # Object ka attribute
s1 = Student6("Priyal")
print(s1) ## Object ka reference print hota hai <__main__.Student6 object at 0x0000028F76B27620>
print(s1.name) ## Attribute value print hoti hai → Priyal
# del s1   #  Pura object delete ho jaata  Ab s1 exist hi nahi karta (NameError)
# print(s1) # name 's1' is not defined
# del s1.name #   Sirf 'name' attribute delete hua Object s1 abhi bhi exist karta hai
# print(s1.name) #'Student6' object has no attribute 'name'
# -----------------------------------
"""Private(like) attributes and methods
# Private attributes and methods are meant to  be used only within the class and are not accessible from outside the class
Python me strict private nahi hota,
lekin naming convention ke through hum cheezon ko private jaisa bana dete hain.
Name mangling ka matlab hai:
Python private-like (__) naam ko automatically change kar deta hai,
taaki wo class ke bahar direct access na ho sake.
Jab tum kisi variable ya method ka naam __ se start karte ho,
Python uska naam andar hi andar badal deta hai.
__name  →  _ClassName__name
Tum likhte ho: self.__age
Python internally bana deta hai:self._Student__age
class ke under private method ko call kr skte h but class ke bahar nhi kr skte h
"""


class Account1:
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass # (__ 2 underscore mtlb private h ye attribute )
    def reset_pass(self):
        print(self.__acc_pass)   # abcde  ye chal jaega kyuki ye class ke under h  
acc2 =  Account1("12345","abcde")
print(acc2.acc_no) # 12345
print(acc2.reset_pass()) # call kr None return krega 
# print(acc2.__acc_pass)  # 'Account1' object has no attribute '__acc_pass'  

class Person:
    __name = "Anonymous" 
    def __hello(self): #  private
        print("Hello User!")
    def welcome(self):
        self.__hello()    # Hello User!
p1 = Person()
# print(p1.__name)  #'Person' object has no attribute '__name
# print(p1.__hello()) # 'Person' object has no attribute '__hello'  ye krna possible nhi h
print(p1.welcome()) # None-> (Hello User!) ye possible h kyounki welcome method ke under hello function ko call keya h jo ki class ka method h or class ke underhi call keya h
# -----------------------------------------

""" Inheritance -> Wheen one class(child/derived) drives the properties & methods of another class(parent/base)
Inheritance ka matlab hota hai:
Ek class dusri class ki properties (data) aur methods le leti hai
Real-life example
Parent →  Child
Child:
Parent ki aadatein
Parent ki property
Same concept programming me
Important points
Child class parent ke public & protected members use kar sakti hai
Private (__) directly inherit nahi hote (name mangling)
Code reusability badhti hai
Types of inheritance:
1. Single inheritance
Ek parent class → ek child class
2. Multilevel inheritance
Parent → Child → Grandchild (chain)
3. Multiple inheritance
Ek child → multiple parents
4. Hierarchical Inheritance
 Ek parent → multiple child classes
5. Hybrid Inheritance
Combination of two or more types
(Single + Multiple + Multilevel etc.) 
"""

# Single Inheritance
class Car: # Parent class
    color = "Black"
    @staticmethod
    def start():
        print(" Car started... ")
    @staticmethod
    def stop():
        print(" Car stopped... ")   
class ToyotaCar(Car): # child class
    def __init__(self,name):
        self.name =  name
        
car2 = ToyotaCar("Fortuner") 
car3 = ToyotaCar("Duster")
print(car2.name) # Fortuner       
print(car3.name) # Duster    
print(car2.start()) # None ->  Car started... kyounki humne car class ko inherit keya h to error nhi aaega
print(car2.color) # Black

# Multilevel inheritance
class Car1: # Parent for Toyota car
    @staticmethod
    def start():
        print(" Car started... ")
    @staticmethod
    def stop():
        print(" Car stopped... ")   
class ToyotaCar(Car): #  Parent for Fortuner class->Derieved class for Car1->Multilevel 
    def __init__(self,brand):
        self.brand =  brand
class Fortuner(ToyotaCar): # Derived class for Toyota ->  Multilevel
    def __init__(self,type):
        self.type = type
car3 = Fortuner("diesel")    
car3.start()     #Car started...
# Multiple Inheritance
class A: # Parent class
    varA = "Welcome to class A"
class B: #  Parent class
    varB = "Welcome to class B"
class C(A , B) : # child of both classes A,B -> multiple inheritance
    varC = "Welcome to class C"
c1 = C() 
print(c1.varC)    # Welcome to class C   
print(c1.varB)  # Welcome to class B    
print(c1.varA)  # Welcome to class A

# Heirarchical inheritance
class A: # Parent class of B,C
    pass
class B(A): # child of A
    pass # A ka child B bhi h or C bhi
class C(A): # child of A
    pass

# Hybrid inheritance
class A: # Combination of Single,Multilevel or multiple inheritance 
    pass

class B(A): # child  of A -> Single inheritance 
    pass

class C (): 
    pass

class D(B, C): # Child of B,C -> Multiple
    pass


""" Super Method -> Super() is used to access methods of the parent class 
super() parent (base) class ke method / constructor ko call karne ke liye use hota hai.
Parent ke variables / setup ko initialize karne ke liye
super() bina inheritance? -> Possible nahi
super() sirf inheritance me kaam karta hai
Method overriding ke time
Parent logic reuse karna ho
Code duplication avoid karna ho
super() is used to access parent class members in a child class.
**Jab inheritance ke baad parent ke methods / attributes direct call ho sakte hain,
to super() kyun use karte hain?**
super() parent ka method dobara use (reuse) karne ke liye hota hai,
especially jab child same method ko override kar raha ho.
Object ke through call  → super() ❌
Constructor ke andar call → super() ✅
Child object = Parent + Child
Parent object = Only Parent
Hum aksar child class ka object isliye banate hain
taaki parent ke saare methods free me mil jayein
aur saath me child ke extra features bhi.
Kya parent ka reference child object ko point kar sakta hai?->Haan (Polymorphism)
ab real-world cheez specific(child) ho (jaise ToyotaCar), tab Child class ka object banate hain.
Jab cheez generic(parent) ho (jaise Car), tab Parent class ka object banate hain.
Sirf car chahiye
👉 Brand matter nahi karta

Specific (Child)
car = ToyotaCar()
Toyota car chahiye
extra features + brand behavior chahiye
"""
class Car:
    def __init__(self,type):
        self.type = type
    @staticmethod
    def start():
        print("Car Started...") 
    @staticmethod
    def stop():
        print("Car stopped....")
class ToyotaCar(Car):
    def __init__(self,name,type):
        self.name = name 
        super().__init__(type) # isse parent class ke type attribute ko change kr skte h
        super().start() # parent class ke method ko call keya h constructer ke under isssleye super lgaya h
car5 = ToyotaCar("Prius","Electric")
print(car5.type)   # Electric     

"""Instance = class ka real object
Jab hum class se object banate hain,usi object ko instance kehte hain.
Class ka jo actual copy/object memory me banta hai, wahi instance hota hai.
Real-Life Example
Class → Car ka design
Instance → Ek real Car (red Toyota, blue Honda)
Har instance:
Alag memory leta hai
Apna data rakhta hai
Value instance ke under store hoti h c1 = Car("Blue")"""

"""Class method -> A class method is bound to the the class and receives the class as an implicit first argument
Note -> Static method can't access or modify class state and generally for utility
 Class Method wo method hota hai jo object (instance) par nahi , class par kaam karta hai.
Isme:self ❌ nahi hota
cls ✅ hota hai (class ko refer karta hai) 
Class Method kyun use karte hain?
Class variable ko access / modify karne ke liye
Alternative constructor banane ke liye
Jab logic poori class se related ho, object se nahi
Class Method class ke data par kaam karta hai, object ke data par nahi.
self.__class__.variable ka use
Person.show_school() → direct class ke through call
Object banane ki zarurat nahi
cls automatically class ko refer karta hai
Agar object se call karo bhi, same kaam karega:
p = Person()
p.show_school()  # Output: ABC School
static methods -> jo class ya instance dono me se kisi bhi attribute ko change nhi krskte
class methods -> (cls as first implicit  argument) 
instance methods -> jo self leta h
"""

class Person:
    name = "Anonymous"
    # def changeName(self,name):
    #     # self.name = name # ye naya create ho gya h isne class attribute name ko change nhi keya h
    #     # Person.name = name 
    #     self.__class__.name = "Rahul"  # (self.__class__ -> Person class)self mtlb object jis object ki class ke under change krna chahte h uski class ko access  kr skte h
    #     # self .__class__
    #     # Person.name = "Rahul"
    @classmethod
    def changeName(cls,name):
        cls.name = name   #  class ke attribute me directly change hua h

p1 = Person()
p1.changeName("Rahul Kumar")   
# print(p1.name)   # Rahul Kumar  
print(p1.name)   # Rahul Kumar  ,Rahul 
# print(Person.name)   # Anonymous  
print(Person.name)   # (Rahul Kumar -> Person.name = name  ne change krdeya h ),Rahul


        

         




     











  
