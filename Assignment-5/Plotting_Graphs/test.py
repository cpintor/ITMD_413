from turtle import *
color('black', 'blue')
begin_fill()
while True:
    forward(90)
    left(150)
    if abs(pos()) < 1:
        break
end_fill()
done()