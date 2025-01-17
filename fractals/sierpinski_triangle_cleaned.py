
import sys
import turtle

PROGNAME = "Sierpinski Triangle"

points = [[-175, -125], [0, 175], [175, -125]]  


def getMid(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)  


def triangle(points, depth):

    myPen.up()
    myPen.goto(points[0][0], points[0][1])
    myPen.down()
    myPen.goto(points[1][0], points[1][1])
    myPen.goto(points[2][0], points[2][1])
    myPen.goto(points[0][0], points[0][1])

    if depth > 0:
        triangle(
            [points[0], getMid(points[0], points[1]), getMid(points[0], points[2])],
            depth - 1,
        )
        triangle(
            [points[1], getMid(points[0], points[1]), getMid(points[1], points[2])],
            depth - 1,
        )
        triangle(
            [points[2], getMid(points[2], points[1]), getMid(points[0], points[2])],
            depth - 1,
        )


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise ValueError(
            "right format for using this script: "
            "$python fractals.py <int:depth_for_fractal>"
        )
    myPen = turtle.Turtle()
    myPen.ht()
    myPen.speed(5)
    myPen.pencolor("red")
    triangle(points, int(sys.argv[1]))
