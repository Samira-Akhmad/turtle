# import turtle as t


# t.speed(0)
# t.bgcolor("black")
# t.color("aqua")
# t.hideturtle()

# for i in range(170):
#     t.circle(i-5)
#     t.left(5)

# t.done()


from turtle import *
import colorsys

speed(0)
bgcolor("black")

h=0
for i in range(360):
    for j in range(2):
        c=colorsys.hsv_to_rgb(h,1,1)
        color(c)
        h+=0.005
        rt(90)
        circle(150 - j * 6, 90)
        lt(90)
        circle(150 - j * 6, 90)
        rt(180)
    circle(40, 24)

done()