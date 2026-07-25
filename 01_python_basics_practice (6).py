# # # # # # """
# # # # # # PYTHON PRACTICE FILE - FROM BASIC INTRO TO OPERATORS
# # # # # # ====================================================

# # # # # # How to use this file in VS Code:
# # # # # # 1. Create a folder: Python_Practice
# # # # # # 2. Open that folder in VS Code
# # # # # # 3. Create this file: 01_python_basics_practice.py
# # # # # # 4. Run using terminal:
# # # # # #    python 01_python_basics_practice.py

   
   
# # # # # # This file is written with notes + code + practice tasks.
# # # # # # Students should READ comments, RUN code, then SOLVE practice questions.
# # # # # # """

# # # # # # # ============================================================
# # # # # # # 1. INTRODUCTION TO PYTHON
# # # # # # # ============================================================

# # # # # # """
# # # # # # Python is a high-level, interpreted, beginner-friendly 
# # # # # # programming language.

# # # # # # Python is used in:
# # # # # # - Web development
# # # # # # - Data Science
# # # # # # - AI / Machine Learning
# # # # # # - Automation
# # # # # # - Software development
# # # # # # - Game development
# # # # # # - Scripting
# # # # # # """

# # # # # # print("Welcome to Python Practice!")


# # # # # # # ============================================================
# # # # # # # 2. TRANSLATOR ANALOGY
# # # # # # # ============================================================

# # # # # # """
# # # # # # Computer understands only machine language: 0 and 1.

# # # # # # Example:
# # # # # # Human language: Add 2 and 3
# # # # # # Python code:     2 + 3
# # # # # # Machine language: 010101...

# # # # # # So we need a translator.

# # # # # # Translator means a program that converts our code into machine-understandable form.

# # # # # # Two common translators:
# # # # # # 1. Compiler
# # # # # # 2. Interpreter
# # # # # # """


# # # # # # # ============================================================
# # # # # # # 3. COMPILER VS INTERPRETER
# # # # # # # ============================================================

# # # # # # """
# # # # # # Compiler:
# # # # # # - Translates full code at once.
# # # # # # - Shows errors after checking complete code.
# # # # # # - Generally faster after compilation.
# # # # # # - Example languages: C, C++, Java

# # # # # # Interpreter:
# # # # # # - Translates code line by line.
# # # # # # - Stops when it finds an error.
# # # # # # - Python uses an interpreter.
# # # # # # - Example languages: Python, JavaScript, Ruby
# # # # # # """

# # # # # # print("Python runs line by line using an interpreter.")


# # # # # # # ============================================================
# # # # # # # 4. IDE AND CODE EDITOR
# # # # # # # ============================================================

# # # # # # """
# # # # # # IDE means Integrated Development Environment.

# # # # # # It helps us write, run, debug, and manage code.

# # # # # # Examples:
# # # # # # - VS Code
# # # # # # - PyCharm
# # # # # # - Jupyter Notebook
# # # # # # - Google Colab
# # # # # # - IDLE

# # # # # # For this practice, we use VS Code.
# # # # # # """


# # # # # # # ============================================================
# # # # # # # 5. VS CODE SETUP STEPS
# # # # # # # ============================================================

# # # # # # """
# # # # # # Step 1: Install Python from python.org
# # # # # # Step 2: Install VS Code
# # # # # # Step 3: Install Python extension in VS Code
# # # # # # Step 4: Create a folder for practice
# # # # # # Step 5: Create .py file
# # # # # # Step 6: Open terminal and run:
# # # # # #         python filename.py

# # # # # # To check Python version:
# # # # # # python --version
# # # # # # """


# # # # # # # ============================================================
# # # # # # # 6. FIRST PYTHON PROGRAM
# # # # # # # ============================================================

# # # # # print("Hello, World!")
# # # # # print("My name is Jyoti.")
# # # # # print("I am learning Python from basics.")


# # # # # # # Practice:
# # # # # # # 1. Print your name.
# # # # # # # 2. Print your college name.
# # # # # # # 3. Print your goal.


# # ============================================================
# # 7. COMMENTS IN PYTHON
# # ============================================================

# # This is a single-line comment.

# """
# This is a multi-line comment.
# It is mostly used for notes or documentation.
# """

# # # # # # print("Comments are ignored by Python.")


# # # # # # # ============================================================
# # # # # # # 8. VARIABLES
# # # # # # # ============================================================

# # # # # # """
# # # # # # Variable = Container / Locker to store data.

# # # # # # Example:
# # # # # name = "Jyoti"

# # # # # # Here:
# # # # # # name  -> variable name
# # # # # # =     -> assignment operator
# # # # # # "Jyoti" -> value
# # # # # # """

# name = "Jyoti"
# age = 25
# city = "Surat"

# print(name)
# print(city)
# print(age)

# # # # # # # Updating variable value
# age = 26
# print("Updated age:", age)


# # # # # # # Practice:
# # Create variables:
# # student_name
# # student_age
# # course_name
# # Then print all values.


# # # # # # # ============================================================
# # # # # # # 9. RULES FOR VARIABLE NAMES
# # # # # # # ============================================================

# # # # # # """
# # # # # # Valid variable names:
# # # # # # student_name
# # # # # # age
# # # # # # marks1
# # # # # # _total

# # # # # # Invalid variable names:
# # # # # # 1name        -> cannot start with number
# # # # # # student-name -> hyphen not allowed
# # # # # # class        -> keyword
# # # # # # my name      -> space not allowed

# # # # # # Best practice:
# # # # # # Use meaningful names.
# # # # # # Use snake_case in Python.
# # # # # # """

# # # # # # student_name = "Riya"
# # # # # # student_marks = 85

# # # # # # print(student_name)
# # # # # # print(student_marks)


# # # # # # # ============================================================
# # # # # # # 10. DATA TYPES
# # # # # # # ============================================================

# # # # # # """
# # # # # # Data type means type/category of value.

# # # # # # Common Python data types:

# # 1. int      -> whole numbers(0, 1, -5, 100)
# a = 10
# # 2. float    -> decimal numbers(3.14, -2.5, 0.0)
# b = 3.14
# # 3. str      -> text/string ("Hello, World!")
# c = "Hello, World!"
# # 4. bool     -> True/False
# d = True
# # 5. list     -> ordered, mutable collection
# e = [1, 2, 3]
# # 6. tuple    -> ordered, immutable collection
# f = (1, 2, 3)
# # 7. set      -> unordered unique values
# g = {1, 2, 3}
# # 8. dict     -> key-value pair
# h = {"name": "Jyoti", "age": 25}
# # 9. complex  -> complex numbers (3+4j)
# i = 3 + 4j
# # """


# id=10
# print("integer",id)

# name="krishna"
# print("string",name)

# # percentage

# # # # # # # Integer
# # # # roll_no = 101

# # # # # # # Float
# # # # percentage = 88.5

# # # # # # # String
# # # # student = "Amit"
# # # # name1 = "'Rusta's            "
# # # # name2 = """
# # # # hello        world
# # # # vncjksdnvkj
# # # # ds 
# # # # vsd 
# # # # vdsv
# # # # """
# # # # print(student)
# # # # print(name1)
# # # # print(name2)


# # # # # # # Boolean
# # # # is_passed = True

# # # # print(roll_no)
# # # # print(percentage)
# # # # print(student)
# # # # print(is_passed)


# # # # # # # Check data type using type()
# # # # print(type(roll_no))
# # # # print(type(percentage))
# # # # print(type(student))
# # # # print(type(is_passed))

# # # # # type function return the data type of the variable or 
# # # # # value passed to it. 
 
# # # # # This is useful for understanding what kind of data 
# # # # # you are working with in your program.


# # # # # # # ============================================================
# # # # # # # 11. STRING PRACTICE
# # # # # # # ============================================================

str = 'String practice'
message = "Python's rules formula"
print(str)
print(message)

poem = """
Johnny's      johnny


fvdfvfd 
vfvdf
vfvfdv

"""
print(poem)

print(message)
print(message.upper()) # in uppercase
print(message.lower()) # in lower case
print(message.title()) #
print(message.capitalize()) #
print(len(message)) #length of string

# String indexing
print(message[0])   # First character
print(message[-1])  # Last character

# p y t h o n
# 0 1 2 3 4 5
#-6 -5 -4 -3 -2 -1

# # String slicing[start: End]
print(message[0:6])   # Python
print(message[7:])    # is easy


# Practice:
# Create a variable full_name.
# Print it in uppercase.
# Print its length.
# Print first and last character.


# # # # # # # ============================================================
# # # # # # # 12. TYPE CASTING
# # # # # # # ============================================================

# # # # # # """
# # # # # # Type casting means converting one data type into another.

# # # # # # int()
# # # # # # float()
# # # # # # str()
# # # # # # bool()
# # # # # # """

num1 = "10"
num2 = "20"

# check their datatype which function we can use???
# => type()

print(type(num2))
print(type(num1))
print(num1 + num2)  # String concatenation: 1020

num1 = int(num1)
num2 = int(num2)

print(num1 + num2)  # Addition: 30


# # # # # # # Example
# # # # # # price = 99.99
# # # # # # price_int = int(price)

# # # # # # print(price_int)


# ============================================================
# 13. USER INPUT
# ============================================================

"""
input() is used to take value from user.

Important:
input() always returns string.
"""

# Uncomment to practice:
# user_name = input("Enter your name: ")
# print("Hello", user_name)

# age = input("Enter your age: ")
# print(age)
# print(type(age))  # string

# age = int(age)
# print("After 5 years, your age will be:", age + 5)
# # # # # # # ============================================================
# # # String Methods:   

# 1. upper() - Converts string to uppercase.
str = "Python is easy to learn"
print(str.upper())  # "PYTHON IS EASY TO LEARN"

# 2. lower() - Converts string to lowercase.
print(str.lower())  # "python is easy to learn"

# 3. title() - Converts first character of each word to uppercase.
print(str.title())  # "Python Is Easy To Learn"

# 4. capitalize() - Converts first character of string to uppercase.
print(str.capitalize())  # "Python is easy to learn"

# 4. len() - Returns the length of the string.
print(len(str))  # 22

# 5. strip() - Removes leading and trailing whitespace.
str1 = "  Python is easy to learn.  "
print(str1.strip())  # "Python is easy to learn."

# lstrip() - Removes leading whitespace.
print(str1.lstrip())  # "Python is easy to learn.  "

# rstrip() - Removes trailing whitespace.
print(str1.rstrip())  # "  Python is easy to learn."

# 6. replace() - Replaces a substring with another substring.
str2 = "Python is easy to learn."
print(str2.replace("easy", "fun"))  # "Python is fun to learn."

# 7. split() - Splits the string into a list based on a delimiter.
str3 = "Python is easy to learn."
print(type(str3))
print(str3.split())  # ['Python', 'is', 'easy', 'to', 'learn.']

# string => List => split()
# List => string =>Join()

# 8. find() - Returns the index of the first occurrence of a substring.
str4 = "Python is easy to learn."
print(str4.find("easy"))  # 14

# 9. count() - Returns the number of occurrences of a substring.
print(str4.count("o"))  # 2

# 10. join() - Joins elements of a list into a string with a specified delimiter.
list = ["Python", "is", "fun"]
print(" ".join(list))  # "Python is fun"
print(" | ".join(list))  # "Python | is | fun"

# # # # # split => str to list
# # # # # join => list to str

# # # # # # # Example:
# # # # # # text = "  Python is easy to learn.  "
# # # # # # print(text.upper())        # "  PYTHON IS EASY TO LEARN.  "
# # # # # # print(text.lower())        # "  python is easy to learn.  "
# # # # # # print(text.title())        # "  Python Is Easy To Learn.  "
# # # # # # print(len(text))           # 28
# # # # # # print(text.strip())        # "Python is easy to learn."
# # # # # # print(text.replace("easy", "fun"))  # "  Python is fun to learn.
# # # # # # print(text.split())        # ['Python', 'is', 'easy', 'to', 'learn.']
# # # # # # print(text.find("easy"))   # 14
# # # # # # print(text.count("o"))     # 2
# # # # # # words = ["Python", "is", "fun"]
# # # # # # print(" ".join(words))     # "Python is fun"

# Practice:
# 1. Create a variable sentence with a string value.
# 2. Print it in uppercase.
# 3. Print its length.
# 4. use split and join method

# Task 1:
# 1. Take a string input from user.
# 2. Count how many times letter 'a' appears in the string.

# # # # task_1 = input("Enter a string: ")
# # # # print(task_1.count("a"))



# # # # # Task 2:
# # # # # 1. Take a string input from user.
# # # # # 2. Replace all spaces with hyphens and print the result.

# # # # name=input("Enter a string: ")
# # # # print(name.replace(" ", "-"))

# # # # # Task 3:
# # # # # 1. Take a string input from user.
# # # # # 2. Split the string into words and print the list of words.
# # # # name=input("Enter a string: ")
# # # # word=name.split()
# # # # print("list of words:",word)


# # # # Task 4:
# # # # 1. Take a list input from user.
# # # # 2. Join the list elements into a single string 
# # # # with commas and print the result.

# # # A = ["apple", "banana", "cherry"]
# # # # OUTPUT = "apple,banana,cherry"
# # # print(" | ".join(A))


# # # # Task 5:
# # # # 1. input: "Python is easy to learn"
# # # # 2. output: "Python-is-easy-to-learn"

# # # input="Python is easy to learn"
# # # print(input.replace(" ","-"))

# # # # Task 6:
# # # # 1. input: "Python is easy to learn"
# # # # 2. output: "Java is easy to learn"

# # # input="Python is easy to learn"
# # # print(input.replace("Python","java"))



# # # # ============================================================
# # # # List Methods:

# 1. append() - Adds an element at the end of the list.
list = ["apple", "banana", "ornage"]
list.append("cherry")
print(list)

# 2. insert(indexno, value) - Inserts an element at a specified position.
list.insert(2, "anything")
print(list)
# op = ["apple", "banana", "anything","ornage","cherry"]

# 3. remove() - Removes the first occurrence of a specified element.
list.remove("apple")
print(list)

# 4. pop() - Removes and returns the last element of the list.
# by defualt it will remove the last element

list.pop()  # remove the last element
print(list)

list.pop(1) 
print(list)

# 5. sort() - Sorts the list in ascending order. A TO Z
list.sort()
print(list)

# 6. reverse() - Reverses the order of the list. Z TO A
list.reverse()
print(list)

# 7. index() - Returns the index of the first occurrence of a 
# specified element.
["apple", "banana", "anything","ornage","cherry","apple"]
# 8. count() - Returns the number of occurrences of a specified 
# element.
# 9. clear() - Removes all elements from the list.
# 10. copy() - Returns a shallow copy() of the list.

# # # Example:
# # fruits = ["apple", "banana", "cherry"]

# # fruits.append("mango")
# # print(fruits)  # ['apple', 'banana', 'cherry', 'mango']

# # fruits.insert(1, "orange")
# # print(fruits)  # ['apple', 'orange', 'banana', 'cherry', 'mango']

# # fruits.remove("banana")
# # print(fruits)  # ['apple', 'orange', 'cherry', 'mango']

# # fruits.pop()
# # print(fruits)  # ['apple', 'orange', 'cherry']

# # fruits.pop(1)
# # print(fruits)  # ['apple', 'cherry']

# # fruits.sort()
# # print(fruits)  # ['apple', 'cherry']

# # fruits.reverse()
# # print(fruits)  # ['cherry', 'apple']

# # fruits.clear()
# # print(fruits)  # []

fruits = ["apple", "banana", "cherry", "apple"]
print(fruits.index("cherry"))  # 2
print(fruits.count("apple"))    # 2

# # fruits_copy = fruits.copy()
# # print(fruits_copy)  # ['apple', 'banana', 'cherry', 'apple']

# # fruits = ["apple", "banana", "cherry"]

# # # # Task 1:
# # # # 1. Create a list of your Best friend names.
# # # # 2. Add a new Best friend name to the list.
# # # list = ["priti", "bhoomi", "falguni"]
# # # list.append("hiral")
# # # print(list)




# # # # Task 2:
# # # # 1. Create a list of numbers.
# # # # 2. Sort the list in ascending order.
# # # list = [10,7, 5, 6 ,8]
# # # list.sort()
# # # print(list)


# # # # Task 3:
# # # # 1. Create a list of Best friend names.
# # # # 2. Remove a Best friend names from the list.


# # # list=["feny","dhruvi"]
# # # list.remove("feny")
# # # print(list)


# # # # Task 4:
# # # # input: ["red", "green", "blue"]
# # # # output: "red-green-blue-black"

# # # list=["red", "green", "blue"]
# # # list.append("black")
# # # print("-".join(list))

# # # # Task 5:
# # # # input: red, green, blue, black
# # # # output: red, white, blue, black

# # # # # # # ============================================================
# # # # # # # 14. OPERATORS IN PYTHON
# # # # # # # ============================================================

# # # # # # """
# # # # Operators are symbols used to perform operations.

# Types of operators:
# 1. Arithmetic operators
# 2. Assignment operators
# 3. Comparison operators
# 4. Logical operators
# 5. Membership operators
# 6. Identity operators
# 7. Bitwise operators
# """


# # # # # # # ============================================================
# # # # # # # 15. ARITHMETIC OPERATORS (=, +, -, *, /, //, %, ** )
# # # # # # # ============================================================

a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus/Remainder:", a % b)
print("Exponent/Power:", a ** b)

# # # # """
# # # # /  gives decimal result
# # # # // gives integer/floor result
# # # # %  gives remainder
# # # # ** gives power
# # # # """


# # # # Practice:
# # # # # Take two numbers and perform all arithmetic operations.
# # # a=int(input("Enter first number: "))
# # # b=int(input("Enter second number: "))
# # # print(a+b)
# # # print(a-b)
# # # print(a*b)
# # # print(a/b)
# # # print(a**b)
# # # print(a//b)



# # # # ============================================================
# # # # 16. ASSIGNMENT OPERATORS(=, +=, -=, *=, /=, %=)
# # # # ============================================================

x = 10
print("Initial x:", x)

x += 5   # x = x + 5
print("After += :", x)

x -= 3   # x = x - 3
print("After -= :", x)

x *= 2   # x = x * 2
print("After *= :", x)

x /= 4   # x = x / 4
print("After /= :", x)

x %= 3   # x = x % 3
print("After %= :", x)


# # # # ============================================================
# # # # 17. COMPARISON OPERATORS(==, !=, >, <, >=, <=)
# # # # ============================================================

# # # """
# # # Comparison operators return True or False.
# # # """
p = 10
q = 20

print(p == q)  # Equal to
print(p != q)  # Not equal to
print(p > q)   # Greater than
print(p < q)   # Less than
print(p >= q)  # Greater than or equal to
print(p <= q)  # Less than or equal to


# # # Practice:
# # # Compare your age with voting age 18.

# # # age = int(input("Enter your age: "))
# # # print("Eligible to vote:", age >= 18 )


# # # ============================================================
# # # 18. LOGICAL OPERATORS(and, or, not)
# # # ============================================================

# # """
# # Logical operators:
# # 1. and -> True if both conditions are True
# # 2. or  -> True if at least one condition is True
# # 3. not -> reverses result
# # """

# # # age = 22
# # # has_id = True

# # # print(age >= 18 and has_id == True) # True
# # # print(age >= 18 or has_id == False) # True
# # # print(not has_id) # False


# # # Example
# # # marks = 75

# # # print(marks >= 35 and marks <= 100) #True


# # # ============================================================
# # # 19. MEMBERSHIP OPERATORS (in, not in)
# # # ============================================================

# # """
# # Membership operators check whether a value exists in a sequence.
# # # in
# # # not in
# # # """

# # course = "Python Data Science" # string

# # print("Python" in course)
# # print("Java" in course)
# # print("Java" not in course)

# # fruits = ["apple", "banana", "mango"] # List

# # print("mango" in fruits)
# # print("grapes" not in fruits)


# # # ============================================================
# # # 20. IDENTITY OPERATORS
# # # ============================================================

# # """
# # Identity operators check memory/location/object identity.

# # is
# # is not
# # """

# # m = [1, 2, 3]
# # n = m
# # o = [1, 2, 3]

# # print(m is n)      # True, same object
# # print(m is o)      # False, values same but object different
# # print(m == o)      # True, values same
# # print(m is not o)  # True


# # # ============================================================
# # # 21. MINI PRACTICE PROGRAMS
# # # ============================================================

# # # Program 1: Simple Calculator
# # num1 = 20
# # num2 = 5

# # print("Calculator")
# # print("Add:", num1 + num2)
# # print("Subtract:", num1 - num2)
# # print("Multiply:", num1 * num2)
# # print("Divide:", num1 / num2)


# # # Program 2: Area of Rectangle
# # length = 10
# # width = 5
# # area = length * width

# # print("Area of rectangle:", area)


# # # Program 3: Simple Interest
# # principal = 10000
# # rate = 5
# # time = 2

# # simple_interest = (principal * rate * time) / 100
# # print("Simple Interest:", simple_interest)


# # # Program 4: Marks Percentage (5 subjects)
# # # Program 5: Voting Eligibility (user input)(18+ years)


# # # # # # subject1 = 80
# # # # # # subject2 = 75
# # # # # # subject3 = 90

# # # # # # total = subject1 + subject2 + subject3
# # # # # # percentage = total / 3

# # # # # # print("Total Marks:", total)
# # # # # # print("Percentage:", percentage)


# # # # # # student_age = 19

# # # # # # print("Can vote:", student_age >= 18)


# # # # ============================================================
# # # # 22. STUDENT PRACTICE QUESTIONS
# # # # ============================================================

# # # """
# # # Practice Set:

# # # Q1. Print your introduction using print().
# # # Q2. Create variables for name, age, city, and course.
# # # Q3. Check data type of all variables.
# # # Q4. Take two numbers and perform:
# # #     addition, subtraction, multiplication, division, floor division, modulus, power.
# # # Q5. Convert string "500" into integer and add 100.
# # # string_number = "500"
# # # ineger_number = int(string_number)
# # # result = ineger_number + 100
# # # print(result)  # Output: 600



# # # Q6. Create a marks calculator for 5 subjects.
# # # Q7. Create a simple interest calculator.
# # # Q8. Check whether a person is eligible for voting.
# # # Q9. Check whether "Python" exists in "Python is powerful".
# # # var= "Python is powerful"
# # # print("Python" in var)  # Output: True

# # # Q10. Create a mini bill calculator:
# item_price = 500
# quantity = 3
# discount = 100
# final_bill = (item_price * quantity) - discount
# print("Final Bill Amount:", final_bill)  # Output: 1400




# # # # # # # ============================================================
# # # # # # # 23. HOMEWORK TASK
# # # # # # # ============================================================

# # # # # # """
# # # # # # Homework:

# # # # # # Create a file named:
# # # # # # homework_day1.py

# # # # # # Write programs for:

# # 1. Personal introduction
# # 2. Calculator
# # 3. Percentage calculator
# # 4. Simple interest calculator
# # 5. Temperature conversion: Celsius to Fahrenheit

# # # # # # Formula:
# # # # # # fahrenheit = (celsius * 9/5) + 32
# # # # # # """


# # # # # # # ============================================================
# # # # # # # END OF FILE
# # # # # # # ============================================================

# # # # # # print("Practice file completed. Now solve the exercises!")
