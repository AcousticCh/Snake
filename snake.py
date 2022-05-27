#!usr/bin/env python3
from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_seg(position)
    def move(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg_num -1].xcor()
            new_y = self.segment[seg_num -1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.segment[0].forward(DISTANCE)
		
    def move_left(self):
        if self.segment[0].heading() == 0:
            pass
        else:
            self.segment[0].seth(180)
		
    def move_right(self):
        if self.segment[0].heading() == 180:
            pass
        else:
            self.segment[0].seth(0)
	
    def move_up(self):
        if self.segment[0].heading() == 270:
            pass
        else:
            self.segment[0].seth(90)
		
    def move_down(self):
        if self.segment[0].heading() == 90:
            pass
        else:
            self.segment[0].seth(270)
	
    def add_seg(self, position):
        """create segment to add"""
        pen = Turtle()
        pen.shape("square")
        pen.color("white")
        pen.penup()
        pen.goto(position)
        self.segment.append(pen)
			
    def extend(self):
        """add segment to snake"""
        self.add_seg(self.segment[-1].position())
        
    def reset(self):
        for seg in self.segment:
            seg.goto(1000, 1000)
        self.segment.clear()
        self.create_snake()

