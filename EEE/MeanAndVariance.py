from NumberList import NumberList, mean, variance

def main():
    print("Choose data input method:")
    print("1. Enter data manually")
    print("2. Generate random data")
    print("3. Read data from a file")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        numberList = NumberList()
        numberList.getDataFromKeyboard()
        data = numberList.getData()
    elif choice == '2':
        ndata = int(input("How many random data points? "))
        range1 = float(input("Enter the lower range: "))
        range2 = float(input("Enter the upper range: "))
        numberList = NumberList()
        numberList.getRandomData(ndata, range1, range2)  # make sure ndata int
        data = numberList.getData()
    elif choice == '3':
        fileName = input("Enter the file name: ")
        numberList = NumberList()
        numberList.getDataFromFile(fileName)
        data = numberList.getData()
    else:
        print("Invalid choice.")
        return

    print("Data:", data)
    print("Mean:", mean(data))
    print("Variance:", variance(data))

if __name__ == "__main__":
    main()

