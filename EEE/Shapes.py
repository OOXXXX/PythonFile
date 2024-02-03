import math

class Shape:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def __str__(self):
        return "Shape(Name: {})".format(self.name)

    def get_area(self):
        raise NotImplementedError

    def get_volume(self):
        raise NotImplementedError

class Point(Shape):
    def __init__(self, x, y):
        super().__init__("Point")
        self.x = x
        self.y = y

    def __str__(self):
        return "Point(x: {}, y: {})".format(self.x, self.y)

    def get_area(self):
        return 0

    def get_volume(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def __str__(self):
        return "Circle(radius: {})".format(self.radius)

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_volume(self):
        return 0

class Cylinder(Shape):
    def __init__(self, radius, height):
        super().__init__("Cylinder")
        self.radius = radius
        self.height = height

    def __str__(self):
        return "Cylinder(radius: {}, height: {})".format(self.radius, self.height)

    def get_area(self):
        return 2 * math.pi * self.radius * self.height + 2 * math.pi * self.radius ** 2

    def get_volume(self):
        return math.pi * self.radius ** 2 * self.height

class Sphere(Shape):
    def __init__(self, radius):
        super().__init__("Sphere")
        self.radius = radius

    def __str__(self):
        return "Sphere(radius: {})".format(self.radius)

    def get_area(self):
        return 4 * math.pi * self.radius ** 2

    def get_volume(self):
        return (4/3) * math.pi * self.radius ** 3

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width

    def __str__(self):
        return "Rectangle(length: {}, width: {})".format(self.length, self.width)

    def get_area(self):
        return self.length * self.width

    def get_volume(self):
        return 0

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __str__(self):
        return "Square(side: {})".format(self.length)

class Cube(Square):
    def __init__(self, side):
        super().__init__(side)

    def get_area(self):
        return 6 * self.length ** 2

    def get_volume(self):
        return self.length ** 3

def create_shape():
    print("Choose the type of shape to create:")
    print("1. Point")
    print("2. Circle")
    print("3. Cylinder")
    print("4. Sphere")
    print("5. Rectangle")
    print("6. Square")
    print("7. Cube")
    shape_choice = input("Enter your choice: ")

    if shape_choice == '1':
        x = float(input("Enter x coordinate: "))
        y = float(input("Enter y coordinate: "))
        return Point(x, y)
    elif shape_choice == '2':
        radius = float(input("Enter radius: "))
        return Circle(radius)
    elif shape_choice == '3':
        radius = float(input("Enter radius: "))
        height = float(input("Enter height: "))
        return Cylinder(radius, height)
    elif shape_choice == '4':
        radius = float(input("Enter radius: "))
        return Sphere(radius)
    elif shape_choice == '5':
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        return Rectangle(length, width)
    elif shape_choice == '6':
        side = float(input("Enter side length: "))
        return Square(side)
    elif shape_choice == '7':
        side = float(input("Enter side length: "))
        return Cube(side)
    else:
        print("Invalid choice.")
        return None

def print_shapes(shapes):
    for shape in shapes:
        print(shape)

def remove_shape(shapes):
    if not shapes:
        print("No shapes to remove.")
        return

    print_shapes(shapes)
    try:
        index = int(input("Enter the index of the shape to remove (starting from 0): "))
        if 0 <= index < len(shapes):
            del shapes[index]
        else:
            print("Invalid index.")
    except ValueError:
        print("Please enter a valid integer.")

def modify_shape(shapes):
    if not shapes:
        print("No shapes to modify.")
        return

    print_shapes(shapes)
    try:
        index = int(input("Enter the index of the shape to modify (starting from 0): "))
        if 0 <= index < len(shapes):
            shape = shapes[index]
            if isinstance(shape, Point):
                x = float(input("Enter new x coordinate: "))
                y = float(input("Enter new y coordinate: "))
                shape.x = x
                shape.y = y
            elif isinstance(shape, Circle) or isinstance(shape, Sphere):
                radius = float(input("Enter new radius: "))
                shape.radius = radius
            elif isinstance(shape, Cylinder):
                radius = float(input("Enter new radius: "))
                height = float(input("Enter new height: "))
                shape.radius = radius
                shape.height = height
            elif isinstance(shape, Rectangle) or isinstance(shape, Square):
                length = float(input("Enter new length: "))
                width = float(input("Enter new width: "))
                shape.length = length
                shape.width = width
            elif isinstance(shape, Cube):
                side = float(input("Enter new side length: "))
                shape.length = side
                shape.width = side
            else:
                print("Modification not supported for this shape.")
        else:
            print("Invalid index.")
    except ValueError:
        print("Please enter a valid integer.")

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
            if shape is not None:
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
