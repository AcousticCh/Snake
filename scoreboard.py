#!usr/bin/env python3
from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.color("#ffffff")
        self.hideturtle()
        self.penup()
        self.sety(270)
        with open("data.txt") as data:
            self.high_score = data.read()
            self.high_score = int(self.high_score)
        self.clear()
        self.write(arg = f"Score: {self.points} High Score: {self.high_score}", move = False, align = "center", font = ("Arial", 20, "normal"))
		
    def add_point(self):
        self.clear()
        self.points += 1
        self.write(arg = f"Score: {self.points} High Score: {self.high_score}", move = False, align = "center", font = ("Arial", 20, "normal"))

    def reset(self):
        if self.points > int(self.high_score):
            self.high_score = self.points
        self.points = 0
        with open("data.txt", mode="w") as data:
            data.write(str(self.high_score))
        self.clear()
        self.write(arg = f"Score: {self.points} High Score: {self.high_score}", move = False, align = "center", font = ("Arial", 20, "normal"))
        
