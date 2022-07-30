
# Python program to count vowels. 

def count_vowels(lower_string):

    no_vowels = 0
    vowel_count = 0 
     
    for i in input_string : 
        if i not in vowels : 
            no_vowels += 1 
        else : 
            vowel_count += 1 
    return vowel_count 


if __name__ == "__main__" : 
    input_string = "Enter any string to check vowel"
    vowels = 'aeiou'
    lower_string = input_string.lower()

    cv = count_vowels(input_string) 

    print(f"Number of vowels in the string are:{cv}")

