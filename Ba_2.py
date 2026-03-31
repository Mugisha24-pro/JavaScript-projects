# ====================================================
# Lesson 2: Python Loops, Functions and File Handling
# ====================================================

# 1. Loops And Iterations
# -----------------------

# Loops( we use : For loop and While loop)

# # For loop
# print ("This is a For loop in Python")
# print ("----------------------------\n")

# for i in range (1,11):
#     print (i)

# # While loop    
# print ("This is a While loop in Python")
# print ("------------------------------\n")

# i = 1
# while i <= 10:
#     print (i)
#     i += 1

# a program that allows a user to input a number and prints if it is an even or a odd number

# inpt = int (input ( "Enter a number: "))

# if inpt % 2 == 0:
#      print (str(inpt) + " is an even number")
# else:
#      print (str(inpt) + " is an odd number")


# lst_1 = [1,2,3,4,5,6,7,8,9,10]
# for i in lst_1:
#     if i % 2 == 0:
#         print (str(i) + " is an even number")
#     else:
#         print (str(i) + " is an odd number")
    
#  2. Functions (i. user defined functions)
#  ---------------------------------------

# a program that tells a user to enter a number and the program checks wheather the inputed 
# number is an even or an odd number using function(user defined)
# def even_odd (num):
#     if num % 2 == 0:
#      print (str(num) + " is an even number")
#     else:
#      print (str(num) + " is an odd number")


# number = int (input ("Enter a number to check wheather it's an even or an odd number: "))
# even_odd(number)     

# program that calculate a factorial of a number

# def fact_number (nbr):
#   fact = 1
#   for i in range (1,nbr+1):
#     fact = fact * i
#   return str(nbr) + "! = " + str(fact)
  
# number = int (input("Enter a number to get its factorial: "))
# print(fact_number(number))

# ii. lambda fuction
# ------------------

# simple lambda function
# a = lambda a: a+10
# print (a(15))

# program that uses lambda function to display the factorial of a user input number

# fact_number = lambda n: 1 if n == 0 else n * fact_number(n - 1)

# number = int(input("Enter a number to get its factorial: "))
# print(f"{number}! = {fact_number(number)}")

# even_odd = lambda num: print(
#     f"{num} is an even number" if num % 2 == 0
#     else f"{num} is an odd number"
# )

# number = int(input("Enter a number to check whether it's an even or an odd number: "))
# even_odd(number)

# iii. MAP,REDUCE AND FILTER FUNCTION
# -----------------------------------

