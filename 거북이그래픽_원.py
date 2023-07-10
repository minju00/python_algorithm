import turtle as t
t.shape("turtle")

n=50
t.bgcolor("black")
t.color("green")
t.speed(0) # 거북이의 속도 1~9, 0이 최고 속도

for x in range(n):
    t.circle(80)
    t.left(360/n) # 같은 자리에서 50번 그리는 것이 아니라, 360/50도씩 왼쪽으로 회전하며 그리게 됨 (point)

