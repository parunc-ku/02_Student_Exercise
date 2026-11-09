import random
import turtle
from polygon_shape import Polygon

COLORS = ["cyan", "orange", "magenta", "yellow", "lime", "red",
          "deepskyblue", "violet", "gold", "white", "springgreen", "hotpink"]


def make_polygons(count=20):
    polygons = []
    for _ in range(count):
        polygons.append(Polygon(
            x=random.randint(-250, 150),
            y=random.randint(-200, 150),
            sides=random.randint(3, 7),
            side_length=random.randint(40, 150),
            color=random.choice(COLORS),
            pen_size=random.randint(1, 8),
            angle=random.randint(0, 359),
        ))
    return polygons


def main():
    random.seed(7)  
    screen = turtle.Screen()
    screen.title("Static Polygon Art")
    screen.bgcolor("black")
    screen.setup(800, 700)
    screen.tracer(0)

    polygons = make_polygons(20)
    for poly in polygons:
        poly.draw()
    screen.update()
    screen.mainloop()


if __name__ == "__main__":
    main()
