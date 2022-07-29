
def Factors(int): 
    fact = []
    for i in range(1,number+1) : 
        if number % i == 0 : 
            fact.append(i)
    return fact

if __name__ == "__main__" : 
    number = int(input("Enter any number: "))

    fact = Factors(int) 

    print(f"Factorss of {number}:{fact}")