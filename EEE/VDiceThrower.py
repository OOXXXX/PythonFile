import sys
import random

def get_valid_input(prompt, condition):
    while True:
        try:
            value = int(input(prompt))
            if condition(value):
                return value
            else:
                print("Invalid input, please try again.")
        except ValueError:
            print("Input should be a number, please try again.")

def main():
    print("Please enter the number of sides on the dice:")
    nfaces = get_valid_input("Number of sides: ", lambda x: x >= 2)
    print("Please enter the number of throws:")
    nthrows = get_valid_input("Number of throws: ", lambda x: x > 0 and x % nfaces == 0)

    # Initialize a list to count occurrences of each side
    face_counts = [0] * nfaces

    for _ in range(nthrows):
        side = random.randint(1, nfaces)
        face_counts[side - 1] += 1

    for side, count in enumerate(face_counts, 1):
        print(f"Side {side} came up {count} times.")

if __name__ == "__main__":
    main()
