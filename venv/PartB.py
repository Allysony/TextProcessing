"""

@author Allyson Yamasaki
Date Created: Jan 15, 2020

Assignment 1: Text Processing
Part B
"""

"""
Runtime Complexity Analysis:
    The function runs in a worst case time of O(N). This linear time complexity is due to reading every character
    in the file once and checking if the character is alpha-numeric. As the size of the input increases, the runtime 
    will also increase linearly accordingly. Other aspects of the function such as comparing if a character is 
    alphanumeric and adding words to the result set runs in a worst case time complexity of O(1). 
    Thus in total, O(N) * O(1) * O(1) * O(1), which is the same as O(N).
    
    It is important to note that the use of a set instead of a list was done because even though a list could get
    unique words with a simple if statement to check if it was in the list, by using a set the function has avoided an
    unnecessary check with a worst case time complexity of O(N)
    
"""
def tokenize(textFilePath: str):
    result = set()
    file = open(textFilePath, "r")
    tempWord = ""
    for line in file:
        for char in line:
            if char.isalnum():
                tempWord += char
            else:
                if tempWord != '':
                    result.add(tempWord.lower())
                    tempWord = ""
        if tempWord != "":
            result.add(tempWord.lower())
            tempWord = ""
    return result

"""
Runtime Complexity Analysis 
    The function has a worst case time complexity of O(N^2). This is due to comparing the intersection of words by
    iterating through one set of words and checking if it is in the other set. 
    
    By using a set, the function compares the two files in an average time complexity of Θ(1) and a worst case of O(N). 
    The function also iterates the smaller of the two files when comparing to minimize the number of iterations necessary.
    This is demonstrated with 
    
                        O(2N)  + O(N^2)                  = O(N^2) 
                    tokenizing + comparing tokens
"""
def intersectWordFreq(a: str, b: str):
    count = 0
    a_text, b_text = tokenize(a), tokenize(b)
    # iterating through the smaller file to compare words
    if len(a_text) < len(b_text):
        for i in a_text:
            if i in b_text:
                count += 1
                b_text.remove(i)
                print(i)
    else:
        for i in b_text:
            if i in a_text:
                count += 1
                a_text.remove(i)
                print(i)
    return count


"""
Runtime Complexity Analysis 
    The function has a worst case time complexity of O(N^2). This is due to comparing the intersection of words by
    iterating through one set of words and checking if it is in the other set. 
"""
if __name__ == '__main__':
    """
    /Users/allysonyamasaki/PycharmProjects/TextProcessing/venv/world192.txt
    /Users/allysonyamasaki/PycharmProjects/TextProcessing/venv/bible.txt
    """

    fileA = input()
    fileB = input()
    try:
        print(intersectWordFreq(fileA, fileB))
    except FileNotFoundError:
        print("ERROR. FILE NOT FOUND")
