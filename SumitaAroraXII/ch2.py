import os

os.system("cls")


#Q1. In each of the following Python expressions or statements, indicate what data type belongs in the indicated place by choosing one of hese data types:
# int float bool str list

"""
a) s = _________ + 17 :- int
b) t = _________ + 'pie' :- str
c) x[ ________________ ] = 'catfood' :- float
d) ____________.sort() :- list
e) if ______:  :- bool
"""

#Q2. What does Python print as it executes the following sequence of statements ?
"""
a. print((10+3)*2)
b. print(11/2)
c. x = 25
   print(x*2==50)
d. print(x/2 >= 50)
e. a = 'Honda'
   b = 'Audi'
   print(a+b)
f. c = len(a) + len(b)
   print(c)
g. print(a)
h. print(a[1])
"""
"""
D. types:-

a.int
b.float
c.bool
d.bool
e.str
f.int
g.list
h.list
"""

#Q3. What would be the output of the following code ?
# a = 9000 # initializes and assigns value to variable
# print("Now it's a", type(a))
# a = float(a)
# print("Now it's a", type(a))
# a = str(a)
# print("Now it's a", type(a))

"""
Answer:
Now it's a int
Now it's a float
Now it's a str
"""

#Q4. What would be the output of the following code ? Support your answer with reasons.

# x = 4
# y = 8
# z = x/y*y
# print(z)

"""
Answer:-
4.0 
reason:-
We have x = 4 and y = 8
z is an expression which contains an operation division which is only possible in float datatype for accurate results.
By default Python prints accurate results.
By BODMAS we can say that 4/8 x 8 = 1/2 x 8 = 4
"""