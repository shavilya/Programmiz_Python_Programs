def PrimeNumber(int) : 
    global flag
    flag = 0 
    for i in range(2,number+1):
        if number % i  == 0 : 
            flag+= 1


if __name__ == "__main__" :
    global flag

    number = int(input("Enter any number to check prime or not: "))

    Prime = PrimeNumber(int)

    if number == 1 : 
        print(f"{number} is Prime Number.")
    elif flag > 1 :
        print(f"{number} is not a Prime Number.")
    else : 
        print(f"{number} is Prime Number.")

