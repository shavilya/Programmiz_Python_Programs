# Python program to create a simple calculator. 

def calculator(option,number1,number2): 
    if option == 1 : 
        return number1 + number2 
    elif option == 2 : 
        return number1 - number2 
    elif option == 3 : 
        return number1 * number2 
    elif option == 4 : 
        return number1/number2 


if __name__ == "__main__" : 
    print("""Type any number to choose options,
            1.Addition 
            2.Substraction
            3.Multiplication
            4.Division""")
    option = int(input("Enter option: "))
    number1,number2 = map(int,input("Enter values of two numbers for calculation: ").split(" "))

    

    cal = calculator(option,number1,number2)

    print(f"Output: {cal}")