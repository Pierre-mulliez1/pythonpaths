import sys
import ie_utils

# The python -m ie_utils command will first call __main__ by default if no other module is specified


def main():
    print(sys.argv)
    print(ie_utils.tokenize(sys.argv))
