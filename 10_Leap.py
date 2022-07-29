
def LeapYear(int):
    if year % 4 == 0 : 
        if year % 100 ==0 : 
            if year % 400 == 0 : 
                return "Leap year" 
            else : 
                return "Not a leap year"
        else : 
            return "Not a leap year"
    else : 
        return "Not a leap year"

if __name__ == "__main__" : 
    year = int(input("Enter an year to check leap or not: "))

    leap_yr = LeapYear(int)

    print(f"{year} is {leap_yr}.")