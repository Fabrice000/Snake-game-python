import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard



screen = Screen()

screen.setup(width=600, height=600)

screen.bgcolor("black")

screen.title('My Snake game')
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


is_running = True
while is_running:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    # collision food
    
    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh()
        score.increase_score()
    # collision wall
    
    if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        score.reset()
        snake.reset()
    
    # collision tail
    
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()
    
        
        
    
screen.exitonclick() 
