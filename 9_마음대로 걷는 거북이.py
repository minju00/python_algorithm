# unit 09
# 마음대로 걷는 거북이 1

import turtle as t
import random

t.shape("turtle")
t.speed(0)

for x in range(500):
  a = random.randint(1,360)
  t.setheading(a)
  t.forward(10)
