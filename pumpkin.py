import turtle

class Pumpkin(turtle.Turtle):
    """
    Draws a pumpkin in a window using the turtle library.
    """

    def __init__(self):
        super().__init__()
        self.ht()

    def set_to_point(self, x, y):
        """Lifts the pen from canvas and moves to the designated coordinate"""
        self.penup()
        self.goto(x, y)
        self.pendown()
        return self

    def set_to_home(self):
        "Lifts the pen and resets the turtle to the home position"
        self.penup()
        self.home()
        self.pendown()
        return self

    def draw_body(self):
        """
        Draws two halve circles and straight segments on top and bottom to
        create the body of the pumpkin
        """
        self.pen(
            pencolor="orange",
            fillcolor="orange",
            pensize=10
        )
        self.set_to_home()
        self.begin_fill()
        # Turns the turtle around - this makes sure the top of the pumpkin
        # is in line with the home position of the turtle
        self.right(180)
        for i in range(2):
            self.circle(120, 180)
            self.forward(50)
        self.end_fill()
        return self

    def draw_stem(self):
        """Draws the stem of the pumpkin off of the top of the body"""
        self.pen(
            pencolor="green",
            fillcolor="green",
            pensize=25
        )
        self.set_to_point(25, 0) # Midpoint of the top segment on body
        # Angles turtle directly up, draws the straight part of the stem,
        # then draws the curved upper part of the stem
        self.right(90)
        self.forward(50)
        self.circle(-25, 90)
        return self

    def draw_eyes(self):
        """
        Draws the eyes of the pumpkin in the correct locations
        The left eye at (-30, -70)
        The right eye at (50, -70)
        """
        for xcoord in (-30, 50):
            self.set_to_point(xcoord, -70)
            self.draw_filled_triangle()
        return self

    def draw_nose(self):
        self.set_to_point(10, -120)
        self.draw_filled_triangle()
        return self

    def draw_filled_triangle(self):
        """Draws a single equilateral triangle, filled with black"""
        self.pen(
            pencolor="black",
            fillcolor="black",
            pensize=10
        )
        def draw_segment():
            """Draws a single segment of the eye and reorients the turtle"""
            self.forward(30)
            self.left(120)
        self.begin_fill()
        for i in range(3):
            draw_segment()
        self.end_fill()
        return self

    def draw_left_curve(self, x_limit, curve="left"):
        while self.xcor() < x_limit:
            self.forward(1)
            self.left(1)
        self.right(1)

    def draw_mouth(self):
        self.pen(
            pencolor='black',
            fillcolor='black',
            pensize=10
        )

        self.set_to_point(-30, -140)
        self.right(45)
        self.draw_left_curve(15)
        self.forward(35)
        self.draw_left_curve(80)
        return self

    def manual_control(self):
        self.st()
        return self

def main():
    s = turtle.getscreen()
    turtle.bgcolor("black")
    pumpkin = Pumpkin()
    (pumpkin
        .draw_body()
        .draw_stem()
        .draw_eyes()
        .draw_nose()
        .draw_mouth()
    )
    t = pumpkin.manual_control()
    input()

if __name__ == "__main__":
    main()
