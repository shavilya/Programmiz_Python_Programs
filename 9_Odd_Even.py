def Odd_Even(int):
    if number % 2 == 0 : 
        return "even"
    elif number % 2 != 0 :  
        return "odd" 
    else : 
        return "Number must be zero."

    
if __name__ == "__main__" : 
    number = int(input("Enter any number to check even or odd: "))

    oddeven = Odd_Even(int) 

    print(f"Number {number} is {oddeven}.")