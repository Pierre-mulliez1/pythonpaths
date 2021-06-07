"""
IE titanic utls
"""

__version__ = "0.1.0"


def tokenize(text):
    print("splitted")
    return text.split()

if __name__ == "__main__":
    print(tokenize("am I splitted?"))