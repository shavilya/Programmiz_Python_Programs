# Python program to print Factorial of a number. 
# For example, the factorial of 6 is 1*2*3*4*5*6 = 720. 
# Factorial is not defined for negative numbers, 
# and the factorial of zero is one, 0! = 1.

number = int(input("Enter the number to check factorial of: ")) 
fact = 1 


for i in range(1,number+1): 
    fact = fact * i 
    
print(f"Factorial of {number} is {fact}")

