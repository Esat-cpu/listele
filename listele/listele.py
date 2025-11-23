# Bir listenin elemanlarını kolonlar halinde sıralayan fonksiyon:

import sys
from math import ceil

def listele(li:list|dict, kolon:int, ljustmz:int=30, *, find:str="", reverse:bool=False):
    """ listele(li:list|dict, kolon:int, ljustmz:int=30, *, find:str="", reverse:bool=False)

    Usage example:

    from listele import listele

    import sysconfig
    li = dir(sysconfig)  # list type object
    di = sysconfig.get_paths()  # dict type object

    print("Output1:")
    listele(li, 4)

    print("\n\nOutput2:")
    listele(li, 4, find="path")

    print("\n\nOutput3:")
    listele(di, 2, 70)

    print("\n\nOutput4:")
    listele(di, 1, find="include")

    print("\n\nOutput5:")
    listele([1, 2, 3, 4, 5], 3, reverse=True)
    """

    try:
        iter(li)
    except TypeError:
        print("E: Non-iterable argument was given.", file= sys.stderr)
        return


    # convert li to a list
    if isinstance(li, dict):
        li = [f"{key}: {item}" for key, item in li.items()]
    else:
        li = list(li)


    if find:
        find = find.lower()
        li = [i for i in li if find in i.lower()]


    lenght = len(li)


    if (
        not isinstance(kolon, int)
        or not isinstance(ljustmz, int)
        or 1 >= kolon > length
        or ljustmz < 0
    ):
        print("E: Incorrect arguments.", file= sys.stderr)
        return


    # print list elements left to right
    # 'kolon' represents the number of columns
    if not reverse:
        for i in range(0, (length - kolon+1), kolon):
            for j in range(kolon):
                ind = i + j
                st = str(li[ind])

                if (ind+1) % kolon != 0:
                    st = st.ljust(ljustmz)
                print(st, end="")
            print()


        remainder = length % kolon
        if remainder:
            for i in range(remainder, 0, -1):
                st = str(li[-i]).ljust(ljustmz)
                print(st, end="")
            print()

    # print list elements top to bottom
    # now 'kolon' represents the number of lines
    else:
        for i in range(kolon):
            column = ceil(length / kolon)
            for j in range(column):
                ind = kolon * j + i

                if ind >= length: break

                st = str(li[ind])

                if j != column -1:
                    st = st.ljust(ljustmz)
                print(st, end="")
            print()

            if i >= length: break

