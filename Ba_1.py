# ==================================
# Lesson 1: Data Structure in Python
# ==================================

# 1.Variables in Python
# ---------------------

name = "MUGISHA"
age = 23
height = 1.72
choice = True

# 2.Data types in python
# ----------------------

print (type(name))
print (type(age))
print (type(height))
print (type(choice))


print ("============================================================\n")
print ("Hello" +" "+ name + "!" ) 
print ("You are " + str(age) + " years old and your Height is" + " " + str(height) + "m\n")
print ("Dear Sir," + " " + name + " Welcome to Python Programming Language!\n") 
print ("============================================================")


# 3.List and Turples in python
# ----------------------------

print ("This is a List in Python")
print ("------------------------\n")
mylist = ["MUGISHA","Jonathan","Age = " + str(age),"Height = " + str(height)]
print (type(mylist))
print (mylist[0] + " " + mylist[1] + " is" + " " + mylist[2] + " years old and his height is" + " " + mylist[3] + "m")
print ("\n")

print ("This is a Turple in Python")
print ("--------------------------\n")
myturple = ("Mangos","Apples","Oranges",12.5,True,[1,2,3])
print (type(myturple))
print (myturple[0] + " " + myturple[1] + " " + myturple[2] + " are fruits that " + "cost" + " " + str(myturple[3]) + "$ each")
print ("\n")

print ("============================================================\n")

#  --------------------------
#  Sorting a Truple in Python
#  --------------------------

tuple_1 = (1,3,5,4,2,6,10,9,7,8)
sort_lst = sorted(tuple_1) #this is a sorted list and to make it a tuple you must convert it into a tuple .
new_turple = tuple (sort_lst)
print (type(new_turple))
print (new_turple)

#  ------------------------
#  Sorting a List in Python
#  ------------------------

list_1 = [1,3,5,4,2,6,10,9,7,8]
my_new_list = sorted(list_1)
list_1.sort()
my_new_list = sorted(list_1, reverse = True)

print (my_new_list)

#  4.Sets in Python (All items must be unique)
#  -----------------------------------------

class_a = ["John", "Jane", "Doe", "Smith", "Jane"]
class_b = ["Jane", "Smith", "Alex", "Chris"]

set_a = set(class_a)
set_b = set(class_b)

print (set_a)
print (set_b)

print ( set_a.intersection(set_b))
print (set_a.union(set_b))

#  5.Dictionaries in Python ( Keys must be unique and immutable while values can be any of data types)
#  ---------------------------------------------------------------------------------------------------

student = {
    "name": "John",
    "age": 21,
    "course": "Computer Science"
}

print(student)

# Accessing values in a dictionary using keys
print(student["name"])
print(student["age"])
print(student["course"])

# Adding new key value pair to a dictionary
student["grade"] = "A"
print(student)

# Updating a value of a key in a dictionary
student["age"] = 22
student["name"] = "James"
student["grade"] = "B"
print(student)

# deleting a key value pair from a dictionary
del student["age"]
print (student)

# Sorting a dictionary 
sorted_student_info = sorted(student) # this will sort the keys of the dictionary in alphabetical order and return a list of sorted keys.
sorted_student_info = sorted(student.items()) # this will sort the key value pairs of the dictionary based on the keys in alphabetical order and return a list of tuples where each tuple contains a key value pair.
sorted_student_info = sorted(student.keys()) # this will sort the keys of the dictionary in alphabetical order and return a list of sorted keys.
sorted_student_info = sorted(student.values()) # this will sort the values of the dictionary in alphabetical order and return a list of sorted values.
print (sorted_student_info)

# F-String in python
# ------------------

# f"text {variable}"

name = "Jonathan"
age = 21
print(f"My name is {name}")
print(f"My name is {name} and I am {age} years old.")



#                                                     ===========
#                                                      The End !
#                                                     ===========