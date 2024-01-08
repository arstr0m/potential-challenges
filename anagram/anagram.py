"""
Anagrams
Two strings are anagrams if you can make one from the other by rearranging the letters.

Write a function named is_anagram that takes two strings as its parameters. Your function should return True if the strings are anagrams, and False otherwise.

For example, the call is_anagram("typhoon", "opython") should return True while the call is_anagram("Alice", "Bob") should return False.
"""
"""tambien existe lista.sort()"""
"""split parte la string con un identificador , split(string, ",")"""
def is_anagram(first_text, second_text):
    if sorted(list(second_text)) == sorted(list(first_text)):
        return True
    else: 
        return False