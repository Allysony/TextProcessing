"""

@author Allyson Yamasaki
Date Created: Jan 15, 2020

Assignment 1: Text Processing
Part A

"""
# -------------------Method/Function: List<Token> tokenize(TextFilePath)--------------------------------
"""
Runtime Complexity Analysis:
    The function runs in a worst case time of O(N). This linear time complexity is due to reading every character
    in the file once and checking if the character is alpha-numeric. As the size of the input increases, the runtime 
    will also increase linearly accordingly. Other aspects of the function such as comparing if a character is 
    alphanumeric and appending words to the result list runs in a worst case time complexity of O(1). 
    Thus in total, O(N) * O(1) * O(1) * O(1), which is the same as O(N) .
"""
def tokenize(textFilePath: str):
    """
    :param textFilePath: str of a text file
    :return result: list of tokens
    """
    result = []
    file = open(textFilePath, "r")
    tempWord = ""
    for line in file:
        for char in line:
            if char.isalnum():
                tempWord += char
            else:
                if (tempWord != ''):
                    result.append(tempWord.lower())
                    tempWord = ""
        if tempWord != "":
            result.append(tempWord.lower())
            tempWord = ""
    return result
# ------------------Method/Function:  Map<Token,Count> computeWordFrequencies(List<Token>)----------------------------
"""
Runtime Complexity Analysis
    The function runs in a worst case time complexity of O(N). This is the time necessary for the function to 
    iterate through the list in order to count the word frequencies. In order to properly increment the count 
    of each word, I utilized dict.get(key) to keep the time complexity at a worst case of O(1) rather than 
    iterating through the dictionary to check if each word was a new word. This O(1) time complexity for
    checking if an key is in a dictionary is made possible because dictionaries rely on hash functions and hash
    codes to get and set items. By implementing this, the time complexity for this function was able to maintain
    linear time for its worst case.
"""
def computeWordFrequencies(tokenArr: []):
    """
    :param tokenArr: list of tokens
    :return wordFreq: map of [token, frequency]
    """
    wordFreq = {}
    for i in tokenArr:
        if wordFreq.get(i):
            wordFreq[i] += 1
        else:
            wordFreq[i] = 1
    return wordFreq

"""
Runtime Complexity Analysis
    This function runs in O(N) time. In order to print each item in the dictionary, a For Loop is required, which runs
    in a worst case time of O(N) time. 
"""
def printFormat(wordFreq: dict):
    """
    :param wordFreq: dict of word frequencies
    :return:
    """
    for (k, v) in wordFreq.items():
        print("%s -> %d" % (k, v))

"""
Runtime Complexity Analysis
    The time complexity for our main statement is basically the accumulation of the analysis done in the above functions.
    The main function runs in a worst case time complexity of O(N) + O(N) + O(N), which means that it runs in 
    O(N). 
"""
if __name__ == '__main__':
    file = input()
    try:
        printFormat(computeWordFrequencies(tokenize(file)))
    except FileNotFoundError:
        print("ERROR. FILE NOT FOUND")

    # the program handles non alphanumeric in tokenize function, creating an exception would lead to unwanted and
    #  un-needed error messages to the console.

