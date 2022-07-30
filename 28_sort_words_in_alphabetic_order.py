
# Python program to sort words in alphabetic order. 



def sort(list):
    list_of_words.sort()
    return list_of_words 

if __name__ == "__main__" : 
    global list_of_words


    words = map(str,input("Enter words to arrange in alphabetic order: ").split(" "))
    list_of_words = list(words)

    sorted_function = sort(list) 

    print(f"Sorted list of words: {sorted_function}")
