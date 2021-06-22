"""
IE titanic utls
"""

__version__ = "0.1.0"

from nltk.corpus import stopwords
#nltk.download('stopwords')


def tokenize(lis, lower = "F"):
    # Following function not used
    def listToString(l):
        l = ""
        for ele in l:
            l += ele
        return l
    
    text = listToString(lis)
    if lower == "T":
        lis = lis.lower()
    
    # select directly the first element of system.arg
    return lis.split()


def remove_stopwords(text):
    text_tokens = tokenize(text)
    stopwords = ["a", "the", "or", "and"]
    tokens_without_sw = [word for word in text_tokens if not word in stopwords]
    return tokens_without_sw

def remove_punctuation(text):
    text_tokens = tokenize(text)
    punctuation = [".", ",", "!"]
    tokens_without_punc = [word for word in text_tokens if not word in punctuation]
    return tokens_without_punc

if __name__ == "__main__":
    print(tokenize("am I splitted?"))
