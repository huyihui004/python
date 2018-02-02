#!/usr/bin/python
#coding:utf-8

#题目：画图，学用circle画圆形。
'''
if __name__ == '__main__':
    from Tkinter import *

    canvas = Canvas(width=600, height=400, bg='yellow')
    canvas.pack(expand=YES, fill=BOTH)
    k = 1
    j = 1
    for i in range(0,26):
        canvas.create_oval(310 - k,250 - k,310 + k,250 + k, width=1)
        k += j
        j += 0.3

    mainloop()
'''
'''
if __name__ == '__main__':
    import turtle
    turtle.title("画圆")
    turtle.setup(800,600,0,0)
    pen=turtle.Turtle()
    pen.color("yellow")
    pen.width(5)
    pen.shape("turtle")
    pen.speed(1)
    pen.circle(100)
'''

#题目：画图，学用line画直线。

if __name__ == '__main__':
    from Tkinter import *

    canvas = Canvas(width=600, height=600, bg='green')
    canvas.pack(expand=YES, fill=BOTH)
    x0 = 263
    y0 = 263
    y1 = 275
    x1 = 275
    for i in range(19):
        canvas.create_line(x0,y0,x0,y1, width=1, fill='red')
        x0 = x0 - 5
        y0 = y0 - 5
        x1 = x1 + 5
        y1 = y1 + 5

    x0 = 263
    y1 = 275
    y0 = 263
    for i in range(21):
        canvas.create_line(x0,y0,x0,y1,fill = 'red')
        x0 += 5
        y0 += 5
        y1 += 5

    mainloop()