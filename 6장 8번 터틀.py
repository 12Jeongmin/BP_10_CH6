import turtle
myPen = turtle.Turtle()
myPen.speed(0)
myPen.color("#FF0000")       # 색상을 빨강색으로 지정

for j in range (1,10):
    for i in range (1,6):
        myPen.left(144)
        myPen.forward(200)
        myPen.left(10)
myPen._screen.exitonclick() # 화면을 마우스로 클릭해야 종료되게 하는 부분
