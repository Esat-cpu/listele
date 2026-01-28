import sys
import math


__all__ = ["listele"]


def listele(li:list|dict, column:int, /, *, spaces:int=30, find:str="", reverse:bool=False):
    """
    listele(li:list|dict, column:int, /, *, spaces:int=30, find:str="", reverse:bool=False)

    - li      : An iterable
    - column  : Output column number
    - spaces  : Spaces between elements
    - find    : Filters the output with given string
    - reverse : Prints elements top to bottom instead of left to right (disabled by default)
    """

    try:
        iter(li)
    except TypeError:
        print("E: Non-iterable argument was given.", file= sys.stderr)
        return


    # Convert li to a list
    if isinstance(li, dict):
        li = [f"{key}: {item}" for key, item in li.items()]
    else:
        li = list(li)


    if find:
        find = find.lower()
        li = [i for i in li if find in i.lower()]


    length = len(li)


    if (
        not isinstance(column, int)
        or not isinstance(spaces, int)
        or 1 >= column
        or spaces < 0
    ):
        print("E: Incorrect arguments.", file=sys.stderr)
        return


    if (column > length):
        column = length


    number_of_groups = math.ceil(length / column)

    control = (length > ((column - 1) * number_of_groups))
    # Print list elements top to bottom
    # It is not supported for all length and column values
    if reverse and control:

        number_of_lines = math.ceil(length / column)
        printed = 0
        index = 0
        while printed != length:
            token = str(li[index])

            end_of_line = (not ((printed + 1) % column))

            print(token, end=("\n" if end_of_line else " " * spaces))
            printed += 1

            index += number_of_lines
            while index >= length:
                index -= column * number_of_lines
                index += 1

        if not end_of_line:
            print()

    # Print list elements left to right
    else:
        if reverse and not control:
            print("W: Reverse not supported for this input", file=sys.stderr)

        for index in range(length):
            token = str(li[index])

            end_of_line = (not ((index + 1) % column))

            print(token, end=("\n" if end_of_line else " " * spaces))

        if not end_of_line:
            print()

