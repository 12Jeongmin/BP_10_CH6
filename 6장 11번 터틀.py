import turtle                 # turtle 함수 불러오기
t = turtle.Turtle()            # t에 turtle.Turtle()함수 정의
t.shape("turtle")              # 거북이 소환
t.color('red', 'yellow')       # (선, 내부)색상 지정	
t.begin_fill()	         # 색을 칠하는 메소드	
while True:                   # 무한 반복
    t.forward(200)              # 앞으로 200전진
    t.left(170)	        # 왼쪽으로 170도 방향 전환
    if abs(t.pos()) < 1:         # 거북이의 절대 위치 좌표를 구하는데1보다 작으면 즉, 0이 되면 break문을 활용하여 종료한다.
        break											
t.end_fill()                    # end_fill은 칠 해준다.
t._screen.exitonclick() # 화면을 마우스로 클릭해야 종료되게 하는 부분
