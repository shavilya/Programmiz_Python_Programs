# Python program to add two Numbers 

"""
#Without using function 
print("Note : You can enter only integer values of a and b.")
a = int(input("Enter the value of 'a': "))
b = int(input("Enter the value of 'b': "))

sum = a + b  

print(f"Sum of a and b is sum {sum}") 
"""

#With using function 
def sum(a,b) : 
    c = a + b 
    return c 

if __name__ == "__main__" : 
    a = int(input("Enter the value of 'a': "))
    b = int(input("Enter the value of 'b': "))
    s = sum(a,b) 
    print(f'Sum of a and b is {s}')
