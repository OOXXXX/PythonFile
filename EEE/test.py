import random
import statistics


class NumberList:
    def __init__(self):  # the class constructor
        self.__data = []  # initialises the __data “private” instance variable to an empty list

    def getData(self):
        return self.__data  # returns the contained data list to users of the class

    def setData(self, data):
        self.__data = data  # initialises the list with “externally-created” data

    # additional NumberList class methods
    def getdatalength(self):  # “private” method names in Python start with __
        print("Enter the number of data set elements: ")
        length = 0
        gotlengthCorrectly = False  # a flag to loop until we get length correctly
        while gotlengthCorrectly == False:
            try:
                length = float(input())  # read from the keyboard, accept also strings & convert
                if length % 1 == 0 and length >= 2:  # check for integer input >= 2
                    gotlengthCorrectly = True
                else:
                    print("__getdatalength: length should be >=2")
            except (ValueError, SyntaxError):
                print("__getdatalength: length should be an integer!")
        # end while loop
        return int(length)  # return length as int

    def getDataFromKeyboard(self):
        length = self.getdatalength()
        print("Enter the value of data: ")
        number = 0
        datalist = []
        gotarray = False
        for i in range(length):
            while gotarray == False:
                try:
                    value = float(input())
                    gotarray = True
                except(ValueError, SyntaxError):
                    print("__getdatalength: length should be a float number!")
            datalist.append(value)
        NumberList.setData(datalist)

    # here you should write code that gets exactly length numbers from the keyboard
    # and adds them to the __data instance variable using the list append method;
    # you will need a while loop in similar fashion to __getdatalength


def mean(data):
    meanValue = sum(data) / len(data)
    return float(meanValue)


# mean function

def variance(data):
    varianceValue = []
    for i in range(len(data)):
        varianceValue.append((data[i] - mean(data)) ** 2)
        finalvariance = sum(varianceValue) / (len(data) - 1)
    return float(finalvariance)


# variance function

def main():
    mydata = [0.1, 1.1, 2.1, 3.1, 4.1]  # hardcoded data set values, list with 5 elements
    nlist = NumberList()  # create new empty NumberList object instance
    # nlist.setData(mydata) # fill it in with the data set
    nlist.getDataFromKeyboard()
    print("Numbers: " + str(nlist.getData()))  # print the data set
    print("Mean: " + str(mean(nlist.getData())))  # calculate and print mean
    print("Variance: " + str(variance(nlist.getData())))  # calculate and print variance


main()

# if __name__ == "__main__":
#  main()