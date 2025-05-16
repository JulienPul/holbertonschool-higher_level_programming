#!/usr/bin/python3
"""5-text_indentation
function that prints a text with 2 new lines after each of these characters: ., ? and :"""


def text_indentation(text):

    """Write a function that prints a text with 2 new lines after each of these characters: ., ? and :
Prototype: def text_indentation(text):"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in text:
        if i in [".", "?", ":", ","]:
            print("{}".format(i), end="\n")
        else:
            print("{}".format(i), end="")
