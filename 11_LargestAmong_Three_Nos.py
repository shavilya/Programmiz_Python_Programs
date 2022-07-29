
def Largest():
    if a > b and a > c :
        return a 
    elif b > a and b > c : 
        return b 
    else : 
        return c 
 
if __name__ == "__main__" : 
    a,b,c = map(int , input("Enter any three numbers to see which is largest: ").split(" "))

    l = Largest()

    print(f"{l} is largest amoung {a},{b} and {c}.")

