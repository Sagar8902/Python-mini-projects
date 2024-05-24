import turtle
import random
import time

## Creating Screen
screen = turtle.Screen()
screen.title("SNAKE GAME")
screen.setup(width=700, height=700)
screen.tracer(0)
screen.bgcolor("#1d1d1d")

## Creating border
border_pen = turtle.Turtle()
border_pen.speed(5)
border_pen.pensize(4)
border_pen.penup()
border_pen.goto(-310, 250)
border_pen.pendown()
border_pen.color("red")
border_pen.forward(600)
border_pen.right(90)
border_pen.forward(500)
border_pen.right(90)
border_pen.forward(600)
border_pen.right(90)
border_pen.forward(500)
border_pen.penup()
border_pen.hideturtle()

## Score
score = 0
delay = 0.1

## Snake
snake = turtle.Turtle()
snake.speed(0)
snake.shape("circle")
snake.color("green")
snake.penup()
snake.goto(0, 0)
snake.direction = "stop"

## Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("white")
food.penup()
food.goto(30, 30)

segments = []

## Scoring
scoring = turtle.Turtle()
scoring.speed(0)
scoring.color("white")
scoring.penup()
scoring.hideturtle()
scoring.goto(0, 300)
scoring.write("Score: 0", align="center", font=("Courier", 24, "bold"))

## Define how to move
def snake_go_up():
    if snake.direction != "down":
        snake.direction = "up"

def snake_go_down():
    if snake.direction != "up":
        snake.direction = "down"

def snake_go_left():
    if snake.direction != "right":
        snake.direction = "left"

def snake_go_right():
    if snake.direction != "left":
        snake.direction = "right"

def snake_move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)
    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)
    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)
    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)

## Keyboard binding
screen.listen()
screen.onkeypress(snake_go_up, "Up")
screen.onkeypress(snake_go_down, "Down")
screen.onkeypress(snake_go_left, "Left")
screen.onkeypress(snake_go_right, "Right")

## Main loop
while True:
    screen.update()

    # Snake & food collision
    if snake.distance(food) < 20:
        x = random.randint(-290, 270)
        y = random.randint(-240, 240)
        food.goto(x, y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Increase the score
        score += 1
        scoring.clear()
        scoring.write("Score: {}".format(score), align="center", font=("Courier", 24, "bold"))

        # Decrease the delay
        delay -= 0.001

    # Move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = snake.xcor()
        y = snake.ycor()
        segments[0].goto(x, y)

    snake_move()

    # Check for collision with the border
    if snake.xcor() > 290 or snake.xcor() < -310 or snake.ycor() > 250 or snake.ycor() < -250:
        time.sleep(1)
        screen.clear()
        screen.bgcolor("turquoise")
        scoring.goto(0, 0)
        scoring.write(" Game Over \n Your score is {}".format(score), align="center", font=("Courier", 24, "bold"))
        break

    # Check for collision with the body
    for segment in segments:
        if segment.distance(snake) < 20:
            time.sleep(1)
            screen.clear()
            screen.bgcolor("turquoise")
            scoring.goto(0, 0)
            scoring.write(" Game Over \n Your score is {}".format(score), align="center", font=("Courier", 30, "bold"))

    time.sleep(delay)

turtle.Terminator()
