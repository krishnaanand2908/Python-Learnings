import os
from re import X
os.system("cls")
#1. For each of the following, write a single (that is, one) Python statement:
# (a) Tell the user to Enter your name, then read in, and assign to a variable, string typed in by the user.
# name = str(input("Enter your name:\n"))
# (b) Tell the user to Enter your age, then read in, and assign to a variable, integer typed in by the user.
# age = int(input("Enter your age:\n"))
# (c) Print out on separate lines, Your name is 'name' and Your age is 'age', where 'name' and 'age' are the values of the two variables entered above.
# print(f"{name}\n{age}")

#2. Give three examples of legal variable names and two examples of illegal variables names in Python. For the illegal variable names explain why they are illegal. Do not use one-letter variable names.
"""Legal Names:- (i)name (ii)age (iii)choice"""
"""Illegal Names:- (i)1235 (ii)())"""
"""1235 is an illegal name because it isn't starts with an alpha numeric charecter(A-Z, a-z or _)"""
"""()) is an illegal name because it isn't starts with an alpha numeric charecter(A-Z, a-z or _)"""

#3. In each of the following parts there is an error in the Python code, Identify the error by name and describe the problem. (Each piece of code is prefixed with a brief description of the programmer's intention.)

#(i) The following code attempts to compute the product of m and x added to b and assign that value to y.
#   y = mx + b

# y = mx + b 
"""It's the NameError. It will occur because the values of the variables y, m, x and b aren't defined."""

# (ii) The following code attempts to compute the first-order effects of some physical process. You may assume that equation is correct
# cofactor = alpha*x*x
# 1storder = 1.0/cofactor
# 2ndorder = 2.0 ** 1storder
"""The above code is completely wrong and the name of the error is SyntaxError. SyntaxError occurs when a code is not written properly. In this case the variables 1storder and 2ndorder aren't starting with any alpha numeric charecter(A-Z, a-z or _)"""

#4. While taking input from input(), you need to convert the input into floar or int types, if you are reading numbers.
#(a)What built-in function do you use to covert a string into a floating-point number? Demonstrate this function by converting string "85" into a floating-point number and assigning it to a variable x.
# a = "85"
# x = float(a)

# (b) What built-in function do you use to convert a string into an integer?
"""We use int() function to convert a string into an integer."""

# (c) What happens when you try to convert a string into an integer but the string is not a number?
"""If we try to convert a string which is not a number into an integer then the code editor you are using will show that it's a ValueError because a string which is not a number cannot be converted into an integer or a floating-point number."""

# 5. What would be the output of the following code?
# print('doesn\'t')
# print("doesn\'t")
# print(' "Yes," he said.')
# print("\"Yes,\" he said.")

"""
doesn't
doesn't
"Yes," he said.
"Yes," he said.
"""

#6. Write a program to print an acrostic poem as shown below:
# poem name: these things I have spoken unto you by John 16:33, Bible verse

# print("These things I have sPoken unto you,")
# print("         that in me yE might have peace.")
# print("   In the world ye shAll have tribulation:")
# print("      but be of good Cheer;")
# print("       I have overcomE the world.")

# 7. Write a program to print the following ASCII art using print statements:

#a

print()

