import random

class NumberList:
    def __init__(self):
        self.__data = []

    def getData(self):
        return self.__data

    def setData(self, data):
        self.__data = data

    @staticmethod
    def __getNDataFromKeyboard():
        print("Enter the number of data set elements: ")
        while True:
            try:
                ndata = int(input())
                if ndata >= 2:
                    return ndata
                else:
                    print("__getNDataFromKeyboard: ndata should be >=2")
            except ValueError:
                print("__getNDataFromKeyboard: ndata should be an integer!")

    def getDataFromKeyboard(self):
        ndata = self.__getNDataFromKeyboard()
        for _ in range(ndata):
            while True:
                try:
                    value = float(input("Enter a number: "))
                    self.__data.append(value)
                    break
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")

    def getRandomData(self, ndata, range1, range2=0):
        if range2 and range1 >= range2:
            print("Error: range1 must be less than range2")
            return
        low, high = (range1, range2) if range2 else (0, range1)
        self.__data = [random.uniform(low, high) for _ in range(ndata)]

    def getDataFromFile(self, fileName):
        with open(fileName, 'r') as file:
            for line in file:
                try:
                    self.__data.append(float(line.strip()))
                except ValueError:
                    pass  # Ignore lines that can't be converted to float

# separate mean and variance function
def mean(data):
    return sum(data) / len(data) if data else 0

def variance(data):
    m = mean(data)
    return sum((x - m) ** 2 for x in data) / len(data) if data else 0
