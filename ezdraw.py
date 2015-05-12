from Tkinter import *
from math import sin, cos, pi
from time import sleep

class EZDraw(object):
    def __init__(self, w=800, h=600):
        self.root = Tk()
        self.canv = Canvas(self.root, width=w, height=h)
        self.canv.pack()
        self.pos = (w/2, h/2)
        self.angle = -pi/2
        self.w = w
        self.h = h

    def left(self, angle, d=0):
        self.angle -= angle

    def right(self, angle, d=0):
        self.angle += angle

    def pos(self, x, y):
        self.pos = (
            min(self.w, max(0, x)),
            min(self.h, max(0, y))
        )

    def update(self, d):
        self.root.update()
        if d:
            sleep(d)

    def forward(self, px, d=0):
        npos = (self.pos[0] + cos(self.angle) * px, self.pos[1] + sin(self.angle) * px)
        self.canv.create_line(self.pos[0], self.pos[1], npos[0], npos[1])
        self.pos = npos
