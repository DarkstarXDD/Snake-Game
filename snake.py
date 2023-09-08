import turtle
from turtle import *
import random


MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

turtle.colormode(255)


class Snake:

    def __init__(self):
        self.pos_x = 0
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def rand_color(self):
        x = random.randint(0, 255)
        y = random.randint(0, 255)
        z = random.randint(0, 255)
        rand_color = (x, y, z)
        return rand_color

    def create_snake(self):
        for _ in range(3):
            # pos = (-self.pos_x, 0)
            self.pos_x += 20
            self.add_segment()

    def add_segment(self):
        new_segment = Turtle()
        new_segment.shape("square")
        new_segment.color(self.rand_color())
        new_segment.penup()
        self.segments.append(new_segment)

    def snake_extend(self):
        self.add_segment()

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DIST)

    # If the heading is towards up, you can't go down. Same with left & right.
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
