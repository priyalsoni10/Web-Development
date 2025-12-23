# Function-> A block of reusable code that performs a specific task.
# Defining a function without parameters and without return statement
def greet(): #Function name followed by parentheses
    print("Hello, World!")  # Function body
    print("Welcome to Python programming.")
greet()    #Calling the function
#------------------------------------
 # Function with parameters and without return statement
def cal_sum(a, b):  # Function with parameters
    sum = a + b  # Function body
    print("The sum is:", sum)
    # return sum # Return statement
cal_sum(5, 10)  # Calling the function with arguments
#------------------------------------

# function defination with parameters and return statement
def multiply(x, y):  # Function with parameters
    return x*y  # Return statement
product = multiply(8,4)  # Calling the function with arguments
print("The product is:", product)  # Printing the returned value
print("The product is:", multiply(4,5))  # Printing the returned value
#------------------------------------
# Function with default parameters
def power(num, exponent=2):  # Function with default parameter
    return num ** exponent  # Return statement         
print("Power with default exponent:", power(5))  # Using default exponent(power of 2)
print("Power with custom exponent:", power(5, 3))  # Using custom exponent(power of 3)
#------------------------------------
# Average of three numbers using function
def cal_Avg(a,b,c):
    sum = a+b+c
    avg = sum/3
    # print("Calculating average inside the function", avg)
    return avg
result = cal_Avg(10,20,30)
print("The average is:", result)
print("Power result of average result is :",power(result))
print("Average of power result is : ",cal_Avg(power(2,3), power(3,2), power(4)))
print("Power result of average is:",power(cal_Avg(20 ,40 ,60)))
#------------------------------------
print("Hello") #  internally end= "\n" ho jata h 
print("World")
print("Hello", end=" ") # end parameter change kr skte h (with space) Hello World
print("World")
print("Hello", end=" @ ") # end parameter change kr skte h (with special character) Hello @ World
print("World")
print("Hello"," How","are", "you!", sep=" @ ") # sep parameter change kr skte h (with special character) Hello @ How @ are @ you!
#------------------------------------
# Function to calculate factorial of a number
def cal_factorial(n):
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    return factorial
num = 4
result = cal_factorial(num)
print(f"The factorial of {num} is: {result}")
# -------------------------------------
# Function to check if a number is prime
def is_prime(n):
    if(n <= 1):
        return False
    for i in range(2,(n//2) +1):
        if(n % i == 0):
            return False
    return True
num = 29    
if  is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is a composite number.")

# -------------------------------

def checkPrime(n):
    isPrime = True
    for i in range(2, (num//2)+1):
      if(num % i == 0):
        isPrime = False
        break
    if isPrime:
       print(f"{num} is a prime number.")
    else:
       print(f"{num} is Composite number.")   
num=15
checkPrime(num)
# -------------------------------
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)
num=5
result = factorial(num)
print(f"The factorial of {num} is: {result}")
# -------------------------------
# Len function using user-defined function
cities = ["Mumbai", "Indore", "Mandsaur", "Ratlam", "Ujjain"]
def list_length(cities):
    count = 0
    for city in cities:
        count += 1
    return count
length = list_length(cities)
print("The length of the cities list is:", length)
# -------------------------------
# Function to  print list in single line
def print_list_elements(elements):
    for element in elements:
        print(element, end=" ")
    print()  # For newline after printing all elements  
print_list_elements(cities)
# -------------------------------
# Function to find maximum in a list

def find_maximum(numbers):
    max =  numbers[0]
    for i in numbers:
        if i > max:
            max = i
    return max
num_list = [10, 25, 5, 75, 60, 45]
maximum = find_maximum(num_list)    
print("The maximum number in the list is:", maximum)
# -------------------------------
# Function to find minimum in a list
def find_minimum(numbers):  
    min = numbers[0]
    for i in numbers:
        if i < min:
            min = i
    return min
num_list = [10, 25, 5, 75, 60, 45]
minimum = find_minimum(num_list)
print("The minimum number in the list is:", minimum)
# -------------------------------
# Function to conver USD to INR
def usd_to_inr(usd):
    inr = usd * 83  # Assuming 1 USD = 82.74 INR
    return inr
amount_usd = 100
amount_inr = usd_to_inr(amount_usd)     
print(f"{amount_usd} USD is equal to {amount_inr} INR.")
# -------------------------------
# Function to  check even or odd
def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
number = int(input("Enter a number to check even or odd: "))
result = check_even_odd(number) 
print(f"{number} is {result}.")   
# ----------- END-------------------
# ----------- END-------------------
# Recursion in python->  Function calling itself repeatedly is called recursion.
# Print n to 1 backward using recursion
def show(n):
    if (n==0): # Base case
     return
    print(n)
    show(n-1)  # Recursive call
    print("END")
num=3
show(num) 
# -------------------------------

# Factorial using recursion   
def factorial_recursive(n):
    if n==0 or n==1:  # Base case
        return 1
    else:
        return n * factorial_recursive(n-1)  # Recursive call   
num=5
result = factorial_recursive(num)
print(f"The factorial of {num} using recursion is: {result}")
# -------------------------------
# Calculate the sum of first n natural numbers using recursion
def sum_natural_numbers(n):

    if (n==0): # Base case
        return 0
    elif n==1:
        return 1
    else:
        return n + sum_natural_numbers(n-1)  # Recursive call
num=5
# num = int(input("Enter a number to calculate sum of first n natural numbers: "))
result = sum_natural_numbers(num)
print(f"The sum of first {num} natural numbers using recursion is: {result}")
# -------------------------------
# Print all element in a list using recursion 
# Hint: use list and index as parameters
def print_list_recursive(list,index):
    if index>= len(list): # Base case
        return
    print(list[index], end=" " )
    print_list_recursive(list, index+1)  # Recursive call
cities = ["Mumbai", "Indore", "Mandsaur", "Ratlam", "Ujjain"]
print("\nPrinting list elements using recursion:")
print_list_recursive(cities, 0)
print()
# ----------- END-------------------
# ----------- END-------------------
# Modules in python-> A file containing Python code (functions, variables, classes) which can be imported and used in other Python files.
# Creating a module named 'math_operations.py' with basic math functions
# math_operations.py
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):     
    return a * b                
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."  
print(multiply(5, 10))     
# --------------------------------
# print(help("modules")) # List of available modules print kr dega
# print(help("math"))    # Math module ki help print kr dega
import math  # Importing the math module
print(math.e) # Printing the value of e -> 2.718281828459045(mathematical constant Euler's number)
print(math.pi) # Printing the value of pi -> 3.141592653589793(mathematical constant Pi)
#------------------------------- 
a= 10
def area_of_square(side):
    return side ** 2 # side * side 
def  calculator(x,y):
    print(f"Addition of {x , y} is : {x + y}")
    print(f"Substraction of {x , y} is : {x - y}")
    print(f"Multiplication of {x , y} is : {x * y}")
    print(f"Division  of {x , y} is : {x / y}")
 
#  User defined module -> jisme humne function lekha usko humne my_module name se save keya h to hum import my_module lekhenge
# import my_module as m # alias(short name) -> as m h
# print(my_module.a)
# print(m.area_of_square(4))
import FunctionInPython as fp
print(calculator(4,8))
print(fp.a)
print(fp.area_of_square(4))
# ------------------------------
# from FunctionInPython import calculator as c # import only specific things 
from FunctionInPython import calculator, a # import only specific things 
a,b = 4,8
sum = a+b
print(f"Sum of {a,b} is : {sum}")
print("Value of a is : ",a) # 4
# print("Value of a from another module is: " ,FunctionInPython.a ) # 10 jb chalega jb hum pura module import krenge
# c(5,8)
calculator(5,8)
#----------------------------
# Random module 
import random
b = random.randint(1,5) # koe bhi random number a skta h (1,5) ke beech or (1,5) bhi ho skte h
print(b)
print(random.randrange(1,3)) # 1 include hoga but 3 nhi 
print(random.random())  #  floating point number (0.0 to 1.0) but 1.0 not included 
print(random.uniform(1,3)) # (1,3) dono include ho skte h float value aege but range me dene ke leye uniform use krte h
l = [2,3,6,5,10,8,9]
print(random.choice(l)) # koe bhi number dega list me se
print(random.shuffle(l)) # None return krega only shuffle krega
print(l) # [6, 8, 5, 9, 2, 3, 10] shuffle krke deya h list ko 
