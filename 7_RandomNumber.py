# Python Program to generate a Random Number. 

import random as r

def Random(star,end):
    rand_list = []
    for i in range(star,end+1): 
        rand_list.append(i)

    return r.choice(rand_list)

    
if __name__ == "__main__" : 
    star = int(input("Enter a number to start for a range: "))
    end = int(input("Enter a last number for a range: ")) 

    rand = Random(star,end)

    print("Random Number from {} and {} is {}".format(star,end,rand))