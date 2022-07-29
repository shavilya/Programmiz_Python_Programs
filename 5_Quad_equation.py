# Python program to solve quadratic equation 

"""
#Method1.
import math as m 

def unknown(a,b,c):
    global x1,x2
    if a and b and c >= 0 : 
        x1 = -b + m.sqrt((b**2 - 4*a*c)/2*a)
        x2 =  -b - m.sqrt((b**2 - 4*a*c)/2*a)
    else : 
        print("Please enter values of a,b,c such as a,b,c == Real numbers and a!=0")
    return x1,x2 


def quadratic_equation(x1,x2,a,b,c) :
    global equation1,equation2 
    equation1 = a*x1**2 + b*x1 + c
    equation2 = a*x2**2 + b*x2 + c 
    return equation1,equation2

    
if __name__ == "__main__" :
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))
    global x1,x2 
    global equation1,equation2 

    un = unknown(a,b,c) 
    quad = quadratic_equation(x1,x2,a,b,c) 

    print(f"Value of 'Unknown' x are:{x1} and {x2}")
    print(f"Value of 'equation' are:{equation1} and {equation2}")

"""

#Method2
# import complex math module
import cmath

a = 1
b = 5
c = 6

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))