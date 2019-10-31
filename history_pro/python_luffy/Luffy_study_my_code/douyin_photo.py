import  turtle as tu
from random import randint as rint
tu.shape("turtle")
tu.pensize(2)
tu.colormode(255)
tu.bgcolor("black")
tu.tracer(False)
# for y in range(100):
#
#     tu.forward(2)
#     tu.color(255, 0, 0)
#     tu.tracer(True)
for x in range(5000):
    # tu.forward(2*x)
    tu.forward(2)
    tu.color(0,255,0)
    # tu.color(rint(0,255),rint(0,255),rint(0,255))

    if x%2 == 0:
        tu.left(x/100)
    # if x%200 == 0:
    #     tu.right(180)
    # tu.speed(10*x)
    tu.tracer(True)


