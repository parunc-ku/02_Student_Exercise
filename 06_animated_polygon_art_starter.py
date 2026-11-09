import math
import random
import time
import turtle
from polygon_shape import Polygon

COLORS = ["cyan", "orange", "magenta", "yellow", "lime", "red",
          "deepskyblue", "violet", "gold", "white", "springgreen", "hotpink"]
NUM_POLYGONS = 12
NUM_FRAMES = 240
DELAY = 0.03


def main():
    random.seed(7)
    screen = turtle.Screen()
    screen.title("Animated Polygon Art")
    screen.bgcolor("black")
    screen.setup(800, 700)
    screen.tracer(0)


    items = []
    for i in range(NUM_POLYGONS):
        bx = random.randint(-220, 120)
        by = random.randint(-180, 120)
        poly = Polygon(bx, by,
                       sides=3 + i % 5,
                       side_length=random.randint(50, 130),
                       color=COLORS[i % len(COLORS)],
                       pen_size=random.randint(1, 7),
                       angle=random.randint(0, 359))
        items.append((poly, bx, by,
                      random.randint(20, 80),
                      random.uniform(0.04, 0.12),
                      random.uniform(0, 2 * math.pi)))

    try:
        for frame in range(NUM_FRAMES):
            for poly, bx, by, radius, speed, phase in items:
                t = frame * speed + phase
                poly.move_to(bx + radius * math.cos(t),
                             by + radius * math.sin(t))
            screen.update()
            time.sleep(DELAY)
    except turtle.Terminator:
        return

    screen.mainloop()


if __name__ == "__main__":
    main()
