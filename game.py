from turtle import Turtle
import time
from ball import Ball
from paddle import Paddle
class Game(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.score_display = self.update_scoreboard()
        self.ball = Ball()
        self.left_paddle = Paddle((-350,0))
        self.right_paddle = Paddle((350,0))


    def run_game(self):
        while True:
            time.sleep(0.1)
            self.screen.update()
            self.ball.move()
            # Detect collision with the upper and lower wall
            if self.ball.ycor() > 280 or self.ball.ycor() < -280:
                self.ball.bounce_y()
            if (self.ball.distance(self.right_paddle) < 50 and self.ball.xcor() > 310) or (self.ball.distance(self.left_paddle) < 50 and self.ball.xcor() < -310) :
                self.ball.bounce_x()
            if self.ball.xcor() > 380:
                self.ball.reset_position()
                self.l_score += 1
                self.update_scoreboard() 
            elif self.ball.xcor() <- 380:
                self.ball.reset_position()
                self.r_score += 1
                self.update_scoreboard()




    def update_scoreboard(self):
        self.clear()
        self.goto(-180,200)
        self.write(self.l_score, align = 'center', font=('Arial', 60, 'normal'))
        self.goto(180,200)
        self.write(self.r_score, align = 'center', font=('Arial', 60, 'normal'))
    
 

    def left_paddle_score(self):
        self.l_score += 1 
        self.update_scoreboard()

    def right_paddle_score(self):
        self.r_score += 1
        self.update_scoreboard()