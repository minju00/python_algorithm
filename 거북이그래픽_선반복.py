import turtle as t
t.shape("turtle")

angle = 89 # angle이라는 변수를 선언해 몇도 회전시킬지 저장
t.bgcolor("black")
t.color("white")
t.speed(0)
for x in range(200):
    t.fd(x) #x만큼 이동시켜 반복할 수록 이동거리가 늘어나게 설정
    t.lt(angle)
