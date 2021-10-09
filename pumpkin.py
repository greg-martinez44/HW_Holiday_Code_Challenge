import turtle

class Pumpkin(turtle.Turtle):

    def set_to_point(self, x, y):
        self.penup()
        self.goto(x, y)
        self.pendown()
        return self

    def set_to_home(self):
        self.penup()
        self.home()
        self.pendown()
        return self

    def draw_body(self):
        self.pen(
            pencolor="orange",
            fillcolor="orange",
            pensize=10
        )
        self.set_to_home()
        self.begin_fill()
        self.right(180)
        for i in range(2):
            self.circle(120, 180)
            self.forward(50)
        self.end_fill()
        return self

    def draw_stem(self):
        self.pen(
            pencolor="green",
            fillcolor="green",
            pensize=25
        )
        self.set_to_point(25, 0)
        self.right(90)
        self.forward(50)
        self.circle(-25, 90)
        return self

    def draw_eyes(self):
        for xcoord in (-30, 50):
            self.set_to_point(xcoord, -70)
            self.draw_eye()
        return self

    def draw_eye(self):
        self.pen(
            pencolor="black",
            fillcolor="black",
            pensize=10
        )
        def draw_eye_segment():
            self.forward(30)
            self.left(120)
        self.begin_fill()
        for i in range(3):
            draw_eye_segment()
        self.end_fill()
        return self

def main():
    s = turtle.getscreen()
    turtle.bgcolor("black")
    pumpkin1 = Pumpkin()
    (pumpkin1
        .draw_body()
        .draw_stem()
        .draw_eyes()
    )
    input()

if __name__ == "__main__":
    main()
