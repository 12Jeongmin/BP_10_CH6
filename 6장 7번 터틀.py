import turtle
t = turtle.Turtle()
t.shape("turtle")
t.color("#0000ff")
t.left(90)
for i in range (1,7):
 t.forward(100)
 t.forward(-30)
 t.left(60)
 t.forward(30)
 t.forward(-30)
 t.right(120)
 t.forward(30)
 t.forward(-30)
 t.left(60)
 t.forward(-70)
 t.left(60)
t._screen.exitonclick() # 화면을 마우스로 클릭해야 종료되게 하는 부분