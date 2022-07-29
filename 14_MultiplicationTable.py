
def MultiplicationTable(int):
    for i in range(1,number+1):
        if i <= 10 :  
            print(f"{number} * {i} = {number*i}")
        else : 
            break

if __name__ == "__main__" : 
    number = int(input("Enter any number: "))

    multiplcation_table = MultiplicationTable(int) 

   