from turtle import Screen
from game import Game
game = Game()
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)
screen.tracer(0)
screen.listen()
screen.onkey(game.left_paddle.go_up,"w")
screen.onkey(game.left_paddle.go_down,"s")
screen.onkey(game.right_paddle.go_up, "Up")
screen.onkey(game.right_paddle.go_down,"Down")

game.run_game()

screen.exitonclick()



















