"""
IE titanic utls
"""

__version__ = "0.1.0"


def tokenize(lis):
    # Following function not used
    def listToString(l):
        l = ""
        for ele in l:
            l += ele
        return l

    text = listToString(lis)

    print("splitted")
    # select directly the first element of system.arg
    return lis[1].split()


if __name__ == "__main__":
    print(tokenize("am I splitted?"))
