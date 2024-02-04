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
        area = self.get_area()
        return "Circle(radius: {}), Area: {:.2f}".format(self.radius, area)

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
        area = self.get_area()
        volume = self.get_volume()
        return "Cylinder(radius: {}, height: {}), Surface Area: {:.2f}, Volume: {:.2f}".format(self.radius, self.height, area, volume)

    def get_area(self):
        return 2 * math.pi * self.radius * self.height + 2 * math.pi * self.radius ** 2

    def get_volume(self):
        return math.pi * self.radius ** 2 * self.height

class Sphere(Shape):
    def __init__(self, radius):
        super().__init__("Sphere")
        self.radius = radius

    def __str__(self):
        area = self.get_area()
        volume = self.get_volume()
        return "Sphere(radius: {}), Surface Area: {:.2f}, Volume: {:.2f}".format(self.radius, area, volume)

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
        area = self.get_area()
        return "Rectangle(length: {}, width: {}), Area: {:.2f}".format(self.length, self.width, area)

    def get_area(self):
        return self.length * self.width

    def get_volume(self):
        return 0

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.side = side

    def __str__(self):
        area = self.get_area()
        return "Square(side: {}), Area: {:.2f}".format(self.side, area)

class Cube(Square):
    def __init__(self, side):
        super().__init__(side)

    def __str__(self):
        area = self.get_area()
        volume = self.get_volume()
        return "Cube(side: {}), Surface Area: {:.2f}, Volume: {:.2f}".format(self.side, area, volume)

    def get_area(self):
        return 6 * self.side ** 2

    def get_volume(self):
        return self.side ** 3

def is_valid_input(value):
    if value <= 0:
        print("Invalid input. Value must be greater than 0.")
        return False
    return True

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

    try:
        if shape_choice == '1':
            x = float(input("Enter x coordinate: "))
            y = float(input("Enter y coordinate: "))
            return Point(x, y)
        elif shape_choice in ['2', '4']:
            radius = float(input("Enter radius: "))
            if is_valid_input(radius):
                return Circle(radius) if shape_choice == '2' else Sphere(radius)
        elif shape_choice in ['3', '5', '6', '7']:
            if shape_choice == '3':  # Cylinder
                radius = float(input("Enter radius: "))
                height = float(input("Enter height: "))
                if is_valid_input(radius) and is_valid_input(height):
                    return Cylinder(radius, height)
            else:  # Rectangle, Square, or Cube
                length = float(input("Enter length: ")) if shape_choice in ['5', '6'] else float(input("Enter side length: "))
                width = float(input("Enter width: ")) if shape_choice == '5' else length
                if is_valid_input(length) and (is_valid_input(width) or shape_choice in ['6', '7']):
                    return Rectangle(length, width) if shape_choice == '5' else (Square(length) if shape_choice == '6' else Cube(length))
    except ValueError:
        print("Please enter a valid number.")

    print("Invalid choice or input.")
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
        index = int(input("Enter the index of the shape to remove: "))
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
        index = int(input("Enter the index of the shape to modify: "))
        if 0 <= index < len(shapes):
            shape = shapes[index]
            if isinstance(shape, Point):
                x = float(input("Enter new x coordinate: "))
                y = float(input("Enter new y coordinate: "))
                shape.x = x
                shape.y = y
            elif isinstance(shape, Circle) or isinstance(shape, Sphere):
                radius = float(input("Enter new radius: "))
                if is_valid_input(radius):
                    shape.radius = radius
            elif isinstance(shape, Cylinder):
                radius = float(input("Enter new radius: "))
                height = float(input("Enter new height: "))
                if is_valid_input(radius) and is_valid_input(height):
                    shape.radius = radius
                    shape.height = height
            elif isinstance(shape, Rectangle) or isinstance(shape, Square) or isinstance(shape, Cube):
                length = float(input("Enter new length: "))
                if shape.__class__ == Rectangle:
                    width = float(input("Enter new width: "))
                    if is_valid_input(length) and is_valid_input(width):
                        shape.length = length
                        shape.width = width
                else:  # Square or Cube
                    if is_valid_input(length):
                        shape.length = length
                        shape.width = length
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
