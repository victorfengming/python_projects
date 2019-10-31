import  turtle as tu
from random import randint as rint
tu.shape("turtle")
tu.pensize(2)
tu.colormode(255)
tu.bgcolor("black")
tu.tracer(False)
for x in range(500):
    tu.forward(2*x)
    tu.color(rint(0,255),rint(0,255),rint(0,255))
    tu.left(90.5)
    tu.speed(10)
    tu.tracer(True)


