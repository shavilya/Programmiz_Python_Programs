# python program to print amstrong number.

original_number = 153
test_number = original_number 
place_list = []
sum_cube_number = 0 
while(test_number > 0) : 
    place = test_number % 10 
    place_list.append(place)
    test_number = test_number // 10
    

for i in place_list : 
    sum_cube_number += i**3

if original_number == sum_cube_number : 
    print(f"{original_number} is amstrong number")
else : 
    print(f"{original_number} is not an amstrong number.")