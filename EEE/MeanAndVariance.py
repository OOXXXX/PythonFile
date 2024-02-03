from NumberList import NumberList, mean, variance

def main():
    while True:  # Loop to allow retry
        print("Choose data input method:")
        print("1. Enter data manually")
        print("2. Generate random data")
        print("3. Read data from a file")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            numberList = NumberList()
            numberList.getDataFromKeyboard()
            data = numberList.getData()
            break
        elif choice == '2':
            try:
                ndata = int(input("How many random data points? "))
                range1 = float(input("Enter the lower range: "))
                range2 = float(input("Enter the upper range: "))
                numberList = NumberList()
                numberList.getRandomData(ndata, range1, range2)  # make sure ndata, range1, and range2 are valid
                data = numberList.getData()
                break
            except ValueError:
                print("Invalid input for random data. Please enter valid numbers.")
        elif choice == '3':
            try:
                fileName = input("Enter the file name: ")
                numberList = NumberList()
                if not numberList.getDataFromFile(fileName):  # Assuming getDataFromFile returns False if file not found
                    raise FileNotFoundError
                data = numberList.getData()
                break
            except FileNotFoundError:
                print("File not found. Please check the file name and try again.")
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

    print("Data:", data)
    print("Mean:", mean(data))
    print("Variance:", variance(data))

if __name__ == "__main__":
    main()
