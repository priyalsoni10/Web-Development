#Check if a number is positive, negative, or zero.
# num= int(input("Enter a number:"))
# if(num<0):
#     print("Number is negative number!")
# elif(num==0):
#     print("Number is zero!")
# else:
#     print("Number is Positive Number!")
#---------------------END-----------------------------------
#---------------------END-----------------------------------

#Determine if a number is even or odd.
# num=int(input("Enter a number:"))
# if(num%2==0):
#     print("Number is even number!")
# else:
#     print("Number is odd number! ")
# ---------------------END-----------------------------------
# ---------------------END-----------------------------------

# # Check if a user is eligible to vote (age >= 18).
# age=int(input("Enter your age:"))
# if(age<17):
#     print("No, you cannot Vote!")
# elif(age==17):
#     print("Wait one or more year!")
# else:
#     print("Yes,You can Vote!")
# ---------------------END-----------------------------------
# ---------------------END-----------------------------------

# Find the larger of two numbers.
# a = int(input("Enter a 1st  number:"))
# b = int(input("Enter a 2nd number:"))
# if(a>b):
#     print("A is greater !")
# elif(a==b):
#     print("A is equal to B!")
# else:
#     print("B is greater!")
# ---------------------END-----------------------------------
# ---------------------END-----------------------------------

# Check if a number is divisible by 5.
# num = int(input("Enter a  number:"))
# if(num % 5==0):
#     print("Yes, the number is Divisible by 5!")
# else:
#     print("No, the number is Divisible not by 5!")
# ---------------------END-----------------------------------
# ---------------------END-----------------------------------
# Check if a character is a vowel or consonant.
# Char = input("Enter a Character:")
# if(Char=='a' or Char=='e' or Char=='i' or Char=='o' or Char=='u'):
#     print("Yes,Entered Character is Lower Case Vowel!")
# elif(Char=='A' or Char=='E' or Char=='I' or Char=='O' or Char=='U'):
#     print("Yes,Entered Character is Upper Case Vowel!")
# else:
#     print("Entered Character is Consonent!")
# ---------------------END-----------------------------------
# ---------------------END-----------------------------------

# Check if a person is a teenager (age between 13 and 19)
# Age=int(input("Enter the Age:"))
# if(13 <= Age <= 19):
#     print("Yes,This is teenager!")
# else:
#     print("No,This is not a teenager!")
# ---------------------END-----------------------------------
# ---------------------END-----------------------------------
# Check if a letter is uppercase, lowercase, or not a letter.
# Char = input("Enter a Character:")
# if(Char.isupper()):
#     print("Character is Upper Case letter!")
# elif(Char.islower()):
#     print("Character is Lower Case letter!")
# else:
#     print("Character is not a letter!")
# ---------------------END-----------------------------------
# ---------------------END-----------------------------------
# Assign a grade based on a student's score.
# 90+ → A
# 80-89 → B
# 70-79 → C
# 60-69 → D
# Below 60 → F
# marks= int(input("Enter marks:"))
# if(marks>=90):
#     print("The grade is A!")
# elif(80<=marks<=89):
#     print("The grade is B!")
# elif(70<=marks<=79):
#     print("The grade is C!")
# elif(60<=marks<=69):
#     print("The grade is D!")
# else:
#     print("Fail")
# ---------------------END-----------------------------------
# ---------------------END-----------------------------------
# Find the largest among three numbers.
# a=int(input("Enter a number:"))
# b=int(input("Enter a number:"))
# c=int(input("Enter a number:"))
# if(a>=b and a>=c):
#     print("A is greater!")
# elif(b>=a and b>=c):
#     print("B is greater!")
# elif(c>a and c>b):
#     print("C is greater!")
# else:
#   print("All are equal")
# --------------------END-------------------------------------
# ---------------------END-----------------------------------

# Print the corresponding season based on the entered month.
# month=input("Enter the Month name: ").capitalize()
# if(month == "December" or month== "January" or month== "February"):
#     print("This season is a Winter Season!")
# elif(month == "March" or month =="April"):
#     print("This season is a Spring  Season!")
# elif(month == "May" or month=="June" or month== "July"):
#     print("This season is a Summer Season!")
# elif(month == "August" or month=="September" ):
#     print("This season is a Rainy/Mansoon Season!")
# elif(month == "October" or month=="November" ):
#     print("This season is a Autumn Season!")
# else:
#     print("Invalid Season!")
# ---------------------END-----------------------------------
# ---------------------END-----------------------------------
# Check if a number is "Large" (>1000), "Medium" (100-1000), or "Small" (<100).
# num = int(input("Enter a number:"))
# if(num>1000):
#     print(f"Entered number {num} is a larger number!")
# elif(100<=num<=1000):
#     print(f"Entered number {num} is a Medium number!")
# elif(num<=100):
#     print(f"Entered number {num} is a Small number!")
# ---------------------END-----------------------------------
# ---------------------END-----------------------------------
# Determine a person's tax category based on income:
# ≤ 10,000 → No tax
# 10,001 - 30,000 → 10% tax
# 30,000 → 20% tax
# income=int(input("Enter the income:"))
# if(income<=10000):
#     print("No Tax!")
# elif(10001<=income<=30000):
#     print("10% Tax!")
# elif(income>=30000):
#     print("20% Tax!")
# else:
#     print("Invalid Input!")
#--------------------END-------------------------------------
# ---------------------END-----------------------------------
# Check if a number is divisible by both 3 and 5, or only one.
# num=int(input("Enter the number:"))
# if(num%3 == 0 ):
#     if(num%5==0):
#        print(f"{num} is divible by both 3 and 5 !")
#     else:
#         print(f"{num} is divisible by only 3!")
# elif(num%5==0):
#        print(f"{num} is divible by only  5 !")
# else:
#         print(f"{num} is not divisible by only 3 and 5!")
#--------------------END-------------------------------------
# ---------------------END-----------------------------------
# Check if a number is positive, and if positive, whether it's even or odd.
# num = int(input("Enter a number:"))
# if(num<0):
#     print(f"Entered number {num} is negative number!")
# elif(num==0):
#     print(f"Entered number {num} is zero!")
# elif(num>0):
#     if(num%2==0):
#        print(f"Entered number {num} is positive as well as even number! ")
#     else:
#         print(f"Entered number {num} is positive but odd number! ")
# else:
#     print("Invalid input!")
# Check if a year is a leap year using nested conditions.
# year = int(input("Enter a year : "))
# if(year % 4 == 0):
#     if(year % 100 == 0):
#         if(year % 400 == 0):
#             print(f"{year} is a leap year!")
#         else:
#              print(f"{year} is not a leap year!")
#     else:
#          print(f"{year} is  a leap year!")
# else:
#      print(f"{year} is not a leap year!")
# --------------------END-------------------------------------
# ---------------------END-----------------------------------
# # Determine a triangle type based on its sides (Equilateral, Isosceles, Scalene).
# a= int(input("Enter a side of a:"))
# b= int(input("Enter a side of b:"))
# c= int(input("Enter a side of c:"))
# if((a+b>c) and (a+c>b) and (b+c>a)):
#     if(a == b == c):
#         print("This triangle is an equilateral triangle!")
#     elif(a==b or a==c or b==c):
#         print("This triangle is an isosceles triangle !")
#     else:
#        print("This triangle is scalene triangle ! ")
# else:
#        print("The given sides are not in the form of valid triangle ! ")
# --------------------END-------------------------------------
# ---------------------END-----------------------------------
# Compare two numbers: If they are equal, print "Equal". If not, check if the larger is divisible by the smaller.
# num1 = int(input("Enter a number:"))
# num2 = int(input("Enter a number:"))
# if(num1==num2):
#     print(f"{num1} equal to {num2} !")
# else:
#    if(num1>num2):
#        if(num1%num2==0):
#           print(f" {num1} is divide by {num2}! ")
#        else:
#            print(f" {num1} is not divide by  {num2}! ")
#    else:
#        if(num2%num1==0):
#            print(f" {num2} is divide by  {num1}! ")
#        else:
#            print(f" {num2} is not divide by {num1} !")
       # --------------------END-------------------------------------
       # ---------------------END-----------------------------------
# If a  customer is an adult, check if they are also a senior citizen(age ≥ 60).
# age=int(input("Enter a age:"))
# if(age>=18):
#     print("Customer is an adult!")
#     if(age>=60):
#         print("This customer is also a senior citizen!")
#     else:
#         print("This customer is not a senior citizen!")
# else:
#    print("Customer is not an adult!")
# --------------------END-------------------------------------
# ---------------------END-----------------------------------
# Check if a number is divisible by 2, 3, or 5.
# num=int(input("Enter a number:"))
# if(num%2==0 and num%3==0 and num%5==0):
#     print(f"{num} is divisible by 2,3 and 5 ")
# else:
#     if(num%2==0 and num%3==0):
#         print(f"{num} is divisible by 2 and 3")
#     elif(num%2==0 and num%5==0):
#         print(f"{num} is divisible by 2 and 5")
#     elif(num%3==0 and num%5==0):
#         print(f"{num} is divisible by 3 and 5")
#     else:
#         if(num%2==0):
#            print(f"{num} is divisible by 2 only")
#         else:
#            if(num%3==0):
#               print(f"{num} is divisible by 3 only")
#            else:
#                if(num%5==0):
#                     print(f"{num} is  divisible by 5 only")

               # else:
               #      print(f"{num} is not divisible by 2, 3,5 ")
# ---------------------END-----------------------------------
# ---------------------END-----------------------------------
# Check if a student passed in all three subjects (Math, Science, English).
# Math = int(input("Enter maths marks:"))
# English = int(input("Enter english marks:"))
# Science = int(input("Enter Science marks:"))
# if(Math>=50 and English>=50 and Science>=50):
#     print("You Passed in all the Subject!")
# else:
#     if(Math>=50 and English>=50):
#         print("You pass in Maths and English  subject!")
#     elif(Math>=50 and Science>=50):
#         print("You pass in Math and Science  subject!")
#     elif(English>=50 and Science>=50):
#         print("You pass in English and Science subject")
#     elif(Math>=50):
#         print("You pass only in math!")
#
#     elif(English>=50):
#         print("You pass only in English!")
#
#     elif(Science>=50):
#         print("You pass only in Science!")
#
#     else:
#         print("You Fail! ")
# ---------------------END-----------------------------------
# ---------------------END-----------------------------------
# Check if a person qualifies for multiple discounts based on purchase amount.
# purchaseAmt=int(input("Enter the Purchase Amount:"))
# if(10000<=purchaseAmt<=25000):
#     print("You get 5% discount!")
# elif(26000<=purchaseAmt<=40000):
#     print("You get 10% discount!")
# elif(41000<=purchaseAmt<=50000):
#     print("You get 15% discount!")
# elif(purchaseAmt>50000):
#     print("You get 20% discount with free gift voucher worth 5000rs !")
# else:
#     print("No discount available. Try shopping more to unlock discounts!")
# ---------------------END-----------------------------------
# ---------------------END-----------------------------------

# Calculate bus fare based on age and distance traveled.
# distance=int(input("Enter a distance in km:"))
# if(distance<=10):
#     print("The bus fare is Rs.10!")
# elif( distance<=25):
#     print("The bus fare is Rs. 30!")
# elif(distance<=40):
#     print("The bus fare is Rs.50 !")
# elif(distance<=50):
#     print("The bus fare is Rs. 70!")
# else:
#     print("Invalid distance!")
# ---------------------END-----------------------------------
# ---------------------END-----------------------------------
# Check if a number is both even and divisible by 10
# num = int(input("Enter a number:"))
# if(num%2==0):
#     if(num%10==0):
#         print("The number is even and divisible by 10! ")
#     else:
#         print("The number is even but not divisible by 10! ")
# else:
#     print("The number is odd number! ")

#---------------------END-----------------------------------
# ---------------------END-----------------------------------
# Print numbers from 1 to 10.
# for i in range(1,11):
#     print(i)
# ---------------------END-----------------------------------
# ---------------------END-----------------------------------
# Print even numbers between 1 and 20.
# for i in range(0,21,2):
#     print(i)
# ---------------------END-----------------------------------
# ---------------------END-----------------------------------
# Find the sum of the first 10 natural numbers (1 to 10).
# sum=0
# for i in range(1,11):
#     sum+=i
#     # print(sum)
# print(f"Sum of first 10 natural number is: {sum}")
# ---------------------END-----------------------------------
# ---------------------END-----------------------------------
# Print the multiplication table of 5.
# n=5
# for i in range(1,11):
#     print(f"{n} x {i} = {n*i} ")
# ---------------------END-----------------------------------
# ---------------------END-----------------------------------
# Print the first 10 odd numbers.
# for i in range(1,21,2):
#     print(i)
#---------------------END-----------------------------------
# ---------------------END-----------------------------------
# Reverse counting from 10 to 1.
# for i in range(10,0,-1) :
#     print(i)
#---------------------END-----------------------------------
# ---------------------END-----------------------------------
# Iterate through a list and print each element.
# list=["Apple" ,"Grapes","Pineapple","Banana"]
# for i in list:
#     print(i)
#---------------------END-----------------------------------
# ---------------------END-----------------------------------
# Find the sum of elements in a list.
# List=[1,4,7,10,12]
# Sum=0
# for i in List:
#     Sum+=i
# print("Sum of List element is:" ,Sum)
#---------------------END-----------------------------------
# ---------------------END-----------------------------------
#Find the factorial of a number using a for loop.
# num=int(input("Enter a number:"))
# fact=1
# for i in range(1,num+1):
#     fact=fact*i
# print(f"factorial of given number {num} is: {fact}")
# ---------------------END-----------------------------------
# ---------------------END-----------------------------------
# Print whether each number from 1 to 20 is even or odd.
# for i in range(1,21):
#     if(i%2==0):
#         print(f"{i} is even!")
#     else:
#         print(f"{i} is odd!")
# ---------------------END-----------------------------------
# ---------------------END-----------------------------------
# Check prime numbers between 1 and 50.
# for num in range(2,51):
#    isPrime = True
#    for i in range(2,(num//2)+1):
#        if(num%i==0):
#          isPrime=False
#          break
#    if isPrime:
#     print(num)
# ---------------------END-----------------------------------
# ---------------------END-----------------------------------
# # Count vowels and consonants in a string.
# String=input("Enter a string:").lower()
# countVowels=0
# countConsonent=0
# for ch in String:
#     ascii_value =ord(ch)
#     if(97<=ascii_value<=122):
#          if ascii_value in [97, 101, 105, 111, 117]:
#              countVowels+=1
#          else:
#              countConsonent+=1
# print(f"Number of vowels in given string is:{countVowels} ")
# print(f"Number of Consonent in given string is :{countConsonent} ")
# ---------------------END-----------------------------------
# ---------------------END-----------------------------------
# Identify the character is uppercase or lower case
# Character = input("Enter the character:")
# ascii_value=ord(Character)
# if(97<=ascii_value<=122):
#     print(f"The given character {Character} which ascii value is  {ascii_value} is lower case!")
# elif(65<=ascii_value<=90):
#     print(f"The given character {Character} which ascii value is  {ascii_value} is Upper case!")
# else:
#     print(f"The given character {Character} which ascii value is {ascii_value} is Special character!")
# ---------------------END-----------------------------------
# ---------------------END-----------------------------------
# Find numbers between 1 and 100 that are divisible by 7.
# for i in range(1,101):
#     if(i%7==0):
#         print(i)
# ---------------------END-----------------------------------
# ---------------------END-----------------------------------
#Check if words in a list are palindromes.
# words = ["madam", "hello", "level", "python", "radar"]
# for word in words:
#     if word == word[::-1]:#  reverse the string
#         print(f"Given word {word} is a palindrome!")
#     else:
#         print(f"Given word {word} is not  a palindrome!")
# ---------------------END-----------------------------------
# ---------------------END-----------------------------------
# Day Mathing
# day = 5
# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thrusday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")
#     case _:
#         print("Invalid")
# ---------------------END-----------------------------------
# ---------------------END-----------------------------------
# User greeting
# userSaid = "Good Afternoon"
# match  userSaid:
#     case "Good Morning":
#         print("Good Morning Sir")
#
#     case "Good Afternoon":
#         print("Good Afternoon Sir")
#     case "Good Evening":
#         print("Good Evening Sir")
#     case _:
#         print("Invalid")
# ---------------------END-----------------------------------
# ---------------------END-----------------------------------
# Table
# b = int(input("Enter a number:"))
# a=1
# while(a<=10):
#     # print("Hii")
#     print(b,"x" ,a,"=" ,b*a)
#     a += 1
# ---------------------END-----------------------------------
# ---------------------END-----------------------------------
# Print the number between 5 to 500
# a=5
# while(a<=500):
#     print(a)
#     a+=5
# ---------------------END-----------------------------------
# ---------------------END-----------------------------------
# Print the number between 5 to 500
# a=500
# while a>=5:
#     print(a)
#     a = a-5
# ---------------------END-----------------------------------
# ---------------------END-----------------------------------
# Print the number between 1 to 10
# for i in range(1,11):
#     print(i)
# ---------------------END-----------------------------------
# ---------------------END-----------------------------------
# Print 1 t0 10 value with step value
# for i in range(1,11,2):
#     print(i)
# ---------------------END-----------------------------------
# ---------------------END-----------------------------------
# Print reverse number with step value
# for i in range(11,0,-2) :
#     print(i)
# for i in range(10,-1,-1): # 10 se -1 tak bola h to 0 tk chalega
#     print(i)
# ---------------------END-----------------------------------
# ---------------------END-----------------------------------
# Print 500 to -500
# for i in range(500,-501,-1):
#   print(i)
# for i in range(-50 ,-71,-1):
#     print(i)
# ---------------------END-----------------------------------
# ---------------------END-----------------------------------
# Print 5 to 500
# start = 5
# end = 500
# for i in range(start ,end+1):
#     print(i)
 # ---------------------END-----------------------------------
# ---------------------END-----------------------------------
# start = int(input("Enter a start number:"))
# end = int(input("Enter a end number:"))
# if(start>end):
#     for i in range(start,end-1,-1):
#         print(i)
# else:
#     for i in range(start,end+1):
#             print(i)
# ---------------------END-----------------------------------
# ---------------------END-----------------------------------
#Print factor of given number
# num = int(input("Enter a number:"))
# for i in range(2,num):
#     if(num % i==0):
#         print(i)
# ---------------------END-----------------------------------
# ---------------------END-----------------------------------
#Print factor of given number
# num = int(input("Enter a number:"))
# count = 0
# for i in range(2,num):
#     if(num % i==0):
#         # print(i)
#        count+=1
# # print(f"Count of factor of given number {num} is:{count} ")
# # ---------------------END-----------------------------------
# # ---------------------END-----------------------------------
# # Print factor of given number with prime number also
# num = int(input("Enter a number:"))
# count = 0
# for i in range(2,(num//2)+1):
#     if(num % i==0):
#         # print(i)
#        count+=1
# # print(f"Count of factor of given number {num} is:{count} ")
# if(count==0): # prime number
#     print(f"{num} is prime number!")
# else:
#     print(f"{num} is composite number!")
# ---------------------END-----------------------------------
# ---------------------END-----------------------------------
# Print factor of given number with prime number also
# num = int(input("Enter a number:"))
# count = 0
# for i in range(2,(num//2)+1):
#     if(num % i==0):
#         # print(i)
#        count+=1
#        break
# # print(f"Count of factor of given number {num} is:{count} ")
# if(count==0): # prime number
#     print(f"{num} is prime number!")
# else:
#     print(f"{num} is composite number!")
# ---------------------END-----------------------------------
# ---------------------END-----------------------------------
# Termination concept (break)
# for i in range(1,100):
#     if(i==55):# 54 tk chalega
#         break
#     print(i)
# Reverse break and maximum factor
# n=45
# for i in range( n//2,2,-1):
#     if(n%i==0):
#         print(f"Maximum factor of {n} is : {i}")
#         break

# ---------------------END-----------------------------------
# ---------------------END-----------------------------------
# for i in range(1,100):
#     if(i==55):
#         continue
#     print(i)

# Skip 55 56 57 58
# for i in range(1,100):
#     if(i>=55 and i<=58):
#         continue
#     print(i)
# Skip
# for i in range(1,100):
#     if(i<=55 and i>=58):
#         continue
#     print(i)
#---------------------END-----------------------------------
# ---------------------END-----------------------------------
# # Print the smallest factor
# num=int(input("Enter a number:"))
# for i in range(2,num):
#     if(num%i==0):
#        print(i)
#        break
# Print the smallest factor
# num = int(input("Enter a number:"))
# max = num
# for i in range(2,num):
#     if(num%i==0):
#       max = i
# print(f"Maximum factor of {num} is :{max}")
#---------------------END-----------------------------------
# ---------------------END-----------------------------------
# Print Common Factor of the given number
# n1=int(input("Enter a number:"))
# n2=int(input("Enter a number:"))
# min = n2
# if(n1 < n2):
#     min = n1
# # else:
# #     min = n2
# for i in range(2,min+1):
#     if((n1 % i == 0) and (n2 % i == 0)):
#         print(i)
#---------------------END-----------------------------------
# ---------------------END-----------------------------------
# Print Common Factor of the given number
# n1=int(input("Enter a number:"))
# n2=int(input("Enter a number:"))
# min = n2
# if(n1 < n2):
#     min = n1
# HCF=1
# for i in range(2,min+1):
#     if((n1 % i == 0) and (n2 % i == 0)):
#         HCF = i
# print(HCF)
#---------------------END-----------------------------------
# ---------------------END-----------------------------------
# # Print Square of the given range
# start=int(input("Enter the number:"))
# end=int(input("Enter the number:"))
# for i in range(start,end+1):
#     square = i*i
#     print(f"Square of {i} is:{square}")
#     i += 1
#---------------------END-----------------------------------
# ---------------------END-----------------------------------
# # Print the cube of that which is divisible by 7  between 5 to 210
# for i in range(5,211):
#     if(i%7==0):
#         cube = i*i*i
#         print(f"Cube of {i} is : {cube}")
#---------------------END-----------------------------------
# ---------------------END-----------------------------------
# Reverse numbers
# num = int(input("Enter a number:"))
# # sum = 0
# # while(num>0):
# #     rem = num%10
# #     sum = sum*10 + rem
# #     num = num//10
# # print(sum)ii81
#---------------------END-----------------------------------
# ---------------------END-----------------------------------
# Sum of range
# sum = 0
# for i in range(1,6):
#    sum+=i
#    print(sum)
# print(f"Sum of range is :{sum}")
#---------------------END-----------------------------------
# ---------------------END-----------------------------------
# Count of reverse number
# n=345
# count=0
# while(n>0):
#    n=n//10
#    count+=1
# # print(n)
# print(f"Count of number is:{count} ")
#---------------------END-----------------------------------
# ---------------------END-----------------------------------
# Sum of number
# n = int(input("Enter a number:"))
# sum = 0
# while(n > 0):
#    r = n % 10
#    sum += r
#    n = n // 10
# print(f"Sum of given number {n} is :{Sum}")
#---------------------END-----------------------------------
# ---------------------END-----------------------------------
# Reverse number
# n = int(input("Enter a number:"))
# rem = 0
# rev = 0
# while(n > 0):
#     rem = n % 10
#     rev = rev * 10  + rem
#     n = n//10
#     print(rev)
# print(f"Reverse of given number {n} is : {rev} ")
#---------------------END-----------------------------------
# ---------------------END-----------------------------------
# Check number is a palindrome or not
# n = int(input("Enter a number:"))
# rem = 0
# rev = 0
# temp = n
# while(n > 0):
#     rem = n % 10
#     rev = rev * 10 + rem
#     n = n//10
# if(temp == rev):
#     print(f"Given number {temp} is palindrome!")
# else:
#     print(f"Given number {temp} is not palindrome!")
#---------------------END-----------------------------------
# ---------------------END----------------------------------
# End  And Seperator(sep) operator
# End Operator
# for i in range(6):
#     print("Hi ",end="")
#     print("Good Mornings y a")
# # Seperator Opertor
# for i in range(6):
#         wsw2print("Hi" ,"There",sep="!")
# #     print(f"Given number {temp} is not palindrome!")
#---------------------END-----------------------------------
# ---------------------END----------------------------------
# Pattern using nested loop
# for i in range(10):
#     for j in range(5):
#         print("**",end="")
#     print()
#---------------------END-----------------------------------
# ---------------------END----------------------------------
# Table
# for i in range(2,21):
#     for j in range(1,11):
#         print(f"{i} x {j} = {i * j}")
#     print("--------End j one round----------")
# ---------------------END-----------------------------------
# ---------------------END----------------------------------
# Pattern 1
# n = 5
# for i in range(n):
#     print("* " ,end="")
# print()
# Pattern 2
# n=5
# for i in range(n):
#     for j in range(n):
#         print("* ",end="")
#     print()
# Pattern 3
# n=5
# for i in range(n):
#     for j in range(0,i):# phlr bar i= 0 h to first timr blank print hoga(None)
#         print("* ",end="")
#     print()
# Pattern 4
# n=5
# # for i in range(n):
# #     for j in range(0,i+1):
# #         print("* ",end="")
# #     print()
# Pattern 5
# n = 5
# for i in range(n):
#     for j in range(i,n):
#          print("* " ,end="")
#     print()
#Pattern 6
# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print("* ",end="")
#     print()
# for i in range(n):
#     for j in range(i,n):
#          print("* " ,end="")
#     print()
# Pattern 7
# n = 5
# for i in range(n):
#     for j in range(i,n):
#         print("* ",end="")
#     print()
# for i in range(n):4eij
#     for j in range(i+1):
#          print("* " ,end="")
#     print()
# Pattern 8
# n = 5
# for i in range(n-1):
#     for j in range(i+1):
#         print("* ",end="")
#     print()
# for i in range(n):
#     for j in range(i,n):
#          print("* " ,end="")
#     print()
#Pattern 8
# n = 5
# for i in range(n):
#     for j in range(n):
#         print("* ",end="")
#     for k in range(n):
#            print("# ",end="")
#     print()
# #Pattern 8
# n = 5
# for i in range(n):
#     for j in range(i,n):
#         print("- ",end="")
#     for k in range(n):
#            print("* ",end="")
#     print()
# # #Pattern 8 : lIKE RHOMBUS
# n = 5
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end="")
#     for k in range(n):
#            print("* ",end="")
#     print()
# #Pattern 8 # triangle
# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end="")
#     for k in range(n):
#            print("* ",end="")
#     print()
# #Pattern 9
# n = 5
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end="")
#     for k in range(n):
#            print("* ",end="")
#     print()
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end="")
#     for k in range(n):
#            print("* ",end="")
#     print()
#Pattern 10
# n = 5
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end="")
#     for k in range(i+1):
#            print("* ",end="")
#     print()
#Pattern 10
# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end="")
#     for k in range(i,n):
#            print("* ",end="")
#     print()
# Pattern 11 # Diamond
# n = 5
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end="")
#     for k in range(i+1):
#            print("* ",end="")
#     print()
# for i in range(n):
#    for j in range(i+1):
#         print(" ",end="")
#    for k in range(i,n):
#            print("* ",end="")
#    print()
# Pattern 12 damru like structure
# n=5
# for i in range(n):
#    for j in range(i+1):
#         print(" ",end="")
#    for k in range(i,n):
#            print("* ",end="")
#    print()
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end="")
#     for k in range(i+1):
#            print("* ",end="")
#     print()
# Pattern 13 Frame
# n = 15
# for i in range(n):
#     for j in range(n):
#         if i == 0 or j == 0 or i == n-1 or j == n-1: # (i == 0 → top border , i == n-1 → bottom border ,j == 0 → left border , j == n-1 → right border)
#             print("* ",end="")
#         else:
#             print("  " ,end="")
#     print()
# Pattern 14
# n = 15
# for i in range(n):
#     for j in range(n):
#         if i == 0 or j == 0 or i == n-1 or j == n-1:
#             print("* ",end="")
#         else:
#             print("  " ,end="")
#     print()
# Pattern 15
# Pattern printing: X shape inside a square border
# n = 11  # total rows (and columns)
#
# for i in range(n):  # outer loop -> rows
#     for j in range(n):  # inner loop -> columns
#
#         # 1️⃣ Border print karne ke liye condition
#         if i == 0 or i == n - 1 or j == 0 or j == n - 1:
#             print("*", end=" ")
#
#         # 2️⃣ Left se right diagonal (i == j)
#         elif i == j:
#             print("*", end=" ")
#
#         # 3️⃣ Right se left diagonal (i + j == n - 1)
#         elif i + j == n - 1:
#             print("*", end=" ")
#
#         # 4️⃣ Baaki jagah blank space
#         else:
#             print(" ", end=" ")
#
#     # Ek row complete hone ke baad new line
#     print()
# ss
# n = 11
# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n-1 or j == 0 or j == n-1 or i == j or i + j == n - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


#---------------------END-----------------------------------
# ---------------------END-----------------------------------

#List
# l= [1,2,3,4,6,5,9,87,5] # mutable data structure
# print(l)
# print(l[2]) # 3
# print(len(l)) # 9
# for i in range(len(l)):
#     # print(l[i])
#     print(l[i])
#
# l2 = list(range(1,11))
# print(l2)
#
# l3 =[3,34,5,6,7,33,5,7]
# for i in l3:
#     print(i)
# for i in range(len(l3)):
#     print(i,l[i]) #  list with index number
#  Check whether the given list number is prime or composite
# a =[12,34,56,45,76,65,78,22,13,11,2,10,8, 19 ,31,23,5,7,3 ,87]
# b=[]
# c=[]
# for i in range(len(a)):
#     num = a[i]
#     isPrime = True
#     if (num < 2):
#         c.append(num)
#         continue
#     for j in range(2,(num//2)+1):
#         if(num % j == 0):
#           isPrime =False
#           break
#     if(isPrime):
#         b.append(num)
#     else:
#         c.append(num)
# b.sort()
# c.sort()
# print(f"Original List : {a}")
# print(f"Prime Number List : {b}")
# print(f"Composite Number List : {c}")
#---------------------END-----------------------------------
# ---------------------END-----------------------------------

# List -> List follow Sequence and support different  datatype .it is mutable mean that it can be change after creation
# roll_no = [1,2,3,4,5] # duplicate value are allowed
# name = ["Ram","Shyam","Sita","Geeta"]
# mix_list = [1,"Abc",True,1.1] #  mix list ko sort krna impossible h
# num =[2,6,4,9,3,1,0,7,4,56,84,33,99,22,39,12,15,12]
# print(roll_no[2]) # 3
# print(name[1]) # Shyam
# print(mix_list[3]) #  1.1
# print(f"Length of list is: {len(mix_list)}") #length of list (Length of list is: 4)
# print(roll_no[0:5]) #[1, 2, 3, 4, 5]
# print(roll_no[:]) # by default [0:5] aaega starting and ending value [1, 2, 3, 4, 5]
# print(roll_no[1:3]) #[2, 3]
# print(roll_no[3:]) #[4, 5]
# print(roll_no[0:3:1]) #[1, 2, 3] nothing  skip the value
# print(roll_no[0:5:2]) #[1, 3, 5] skip 1 value
# print(roll_no[0::3]) #[1, 4]skip 2 value
# print(num.sort()) # return none  krega kyoki sorted koe value return nhi krta
# num.sort()
# print(num) # [0, 1, 2, 3, 4, 4, 6, 7, 9, 12, 12, 15, 22, 33, 39, 56, 84, 99]
# print(sorted(num))# [0, 1, 2, 3, 4, 4, 6, 7, 9, 12, 12, 15, 22, 33, 39, 56, 84, 99]
# print(num.reverse())
# num.reverse()
# print(num) #[99, 84, 56, 39, 33, 22, 15, 12, 12, 9, 7, 6, 4, 4, 3, 2, 1, 0]
# print(list(reversed(num))) #[99, 84, 56, 39, 33, 22, 15, 12, 12, 9, 7, 6, 4, 4, 3, 2, 1, 0]
# print(num[::-1]) #[99, 84, 56, 39, 33, 22, 15, 12, 12, 9, 7, 6, 4, 4, 3, 2, 1, 0]
# print(min(num)) # 0
# print(max(num)) # 99
# num.append(45) #[0, 1, 2, 3, 4, 4, 6, 7, 9, 12, 12, 15, 22, 33, 39, 56, 84, 99, 45]
# print(num)
# num.insert(6,18) # insert or append me ek time pr ek hi value dee skte h or extend me puri list bhi de skte h
# print(num)#[0, 1, 2, 3, 4, 4, 18, 6, 7, 9, 12, 12, 15, 22, 33, 39, 56, 84, 99, 45]
# num.extend([85,7])
# print(num) # [0, 1, 2, 3, 4, 4, 18, 6, 7, 9, 12, 12, 15, 22, 33, 39, 56, 84, 99, 45, 85, 7] extend at the end of the list
# num[6] = 5
# print(num) #[0, 1, 2, 3, 4, 4, 5, 6, 7, 9, 12, 12, 15, 22, 33, 39, 56, 84, 99, 45, 85, 7]
# num[8:12] = [8,9,10,11,12]
# print(num)# [0, 1, 2, 3, 4, 4, 5, 6, 8, 9, 10, 11, 12, 15, 22, 33, 39, 56, 84, 99, 45, 85, 7]
# num.remove(4) # first occurence of that element
# print(num) #[0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 15, 22, 33, 39, 56, 84, 99, 45, 85, 7]
# print(num.pop()) #7
# print(num.pop(16)) # 56
# print(num.count(22)) # 1 times
# num1 = num.copy()
# print(num1) #[0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 15, 22, 33, 39, 84, 99, 45, 85]
# print(num.index(10)) # 9
# print(num.clear())# None list ko pure delete kr deta h
# marks = [3,5,6 ,"Abc",True]
# print(marks)
# print(marks[0]) # 3
# print(type(marks))
# print(marks[-3])# negative index -> 6
# print(marks[len(marks)-3]) # 6
# print(marks[5-3])   # 6
# print(marks[2])  # 6
# if 7 in marks: #No
#     print("Yes")
# else:
#     print("No")
# if "Abc" in marks: # yes
#     print("Yes")
# else:
#     print("No")
#
# if "7" in marks: # No
#     print("Yes")
# else:
#     print("No")
#
# if "bc" in "Abc": # Yes
#     print("Yes")
# else:
#     print("No")
# print(marks[:]) #[3, 5,6, 'Abc', True]
# print(marks[1:]) #  [5, 6, 'Abc', True]
# print(marks[1:-1])   # [5, 6, 'Abc'] not  include -1
# print(marks[1:4])   # [5, 6, 'Abc'] not  include 4 (5-1)
# print(marks[1:4:2])   # [5, 'Abc']
# print(marks[::-1])   # [True, 'Abc', 6, 5, 3] reverse list

# List comprehension
# l = [i for i in range(6)]
# print(l) # [0, 1, 2, 3, 4, 5]
# l = [i*i for i in range(6)]
# print(l) # [0, 1, 4, 9, 16, 25]
# l = [i*i for i in range(10) if i%2 == 0]
# print(l) # [0, 4, 16,8 36, 64]
# marks = [20,30,40,50,60]
# new_marks=[]
# for i in marks:
#     new_marks.append(i+2)
# print(new_marks) #[22, 32, 42, 52, 62]
#
# marks = [20,30,40,50,60]
# new_marks = [i+2 for i in marks]
# print(new_marks) #[22, 32, 42, 52, 62]
# cubes = []
# for i in range(11):
#     if(i%2==0):
#         cubes.append(i**3)
# print("Cubes of given number Using Loop is:" ,cubes) #Cubes of given number is: [0, 8, 64, 216, 512, 1000]
#
# cubes = [i**3 for i in range(10) if i % 2==0]
# print("Cubes of given number Using List Comprehension is: ",cubes) #zCubes of given number Using List Comprehension is:  [0, 8, 64, 216, 512]
#
#  #List Method
# l = [11,2,43,14,5]
# print(l)
# l.append(6)
# print(l) #[11, 2, 43, 14, 5, 6]
# l.sort()
# print(l) #[2, 5, 6, 11, 14, 43]
# l.reverse()
# print(l)  #[43, 14, 11, 6, 5, 2]
# print(l.index(11)) # 2 return the first occurrence of list item
# print(l.count(11)) # 1
#
# m=l
# m[0] = 0
# print(l) #[0, 14, 11, 6, 5, 2] original list me change ho jaaega
# m=l.copy()
# m[0] =10
# print(l) #[0, 14, 11, 6, 5, 2] original list
# print(m) #[10, 14, 11, 6, 5, 2] only copy and modify item in m
# l.insert(3,8)
# print(l) #[0, 14, 11, 8, 6, 5, 2]
# m=[900,1000,1100]
# l.extend(m)
# print(l) #[0, 14, 11, 8, 6, 5, 2, 900, 1000, 1100]
# k = l + m
# print(k) #[0, 14, 11, 8, 6, 5, 2, 900, 1000, 1100, 900, 1000, 1100]
#---------------------END-----------------------------------
# ---------------------END-----------------------------------
#
# #Tuples
# tup =(4,7,3 ,"Abc",True)
# print(tup) #(4, 7, 3) it does not change immutable
# print(type(tup)) # <class 'tuple'>
# tup=(1) #int
# tup=(1,) #tuple
# print(type(tup))  #<class 'tuple'>
# tuple = (2,5,7,4,9,5,4)
# print(tuple[2]) # 7
# if 7 in tuple: #yes
#     print("yes")
# else:
#     print("No")
# print(tuple[1:4]) #(5, 7, 4) ek new tuple return hua h existing tuple me koe change nhi hua h
# tup2= tuple[2:5]
# print(tup2) #(7, 4, 9) return new tuple
# print(tuple[-4:-1:2]) #(4, 5)
# print(tuple[:-1]) #(2, 5, 7, 4, 9, 5) not include -1
# print(tuple[::-1]) #(4, 5, 9, 4, 7, 5, 2) reverse tuple

countries =("Spain","Italy","India","England","Germany")
temp = list(countries) # change in list
print(temp) #['Spain', 'Italy', 'India', 'England', 'Germany']
temp.append("Russia") # append in list
temp.pop(2) # remove item in a list (India)
temp[2]="Greece" # change item
countries = tuple(temp) #change in tuple  ('Spain', 'Italy', 'Greece', 'Germany', 'Russia')
print(countries)

Countries1= ("Pakistan","Afghanistan","Bangladesh","SriLanka")
Countries2= ("Vietnam","India","China")
southEastAsia=Countries1+Countries2
print(southEastAsia)

tup1 = (1,9,7,5,9,4,7,3,9,6,5,2)
res =tup1.count(9)
print("Count of 9 in tuple is :",res) #Count of 9 in tuple is : 3
res = tup1.index(5)
print(res) # 3 index
print(tup1.index(9,5,10)) # 8 index internally phlee slicing hoti h fir value find  hoti h [5:10]index ke bech me 3 find krenge(value jo find krna h vo,start value jha se find krna start krna h vo , end value jha tak krna h vo)
print(tup1[-6])  # 7
print(tup1[2:-4]) #(7, 5, 9, 4, 7, 3)
print(tup1[5:1:-1]) # (4, 9, 5, 7)
print(len(tup1)) # 12
tup2= (4,7,8,10,16,75,65)
tup3=(tup1,tup2) # nested tuple
print(tup3) #((1, 9, 7, 5, 9, 4, 7, 3, 9, 6, 5, 2), (4, 7, 8, 10, 16, 75, 65))
print(min(tup1)) # min = 1
print(max(tup2)) # max = 75
lst = [3,6,8,"Abc",True]
print(lst) #[3, 6, 8, 'Abc', True]
print(tuple(lst)) #  (3, 6, 8, 'Abc', True)
tup4=(10,)*8
print(tup4) #(10, 10, 10, 10, 10, 10, 10, 10)
#---------------------END-----------------------------------
# ---------------------END-----------------------------------
 
#  Dictionary
# Python me Dictionary ek data structure hota hai jo data ko key : value pairs me store karta hai.
chai_types = {"Masala Chai": 50,
              "Ginger Chai": 40,
              "Lemon Chai": 45,
              "Elaichi Chai": 60,
              "Green Tea": 70
              }
print(chai_types) # {'Masala Chai': 50, 'Ginger Chai': 40, 'Lemon Chai': 45, 'Elaichi Chai': 60, 'Green Tea': 70}
print(type(chai_types)) # <class 'dict'>
print(chai_types["Lemon Chai"]) # 45
chai_types["Black Tea"] = 55 # add new item
print(chai_types) # {'Masala Chai': 50, 'Ginger Chai': 40, 'Lemon Chai': 45, 'Elaichi Chai': 60, 'Green Tea': 70, 'Black Tea': 55}
chai_types["Ginger Chai"] = 42 # update existing item
print(chai_types) # {'Masala Chai': 50, 'Ginger Chai': 42, 'Lemon Chai': 45, 'Elaichi Chai': 60, 'Green Tea': 70, 'Black Tea': 55}
del chai_types["Elaichi Chai"] # delete item
print(chai_types) # {'Masala Chai': 50, 'Ginger Chai': 42, 'Lemon Chai': 45, 'Green Tea': 70, 'Black Tea': 55}
print(len(chai_types)) # 5
print(chai_types.get("Elaichi Chai") ) # None# key not found
print(chai_types.get("Masala Chai")) # 50 # key found
for chai in chai_types:
    print(chai) # print all key
print("------------------")    
for chai in chai_types:    
     print(chai, chai_types[chai]) # print key with value
print("------------------")
for chai, price in chai_types.items():
    print(chai, price) # print key with value using items()
print("------------------")
for key, value in chai_types.items():
    print(key, value) # print key with value using items()
print("------------------")   
print(chai_types.keys()) # dict_keys(['Masala Chai', 'Ginger Chai', 'Lemon Chai', 'Green Tea', 'Black Tea'])
print(chai_types.values()) # dict_values([50, 42, 45, 70, 55]) 
print(chai_types.items()) # dict_items([('Masala Chai', 50), ('Ginger Chai', 42), ('Lemon Chai', 45), ('Green Tea', 70), ('Black Tea', 55)])                                                                                                                                                        
if "Green Tea" in chai_types:
    print("Yes ,I have") # Yes
print("-----------------")
if "Masala Tea" in chai_types:
    print("No ,I haven't ") # ye kuch bhi print nhi krega kyoki key exist nhi krti h 
print("-----------------")    
chai_types['Earl Grey'] = 80 # add new item
print(chai_types) # {'Masala Chai': 50, 'Ginger Chai': 42, 'Lemon Chai': 45, 'Green Tea': 70, 'Black Tea': 55, 'Earl Grey': 80}      
chai_types.update({"Oolong Tea": 90}) # add new item using update()
print(chai_types) # {'Masala Chai': 50, 'Ginger Chai': 42, 'Lemon Chai': 45, 'Green Tea': 70, 'Black Tea': 55, 'Earl Grey': 80, 'Oolong Tea': 90}
chai_types.pop("Black Tea") # remove item using pop()
print(chai_types) # {'Masala Chai': 50, 'Ginger Chai': 42, 'Lemon Chai': 45, 'Green Tea': 70, 'Earl Grey': 80, 'Oolong Tea': 90}
print(chai_types.popitem()) # ('Oolong Tea', 90) remove last item using popitem()
print(chai_types) # {'Masala Chai': 50, 'Ginger Chai': 42, 'Lemon Chai': 45, 'Green Tea': 70, 'Earl Grey': 80}
del chai_types['Earl Grey'] # delete item using del
print(chai_types) # {'Masala Chai': 50, 'Ginger Chai': 42, 'Lemon Chai': 45, 'Green Tea': 70}
chai_types_copy = chai_types.copy() # copy dictionary
print(chai_types_copy) # {'Masala Chai': 50, 'Ginger Chai': 42, 'Lemon Chai': 45, 'Green Tea': 70}
chai_types_copy.clear() # clear dictionary
print(chai_types_copy) # {} empty dictionary
print(chai_types) # original dictionary remains unchanged {'Masala Chai': 50, 'Ginger Chai': 42, 'Lemon Chai': 45, 'Green Tea': 70}
print("-----------------") 
tea_shop = {
         "chai" : {
               "Masala Chai": "Spicy and Sweet",
                "Ginger Chai": "Strong and Zesty",
                "Elaichi Chai": "Aromatic and Flavorful",      

           },
           "tea": {
               "Green Tea": "Light and Healthy",
               "Black Tea": "Bold and Robust",
               "Oolong Tea": "Smooth and Complex",
              }

} 
print(tea_shop)
print(tea_shop["chai"])# {'Masala Chai': 'Spicy and Sweet', 'Ginger Chai': 'Strong and Zesty', 'Elaichi Chai': 'Aromatic and Flavorful'}
print(tea_shop["tea"]["Oolong Tea"]) # Smooth and Complex
print(tea_shop["chai"]["Masala Chai"]) # Spicy and Sweet
print("-----------------")
squared_num = {i: i**2 for i in range(6)}
print(squared_num) # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
even_squared_num = {i: i**2 for i in range(11) if i % 2 == 0} # even numbers only
print(even_squared_num) # {0: 0, 2: 4,    4: 16, 6: 36, 8: 64, 10: 100} 
even_squared_num.clear()
print(even_squared_num) # {} empty dictionary3
print("-----------------")
keys= ["Masala Chai", "Ginger Chai", "Chocolate Chai"]
print(keys)# ['Masala Chai', 'Ginger Chai', 'Chocolate Chai']
default_value = "Delicious"
new_chai_dict = dict.fromkeys(keys, default_value)
new_chai_dict1 = dict.fromkeys(keys, keys)

print(new_chai_dict) # {'Masala Chai': 'Delicious', 'Ginger Chai': 'Delicious', 'Chocolate Chai': 'Delicious'}
print(new_chai_dict1) # {'Masala Chai': ['Masala Chai', 'Ginger Chai', 'Chocolate Chai'], 'Ginger Chai': ['Masala Chai', 'Ginger Chai', 'Chocolate Chai'], 'Chocolate Chai': ['Masala Chai', 'Ginger Chai', 'Chocolate Chai']}

#---------------------END-----------------------------------
# ---------------------END-----------------------------------3




  







































