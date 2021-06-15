"""
IE titanic utls
"""

__version__ = "0.1.0"


def tokenize(lis, lower = "F"):
    # Following function not used
    def listToString(l):
        l = ""
        for ele in l:
            l += ele
        return l
    
    text = listToString(lis)
    if lis == "T":
        lis.lower()
    
    # select directly the first element of system.arg
    return lis.split()


if __name__ == "__main__":
    print(tokenize("am I splitted?"))
