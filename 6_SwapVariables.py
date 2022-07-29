# Python program to swap variables. 

"""
#Using Functions 

def swap(x1,x2): 
    x1,x2 = x2,x1 
    print(f"Values after swapping:{x1} and {x2}")

if __name__ == "__main__" : 
    x1 = int(input("Enter value of variable 'x1': "))
    x2 = int(input("Enter value of variable 'x2': "))
    print(f"Values before swapping:{x1} and {x2}")

    s = swap(x1,x2) 
    
"""

# Method2 

x1,x2 = input("Enter two values: ").split(" ")
print(f"Values before swapping: x1={int(x1)}  and x2={int(x2)}")

temp = 0 

temp = x2 
x2 = x1 
x1 = temp 

print(f"value after swapping:{int(x1)} and {int(x2)}")