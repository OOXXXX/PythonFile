import sys
import random

def main():
    nthrows = 0
    print("Please enter the number of throws:")
    try:
        nthrows = int(input())  # input returns a string, e.g. "4" - convert to int
    except (ValueError, SyntaxError):
        print("nthrows should be a number, program exiting!")
        sys.exit()

    if nthrows < 2 or nthrows % 2 != 0:
        print("nthrows should be >= 2 and also multiple of 2, program exiting!")
        sys.exit()

    faceUp = faceDown = 0

    # random.seed(100)  # may set a seed for result reproducibility

    for i in range(nthrows):
        if random.randrange(0, 2) == 0:  # produces 0 or 1
            # could have also used randint(0, 1)
            faceDown += 1  # there is no ++ operator in Python
        else:
            faceUp += 1  # ditto

    print("faceUp came " + str(faceUp) + " times")
    print("faceDown came " + str(faceDown) + " times")

if __name__ == "__main__":
    main()
