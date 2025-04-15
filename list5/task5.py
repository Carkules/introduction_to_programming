"Write a function which checks if a word given as an argument is a palindrome."

def palindrome_check(word):
    return word==word[::-1]

print(palindrome_check('kajak'))