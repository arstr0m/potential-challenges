"""
Write a function named add_dots that takes a string and adds "." in between each letter. For example, calling add_dots("test") should return the string "t.e.s.t".

Then, below the add_dots function, write another function named remove_dots that removes all dots from a string. For example, calling remove_dots("t.e.s.t") should return "test".

If both functions are correct, calling remove_dots(add_dots(string)) should return back the original string for any string.

(You may assume that the input to add_dots does not itself contain any dots.)


"""


def add_dots(main_text):
    added_dots =""
    position = 0
    for char in main_text:
        if ((position != len(main_text)-1)):
            added_dots += char + "."
            position +=1
        else:
            added_dots += char
    return added_dots

def remove_dots(main_text):
    return main_text.replace(".","")