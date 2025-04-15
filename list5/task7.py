"""
Write a function that checks if words given as arguments are anagrams
"""
def anagram_check(words):
    sorted_words = [sorted(x) for x in words]
    if all(x == sorted_words[0] for x in sorted_words):
        return True
    else:
        return False

slowa = ['baba', 'abab', 'aabb', 'abba']
print(anagram_check(slowa))