from turtle import Turtle

def regular_polygon(t: Turtle, length: int, num_sides = 4) -> None:
    """
    Draw a regular polygon with given length and number of sides
    :param t: an instance of turtle used
    :param length: the length of the side of a regular polygon
    :param num_sides: the number of sides of this regular polygon
    :return: None
    """
    if num_sides == 3:
        triangle(t, length)
    elif num_sides == 4:
        square(t, length)
    elif num_sides == 6:
        hexagon(t, length)
    elif num_sides == 8:
        octagon(t, length)
    elif num_sides is int:
        for count in range(num_sides):
            t.forward(length)
            t.left(360/num_sides)

def square(t: Turtle, length: int) -> None:
    """
    Draw a square with given length
    :param t: an instance of a Turtle used
    :param length: the length of the side of a square
    :return: None
    """
    for count in range(4):
        t.forward(length)
        t.left(90)

def hexagon(t: Turtle, length: int) -> None:
    """
    Draw a hexagon with given length
    :param t: an instance of Turtle used
    :param length: the length of the side of a hexagon
    :return: None
    """
    for count in range(6):
        t.forward(length)
        t.left(60)

def triangle(t: Turtle, length: int) -> None:
    """
    Draw a triangle with given length
    :param t: an instance of Turtle used
    :param length: the length of the side of a triangle
    :return: None
    """
    for count in range(3):
        t.forward(length)
        t.left(120)

def octagon(t: Turtle, length: int) -> None:
    """
    Draw a triangle with given length
    :param t:
    :param length:
    :return:
    """
    for count in range(8):
        t.forward(length)
        t.left(45)

def main():
    t = Turtle.turtle


if __name__ == "__main__":
    main()