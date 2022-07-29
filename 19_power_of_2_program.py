# Python Program to Display Powers of 2 using function

def power_of_two(element) :
    return 2** element 


if __name__ == "__main__" : 

    terms = 10 

    for i in range(terms+1) : 
        pt = power_of_two(i) 
        print(f"2 raised to power {i} is {pt}")
    


