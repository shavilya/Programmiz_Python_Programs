



# Python program to remove punctuation from the given string.
from string import punctuation

if __name__ == "__main__" : 
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    string = input("Enter any string to remove punctuations: ")
    resulted_string = "" 

    for i in string : 
        if i not in punctuation : 
            resulted_string = resulted_string + i  

print(f"String without punctuations:\n{resulted_string}")


