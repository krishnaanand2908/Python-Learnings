from itertools import product
import os
import random
from tkinter import font 
import fontstyle
import math

os.system('cls')

def factorial29():
   os.system('cls') 
   while(True):
        num = int(input('Enter the whole number of which you want to get the factorial:\n'))
        factorial = 1
        if num < 0:
            print(fontstyle.apply('Please Enter a \'Whole Number\'\n', 'White/Bold'))
            os.system('cls')
            continue
        else:
            for i in range(1, num+1):
                factorial = num*i
            print(f'{num}! = {factorial}')
            break
        
def infinity_add():
    os.system('cls')
    num1 = float(input(fontstyle.apply('Enter a rational number here:\n', 'CYAN/BOLD')))
    num2 = float(input(fontstyle.apply('Enter a rational number here:\n', 'CYAN/BOLD')))
    sum = num1 + num2
    print(fontstyle.apply(f'{num1} + {num2} = {sum}', 'YELLOW/BOLD'))
    os.system('cls')
    
    while(True):
        choice = input(fontstyle.apply('Press ENTER to add another rational number:\n', 'DARKCYAN/BOLD'))
        os.system('cls')
        if choice == '':
            numx = float(input(fontstyle.apply('Enter a rational number here:\n', 'CYAN/BOLD')))
            sum = sum + numx
            print(fontstyle.apply(f'{sum} + {numx} = {sum + numx}', 'yellow/bold'))
        else:
            break
        
def infinity_subtract():
    os.system('cls')
    format = fontstyle.apply('FORMAT:\n[First Number] - [Second Number]', 'red/bold/2underline')
    print(format)
    num1 = float(input(fontstyle.apply('Enter a rational number here:\n', 'PURPLE/BOLD')))
    num2 = float(input(fontstyle.apply('Enter a rational number here:\n', 'PURPLE/BOLD')))
    difference = num1 - num2
    print(fontstyle.apply(f'{num1} - {num2} = {difference}', 'YELLOW/BOLD'))
    
    while(True):
        print(format)
        choice = input(fontstyle.apply('Press ENTER to subtract another rational number:\n', 'Cyan/BOLD'))
        os.system('cls')
        if choice == '':
            numx = float(input(fontstyle.apply('Enter a rational number here:\n', 'PURPLE/BOLD')))
            print(fontstyle.apply(f'{difference} - {numx} = {difference - numx}', 'yellow/bold'))
            difference = difference - numx
        else:
            break
        
def infinity_multiplication():
    os.system('cls')
    num1 = float(input(fontstyle.apply('Enter a rational number here:\n', 'CYAN/BOLD')))
    num2 = float(input(fontstyle.apply('Enter a rational number here:\n', 'CYAN/BOLD')))
    product = num1 * num2
    print(fontstyle.apply(f'{num1} x {num2} = {product}', 'YELLOW/BOLD'))
    os.system('cls')
    
    while(True):
        choice = input(fontstyle.apply('Press ENTER to multiply another rational number:\n', 'DARKCYAN/BOLD'))
        os.system('cls')
        if choice == '':
            numx = float(input(fontstyle.apply('Enter a rational number here:\n', 'CYAN/BOLD')))
            product = product * numx
            print(fontstyle.apply(f'{product} x {numx} = {product * numx}', 'yellow/bold'))
        else:
            break
        
def infinity_division():
    os.system('cls')
    format = fontstyle.apply('FORMAT:\n[First Number] ÷ [Second Number]', 'green/bold/2underline')
    print(format)
    num1 = float(input(fontstyle.apply('Enter a rational number here:\n', 'PURPLE/BOLD')))
    num2 = float(input(fontstyle.apply('Enter a rational number here:\n', 'PURPLE/BOLD')))
    quotient = num1 / num2
    print(fontstyle.apply(f'{num1} ÷ {num2} = {quotient}', 'YELLOW/BOLD'))
    
    while(True):
        print(format)
        choice = input(fontstyle.apply('Press ENTER to divide another rational number:\n', 'Cyan/BOLD'))
        os.system('cls')
        if choice == '':
            numx = float(input(fontstyle.apply('Enter a rational number here:\n', 'PURPLE/BOLD')))
            print(fontstyle.apply(f'{quotient} ÷ {numx} = {quotient / numx}', 'yellow/bold'))
            quotient = quotient / numx
        else:
            break
        
a = math.hcf(10, 15)
print(a)
