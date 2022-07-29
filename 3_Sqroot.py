# Python program to find the square root 

"""
# Using math library 
import math as m 
a = int(input("Enter the value of 'a' to find square root.: "))

SQ_Root = m.sqrt(a)

print(f"SQ root of {a} is {int(SQ_Root)}")
"""

#Without math library 

a = int(input("Enter the value of 'a' to find square root.: "))

SQ_Root = a**(1/2)

print(f"SQ root of {a} is {int(SQ_Root)}")



