from turtle import Turtle

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.score = 0
    self.color("white")
    self.penup()
    self.goto(0,150)
    self.hideturtle()
    self.update()
    
  def update(self):
    self.write(f"SCORE: {self.score}", align="center")

  def increase(self):
    self.score += 1
    self.clear()
    self.update()
  