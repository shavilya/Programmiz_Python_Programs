

# Python program to check if the string is pallindrome or not. 


def is_pallindrome(string) :
    left_string = ''
    right_string = ''
    half_string = int(len(string)) // 2 
    
    left_string = string[:half_string]
    right_string = string[half_string+1:len(string)]

    print(left_string)
    print(right_string)
    if left_string == right_string[::-1] : 
        return "Pallindrome"
    else : 
        return "not Pallindrome"

if __name__ == "__main__" : 
    string = input("Enter string to check pallindrome or not: ")

    pallindrome = is_pallindrome(string)

    print(f"{string} is {pallindrome}")

