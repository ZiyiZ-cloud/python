# import turtle
# colors=['red','purple','blue','green','orange','yellow']
# t=turtle.Pen()
# turtle.bgcolor('black')
# for x in range(360):
#     t.pencolor(color[x%6])
#     t.width(x/100+1)
#     t.forward(x)
#     t.left(59)
    
    
from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()