# function definition
def calculate_circle_area(radius):
    PI = 3.14
    area = PI*(radius*radius)
    print("Circle radius {}, area is {}".format(radius, area))

def calculate_circle_circumference(radius):
    PI = 3.14
    circumference = 2*PI*radius
    print("Circle radius {}, circumferemce is {}".format(radius, circumference))

def calculate_rectangle_area(wide, length):
    area = wide*length
    print("Rectangle area of {}X{} is {}".format(wide, length, area))

def calculate_triangle_area(base, high):
    area = 0.5*base*high
    print("Triangle area of {}X{} is {}".format(base, high, area))