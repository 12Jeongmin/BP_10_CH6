import turtle
import math
t= turtle.Turtle()
t.shape("turtle")
t.color('red', 'yellow')
for x in range(0, 360):
    t.goto(x,200*math.sin(x*3.14/180))
t._screen.exitonclick() # 화면을 마우스로 클릭해야 종료되게 하는 부분
