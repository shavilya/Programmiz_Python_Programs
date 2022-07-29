# Write a Python program to convert kilometers to miles and celsius to fahrenheit 

def kilometer(float):
    return kilometers * 0.62 

def Celsius(float):
    return (celsius * 9/5) + 32 


if __name__ == "__main__" : 
    kilometers =  float(input("Enter a number in kilometers to convert to miles: "))
    celsius = float(input("Enter a number in celsius to convert to fahrenheit: "))

    Kilo_to_miles = kilometer(float)
    Celsius_to_fahrenheit = Celsius(float)

    print("{} Kilometers = {} miles.".format(kilometers,Kilo_to_miles))
    print("{} celsius = {} fahrenheit.".format(celsius,Celsius_to_fahrenheit))