import turtle
t = turtle.Turtle()
t.shape("turtle")
for i in range(5):
    t.forward(200);
    t.right(90)
    t.forward(20);
    t.right(90)
    t.forward(200);
    t.left(90)
    t.forward(20);
    t.left(90)

t._screen.exitonclick() # 화면을 마우스로 클릭해야 종료되게 하는 부분
