print("Enter num1")
num1 = (input())
print("Enter num2")
num2 = (input())
try:
    print("The sum of num1 and num2 is:", 
         int( num1) + int(num2)) # This line may raise a ValueError if inputs are not valid integers
except Exception as e:
    print(e)
print("The program continues...")    # This line will execute even if there was an exception above
print("----------------------------------")  
# -----------------------------------------------------
a = (input("Enter a number: "))
print(f"Multiplication table of {a} is:")
try:
    for i in range(1,11):
        print(f"{int(a)} x {i} = {int(a)*i}")
except:
    print("Invalid input!")
print("Some imp lines of code.")
print("The program ends here.") 
print("----------------------------------")  
# ----------------------------------------------------

try:
    num = int(input("Enter a number: "))
    b =[3,4]
    print(b[num]) # This line may raise an IndexError if num is not 0 or 1
except ValueError:
    print("Number entered is not an integer.")    
except IndexError:
    print("Index out of range.")  
print("----------------------------------")      
# ----------------------------------------------------    


try:
    l = [1,4,5,9]
    i = int(input("Enter an index: "))
    print(l[i])
except:
    print(" Some error occurred.")  
finally:
    print(" I am always execute.") 
print("----------------------------------")    
# ----------------------------------------------------     

def fun1():
    try:
        l = [1,4,5,9]
        i = int(input("Enter an index: "))
        print(l[i])
        return 1
    except:
        print(" Some error occurred.") 
        return 0 

# print(" I am always execute.") #  ye nhi chalenga kyunki return ke baad finally block execute hota hai but print statement execute nahi hota hai. 
    finally:
        print(" I am always execute.")  # finally block will execute before the return statement is executed.
x = fun1() 
print(x)   # The value of x will be 1 if the user enters a valid index (0 to 3) and 0 if the user enters an invalid index or a non-integer input.
