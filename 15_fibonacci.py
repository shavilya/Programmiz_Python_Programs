# Python program to print fibonacci series 

"""
Method 1 : 

nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1
"""

#Method 2 : 

f1,f2 = 0,1 
fibo = [f1,f2]
terms = int(input("Enter number of terms?: "))
count = 0 

if terms == 0 : 
    print("Enter a positive number to check fibonacci series.")
elif terms == 1 : 
    print(f"Fibo series upto {terms} : {f1}")
else : 
    while terms >= count : 
        f1 = f1+f2 
        fibo.append(f1)
        count  += 1 
        f1 = fibo[-2]
        f2 = fibo[-1]
    
    print(f"Fibo series upto {terms}:\n{fibo[:terms]}")

