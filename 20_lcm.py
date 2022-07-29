

# Python program to find the LCM of two numbers. 

# The least common multiple (L.C.M.) of two numbers 
# is the smallest positive integer that is perfectly divisible by the two given numbers.
# Python Program to find the L.C.M. of two input number

def compute_lcm(x, y):

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1
       print(greater)

   return lcm

num1 = 54
num2 = 25 

print("The L.C.M. is", compute_lcm(num1, num2))