

# Python program to print sum of natural numbers 


number_terms = int(input("Enter the number of terms for sum of natural numbers: "))
sum = 0 
for i in range(number_terms+1): 
    sum += i 

print(f"Sum of natural numbers of {number_terms} numbers is {sum}.")
