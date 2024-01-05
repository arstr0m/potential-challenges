"""Capital indexes
Write a function named capital_indexes. The function takes a single parameter, which is a string. Your function should return a list of all the indexes in the string that have capital letters.

For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4]."""


def capital_indexes(text):
    index = []
    count = 0
    for char in text:
        if char.isupper():
            index.append(count)
        count+=1
    return index

print(capital_indexes("HeLlO"))


