### Task 1 - fix the FizzBuzz
#Your :heavy_plus_sign: Task is to fix program non-working correctly.
#The FizzBuzz problem:  
# For all integers between 1 and 99 (include both):  
#- print ('fizz' for multiples of 3),
#- print ('buzz' for multiples of 5), 
#- print ('fizzbuzz' for multiples of 3 and 5).


#Program with exactly **7** bugs:  
#python


# mult_both = 'fizzbuzz'
# three_mul = 'fizz'
# five_mul = 'buzz'
# num1 = 3
# num2 = 5 
# max_num = 100
   
# for i in range(1,max_num):
#     % or modulo division gives you the remainder 
    
# 	if i%num1 == 0 and i%num2 == 0:
# 		print(i, mult_both)
# 	elif i%num2 == 0:
# 		print(i, five_mul)
# 	elif i%num1 == 0:
# 		print(i, three_mul)

### :heavy_plus_sign: Task 2 - summing integers

# Your task is to fix program non-working correctly.
# The problem:  
#   - sum integers from 1 to 5 using while loop
#   - calculate what result should be and what you get after running the program   


# Program with bug:  
# ```python

# n = 5
# number = 1
# sum = 10
# while number < n + 1:
#     sum = sum + 1
#     number = number + 1
# print("Sum =", sum)

# >Find the bug and fix it :smiley:
# - Your result could look like this:

# ```bash
# Sum = 15

### :heavy_plus_sign: Task 3 - summing integers with range()

# Your task is to fix program non-working correctly.
# The problem:  
#   - sum integers from 1 to 5 using `range()` function
#   - calculate what result should be and what you get after running the program   


# Program with bug:  
# ```python


# n = 5
# num = 1
# sum = 5
# for num in range(n):
#     sum += num
# print("Sum =", sum)


# >Find the bug and fix it :smiley:
# - Your result could look like this:

# ```bash
# Sum = 15

### :heavy_plus_sign: Task 4 - printing in loops

# Your task is to fix program non-working correctly.
# The problem:  
#   - there are 4 short programs with loops, that should print some numbers, but they don't work at all!  


# Program no. 1 with the bug:  
# ```python


# for x in range(3):
#     print(x)

# >Find the bug and fix it :smiley:
# - Your result could look like this:

# ```bash
# 0
# 1
# 2
# ```

# Program no. 2 with the bug:  
# ```python
# for j in range(5):
#     print("This is loop number ", j)


# >Find the bug and fix it :smiley:
# - Your result could look like this:

# ```bash
# This is loop number 0
# This is loop number 1
# This is loop number 2
# This is loop number 3
# This is loop number 4
# ```

# Program no. 3 with the bug:  
# ```python
# x = 10
# while x > 0:
#     print(x)
#     x -= 1
    

# ```

# >Find the bug and fix it :smiley:
# - Your result could look like this:

# ```bash
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# ```

# Program no. 4 with the bug:  
# ```python
# countdown = 5
# while countdown > 0:
#     print(f"{countdown}")
#     countdown -= 1
# else:
#     print("Start!")

# >Find the bug and fix it :smiley:
# - Your result could look like this:

# ```bash
# 5
# 4
# 3
# 2
# 1
# Start!
# ```


### :heavy_plus_sign: Task 5 - summing three integers

# Your task is to fix program non-working correctly.
# The problem:  
#   - sum the three prompted integers
#   - however, if two values are equal sum should be zero
#   - calculate what result should be and what you get after running the program   


# Program with bugs:  
# ```python
# x = int(input("First number: "))
# y = int(input("Second number: "))
# z = int(input("Third number: "))

# if x == y or y == z or x == z:
#     result = 0
# else:
#     result = x + y + z
# print("Calculated sum is ", result)


# >Find the bug and fix it :smiley:
# - Your result could look like this:

# ```bash
# First number: 5
# Second number: 5
# Third number: 5
# Calculated sum is  0

# First number: 4
# Second number: 5
# Third number: 5
# Calculated sum is  0

# First number: 3
# Second number: 4
# Third number: 5
# Calculated sum is  12


### :heavy_plus_sign: Task 6 - summing two integers

# Your task is to fix program non-working correctly.
# The problem:  
# - sum the two prompted integers
# - however, if the sum is between 15 to 20 (both numbers included) it should be calculated to 20  
# - calculate what result should be and what you get after running the program   


# Program with bugs:  
# ```python
# x = int(input("First number: "))
# y = int(input("Second number: "))

# result = x + y

# if result >= 15 and result <= 20:
# 	result = 20
# 	print("Calculated sum is ", result)

# else:
# 	print("Calculated sum is ", result)

# >Find the bug and fix it :smiley:
# - Your result could look like this:

# ```bash
# First number: 11
# Second number: 4
# Calculated sum is  20

# First number: 44
# Second number: 4
# Calculated sum is  48

### :heavy_plus_sign: Task 7 - swapping variables

# Your task is to fix program non-working correctly.
# The problem:  
# - prompt two values and assign them to variables `a` and `b`
# - write the Python program to swap these two variables
# - calculate what result should be and what you get after running the program   
# >Remark: **don't use** "fast" swapping available in Python:  
# ```python
# a, b = b, a

# Program with bugs:  
# ```python
# a = input("First value: ")
# b = input("Second value: ")

# print("Before swapping: a =", a, " ,b =", b)

# temp = a
# a = b
# b = temp

# print("After swapping: a =", a, " ,b =", b)

# >Find the bug and fix it :smiley:
# - Your result could look like this:

# ```bash
# First value: Hello 
# Second value: DCI
# Before swapping: a = Hello  b = DCI
# After swapping: a = DCI  b = Hello

### 
### :heavy_plus_sign: Task 8 - max and min values

# Your task is to fix program non-working correctly.
# The problem:  
# - prompt three float numbers and determine the largest and the smallest one
# - calculate what result should be and what you get after running the program   

# Program with bugs:  
# ```python
# x = float(input("First number: "))
# y = float(input("Second number: "))
# z = float(input("Third number: "))

# print("The maximum value is ", max(x, y ,z))
# print("The minimum value is ", min(x, y ,z))


# >Find the bug and fix it :smiley:
# - Your result could look like this:

# ```bash
# First number: 6
# Second number: 7
# Third number: 7

# The maximum value is  7.0
# The minimum value is  6.0
### 

### :heavy_plus_sign: Task 9 - convertion

# Your task is to fix program non-working correctly.
# The problem:  
# - prompt value from the user and assign it to some variable  
# - if given value is 0 (zero) convert it to `False` and if given value is 1 convert it to `True`
# - display results  

# Program with bugs:  
# ```python
# x = input("Type your value: ")

# if x == '0':
#     x = False
# elif x == '1':
#     x = True
# else:
# 	x != 0 or x!=1
        
# print("Your entered value is now ", x)


# >Find the bug and fix it :smiley:
# - Your result could look like this:

# ```bash
# Type your value: 0
# Your entered value is now  False

# Type your value: 1
# Your entered value is now  True

# Type your value: hi!
# Your entered value is now  hi!
### 


### :heavy_plus_sign: Task 10 - divisible number

# Your task is to fix program non-working correctly.
# The problem:  
# - accept (prompt) two integers values from the user  
# - check whether a first number is divisible by second number and vice versa  
# - display results  

# Program with bugs:  
# ```python
# y = int(input("Second number: "))
# x = int(input("First number: "))

# if x % y == 0:
#     print("First number is divisible by second number, result =", x / y)
# elif y % x == 0:
#     print("Second number is divisible by first number, result =", y / x)
# else:
#     print("Numbers are non-divisable!")

# >Find the bug and fix it :smiley:
# - Your result could look like this:

# ```bash
# First number: 5
# Second number: 55
# Second number is divisible by first number, result = 11.0

# First number: 3
# Second number: 5
# Numbers are non-divisable!
# ```