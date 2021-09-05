import turtle
NUM_CIRCLES = 80
RADIUS = 150
ANGLE = 5
ANIMATION_SPEED = 0
turtle.speed(ANIMATION_SPEED)
for x in range (NUM_CIRCLES):
    turtle.circle(RADIUS)
    turtle.left(ANGLE)