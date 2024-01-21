import math

class Shape:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def toString(self):
        return "Shape(Name: {})".format(self.name)

    def getArea(self):
        raise NotImplementedError

    def getVolume(self):
        raise NotImplementedError

class Point(Shape):
    def __init__(self, x, y):
        super().__init__("Point")
        self.x = x
        self.y = y

    def toString(self):
        return "Point(x: {}, y: {})".format(self.x, self.y)

    def getArea(self):
        return 0

    def getVolume(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def toString(self):
        return "Circle(radius: {})".format(self.radius)

    def getArea(self):
        return math.pi * self.radius ** 2

    def getVolume(self):
        return 0

class Cylinder(Shape):
    def __init__(self, radius, height):
        super().__init__("Cylinder")
        self.radius = radius
        self.height = height

    def toString(self):
        return "Cylinder(radius: {}, height: {})".format(self.radius, self.height)

    def getArea(self):
        return 2 * math.pi * self.radius * self.height + 2 * math.pi * self.radius ** 2

    def getVolume(self):
        return math.pi * self.radius ** 2 * self.height

class Sphere(Shape):
    def __init__(self, radius):
        super().__init__("Sphere")
        self.radius = radius

    def toString(self):
        return "Sphere(radius: {})".format(self.radius)

    def getArea(self):
        return 4 * math.pi * self.radius ** 2

    def getVolume(self):
        return (4/3) * math.pi * self.radius ** 3

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width

    def toString(self):
        return "Rectangle(length: {}, width: {})".format(self.length, self.width)

    def getArea(self):
        return self.length * self.width

    def getVolume(self):
        return 0

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.name = "Square"

    def toString(self):
        return "Square(side: {})".format(self.length)

class Cube(Square):
    def __init__(self, side):
        super().__init__(side)
        self.name = "Cube"

    def getArea(self):
        return 6 * self.length ** 2

    def getVolume(self):
        return self.length ** 3


def create_shape():
    # 通过用户输入创建形状实例
    pass

def print_shapes(shapes):
    # 打印形状列表
    for shape in shapes:
        print(shape.toString())

def remove_shape(shapes):
    # 从列表中删除形状
    pass

def modify_shape(shapes):
    # 修改特定的形状
    pass

def main():
    shapes = []
    while True:
        print("1. Create a new shape")
        print("2. Print all shapes")
        print("3. Remove a shape")
        print("4. Modify a shape")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            shape = create_shape()
            shapes.append(shape)
        elif choice == '2':
            print_shapes(shapes)
        elif choice == '3':
            remove_shape(shapes)
        elif choice == '4':
            modify_shape(shapes)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
