'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    
    if len(word) < 2: # base case once word is less then 2 it ends the function
        return 0
    elif word[0] + word[1] == 'th': #compares the index of the first two letters
        return 1 + count_th(word[1:]) #if comparison is true return 1 and split the word at index 1 to the end.

    else:
        return count_th(word[1:]) #else adds function to call stack and splits the word at index 1 to continue comparing, goes through call stack at the end and add up the returns from the call stack

