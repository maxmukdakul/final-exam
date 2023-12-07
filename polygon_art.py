import turtle
import random


class Polygon:

    def __init__(self, num_sides, size, orientation, location, color, border_size):
        self.num_sides = num_sides
        self.size = size
        self.orientation = orientation
        self.location = location
        self.color = color
        self.border_size = border_size

    def draw_polygon(self):
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(self.num_sides):
            turtle.forward(self.size)
            turtle.left(360/self.num_sides)
        turtle.penup()

    def get_new_color(self):
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


turtle.speed(0)
turtle.bgcolor('black')
turtle.tracer(0)
turtle.colormode(255)

# draw a polygon at a random location, orientation, color, and border line thickness
art = int(input("Which art do you want to generate? Enter a number between 1 to 8,inclusive: "))
if art == 1:
    for i in range(random.randint(20, 35)):
        num_sides = random.randint(3, 3) # triangle, square, or pentagon
        size = random.randint(50, 150)
        orientation = random.randint(0, 90)
        location = [random.randint(-300, 300), random.randint(-200, 200)]
        color = [random.randint(0, 255), random.randint(0, 255), random.randint(0,255)]
        border_size = random.randint(1, 10)
        A = Polygon(num_sides, size, orientation, location, color, border_size)
        A.draw_polygon()

elif art == 2:
    for i in range(random.randint(20, 35)):
        num_sides = random.randint(4, 4) # triangle, square, or pentagon
        size = random.randint(50, 150)
        orientation = random.randint(0, 90)
        location = [random.randint(-300, 300), random.randint(-200, 200)]
        color = [random.randint(0, 255), random.randint(0, 255), random.randint(0,255)]
        border_size = random.randint(1, 10)
        A = Polygon(num_sides, size, orientation, location, color, border_size)
        A.draw_polygon()

elif art == 3:
    for i in range(random.randint(20, 35)):
        num_sides = random.randint(5, 5) # triangle, square, or pentagon
        size = random.randint(50, 150)
        orientation = random.randint(0, 90)
        location = [random.randint(-300, 300), random.randint(-200, 200)]
        color = [random.randint(0, 255), random.randint(0, 255), random.randint(0,255)]
        border_size = random.randint(1, 10)
        A = Polygon(num_sides, size, orientation, location, color, border_size)
        A.draw_polygon()

elif art == 4:
    for i in range(random.randint(20, 35)):
        num_sides = random.randint(3, 5) # triangle, square, or pentagon
        size = random.randint(50, 150)
        orientation = random.randint(0, 90)
        location = [random.randint(-300, 300), random.randint(-200, 200)]
        color = [random.randint(0, 255), random.randint(0, 255), random.randint(0,255)]
        border_size = random.randint(1, 10)
        A = Polygon(num_sides, size, orientation, location, color, border_size)
        A.draw_polygon()

elif art == 5:
    for i in range(random.randint(20, 35)):
        num_sides = random.randint(3, 3)  # triangle, square, or pentagon
        size = random.randint(50, 150)
        orientation = random.randint(0, 90)
        location = [random.randint(-300, 300), random.randint(-200, 200)]
        color = [random.randint(0, 255), random.randint(0, 255),
                 random.randint(0, 255)]
        border_size = random.randint(1, 10)
        A = Polygon(num_sides, size, orientation, location, color, border_size)
        reduction_ratio = 0.618
        A.draw_polygon()
        for j in range(1):
            turtle.penup()
            turtle.forward(size * (1 - reduction_ratio) / 2)
            turtle.left(90)
            turtle.forward(size * (1 - reduction_ratio) / 2)
            turtle.right(90)
            location[0] = turtle.pos()[0]
            location[1] = turtle.pos()[1]
            size2 = size * reduction_ratio
            B = Polygon(num_sides, size2, orientation, location, color, border_size)
            B.draw_polygon()
            for k in range(1):
                turtle.penup()
                turtle.forward(size2 * (1 - reduction_ratio) / 2)
                turtle.left(90)
                turtle.forward(size2 * (1 - reduction_ratio) / 2)
                turtle.right(90)
                location[0] = turtle.pos()[0]
                location[1] = turtle.pos()[1]
                size3 = size2 * reduction_ratio
                C = Polygon(num_sides, size3, orientation, location, color,
                            border_size)
                C.draw_polygon()

elif art == 6:
    for i in range(random.randint(20, 35)):
        num_sides = random.randint(4, 4)  # triangle, square, or pentagon
        size = random.randint(50, 150)
        orientation = random.randint(0, 90)
        location = [random.randint(-300, 300), random.randint(-200, 200)]
        color = [random.randint(0, 255), random.randint(0, 255),
                 random.randint(0, 255)]
        border_size = random.randint(1, 10)
        A = Polygon(num_sides, size, orientation, location, color, border_size)
        reduction_ratio = 0.618
        A.draw_polygon()
        for j in range(1):
            turtle.penup()
            turtle.forward(size * (1 - reduction_ratio) / 2)
            turtle.left(90)
            turtle.forward(size * (1 - reduction_ratio) / 2)
            turtle.right(90)
            location[0] = turtle.pos()[0]
            location[1] = turtle.pos()[1]
            size2 = size * reduction_ratio
            B = Polygon(num_sides, size2, orientation, location, color,
                        border_size)
            B.draw_polygon()
            for k in range(1):
                turtle.penup()
                turtle.forward(size2 * (1 - reduction_ratio) / 2)
                turtle.left(90)
                turtle.forward(size2 * (1 - reduction_ratio) / 2)
                turtle.right(90)
                location[0] = turtle.pos()[0]
                location[1] = turtle.pos()[1]
                size3 = size2 * reduction_ratio
                C = Polygon(num_sides, size3, orientation, location, color,
                            border_size)
                C.draw_polygon()

elif art == 7:
    for i in range(random.randint(20, 35)):
        num_sides = random.randint(5, 5)  # triangle, square, or pentagon
        size = random.randint(50, 150)
        orientation = random.randint(0, 90)
        location = [random.randint(-300, 300), random.randint(-200, 200)]
        color = [random.randint(0, 255), random.randint(0, 255),
                 random.randint(0, 255)]
        border_size = random.randint(1, 10)
        A = Polygon(num_sides, size, orientation, location, color, border_size)
        reduction_ratio = 0.618
        A.draw_polygon()
        for j in range(1):
            turtle.penup()
            turtle.forward(size * (1 - reduction_ratio) / 2)
            turtle.left(90)
            turtle.forward(size * (1 - reduction_ratio) / 2)
            turtle.right(90)
            location[0] = turtle.pos()[0]
            location[1] = turtle.pos()[1]
            size2 = size * reduction_ratio
            B = Polygon(num_sides, size2, orientation, location, color,
                        border_size)
            B.draw_polygon()
            for k in range(1):
                turtle.penup()
                turtle.forward(size2 * (1 - reduction_ratio) / 2)
                turtle.left(90)
                turtle.forward(size2 * (1 - reduction_ratio) / 2)
                turtle.right(90)
                location[0] = turtle.pos()[0]
                location[1] = turtle.pos()[1]
                size3 = size2 * reduction_ratio
                C = Polygon(num_sides, size3, orientation, location, color,
                            border_size)
                C.draw_polygon()

elif art == 8:
    for i in range(random.randint(20, 35)):
        num_sides = random.randint(3, 5)  # triangle, square, or pentagon
        size = random.randint(50, 150)
        orientation = random.randint(0, 90)
        location = [random.randint(-300, 300), random.randint(-200, 200)]
        color = [random.randint(0, 255), random.randint(0, 255),
                 random.randint(0, 255)]
        border_size = random.randint(1, 10)
        A = Polygon(num_sides, size, orientation, location, color, border_size)
        reduction_ratio = 0.618
        A.draw_polygon()
        for j in range(1):
            turtle.penup()
            turtle.forward(size * (1 - reduction_ratio) / 2)
            turtle.left(90)
            turtle.forward(size * (1 - reduction_ratio) / 2)
            turtle.right(90)
            location[0] = turtle.pos()[0]
            location[1] = turtle.pos()[1]
            size2 = size * reduction_ratio
            B = Polygon(num_sides, size2, orientation, location, color,
                        border_size)
            B.draw_polygon()
            for k in range(1):
                turtle.penup()
                turtle.forward(size2 * (1 - reduction_ratio) / 2)
                turtle.left(90)
                turtle.forward(size2 * (1 - reduction_ratio) / 2)
                turtle.right(90)
                location[0] = turtle.pos()[0]
                location[1] = turtle.pos()[1]
                size3 = size2 * reduction_ratio
                C = Polygon(num_sides, size3, orientation, location, color,
                            border_size)
                C.draw_polygon()


# specify a reduction ratio to draw a smaller polygon inside the one above

# reposition the turtle and get a new location

# adjust the size according to the reduction ratio

# draw the second polygon embedded inside the original

# hold the window; close it by clicking the window close 'x' mark
turtle.done()
