import turtle
import random
t = turtle.Turtle()
t.shape("turtle")
for j in range (1,10):
    t.up()
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    r = random.randint(10, 200)
    t.goto(x, y)
    t.down()
    t.circle(r)

t._screen.exitonclick() # 화면을 마우스로 클릭해야 종료되게 하는 부분
