import sys
import math
import re


__all__ = ["listele"]


def listele(li:list|dict, column:int, /, *, spaces:int=30, find:str="", regex:str="", reverse:bool=False):
    """
    listele(li:list|dict, column:int, /, *, spaces:int=30, find:str="", regex:str="", reverse:bool=False)

    - li      : An iterable
    - column  : Output column number
    - spaces  : Spaces between elements
    - find    : Filters the output with given string
    - regex   : Filters the output with given regex
    - reverse : Prints elements top to bottom instead of left to right
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
        li = list(map(str, li))


    if find:
        find = find.lower()
        li = [i for i in li if find in i.lower()]


    if regex:
        compiled = re.compile(regex)
        li = [i for i in li if compiled.match(i)]



    length = len(li)


    if (
        not isinstance(column, int)
        or not isinstance(spaces, int)
        or column < 1
        or spaces < 0
    ):
        print("E: Incorrect arguments.", file=sys.stderr)
        return


    # If the list is empty print a new line and do nothing
    if length == 0:
        print()
        return

    if (column > length):
        column = length


    number_of_groups = math.ceil(length / column)

    control = (length > ((column - 1) * number_of_groups))
    # Print list elements top to bottom
    # It is not supported for all length and column values
    if reverse and control:
        _print_top_to_bottom(li, length, number_of_groups, column, spaces)

    # Print list elements left to right
    else:
        if reverse and not control:
            print("W: Reverse not supported for this input", file=sys.stderr)

        _print_left_to_right(li, length, column, spaces)



def _print_top_to_bottom(
        li: list,
        list_length: int,
        number_of_lines: int,
        column: int,
        spaces: int
):
    printed = 0
    index = 0
    while printed != list_length:
        token = li[index]

        end_of_line = (not ((printed + 1) % column))

        # Pad the token with spaces to maintain column alignment
        if not end_of_line:
            token = token.ljust(spaces)

        print(token, end=("\n" if end_of_line else ""))
        printed += 1

        index += number_of_lines
        while index >= list_length:
            index -= column * number_of_lines
            index += 1

    if not end_of_line:
        print()



def _print_left_to_right(
        li: list,
        list_length: int,
        column: int,
        spaces: int
):
    for index in range(list_length):
        token = li[index]

        end_of_line = (not ((index + 1) % column))

        # Pad the token with spaces to maintain column alignment
        if not end_of_line:
            token = token.ljust(spaces)

        print(token, end=("\n" if end_of_line else ""))

    if not end_of_line:
        print()

