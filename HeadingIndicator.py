from tkinter import Button,Frame,Tk,Label,PhotoImage, Canvas
from tkinter import *
import numpy as np
import random
from math import sin,cos,pi,ceil

class HeadingIndicator():
    def __init__(self,root):
        self.root=root
        #load image to canvas
        self.gauge=PhotoImage(file="gauge.png")
        self.canvas=Canvas(self.root)
        self.canvas.create_image(200,200,image=self.gauge)
        self.canvas.pack(expand=YES, fill=BOTH)
        self.canvas.config(width=self.gauge.width(), height=self.gauge.height())
        #key bindings
        self.root.bind('<Left>',self.moveLeft)
        self.root.bind('<Right>',self.moveRight)
        #indicator parameters
        self.center=[200,200]
        self.lineLength=180
        self.lineWidth=4
        self.indicator=[]
        self.angle=0
        self.angleReference=[random.randint(0,1) for i in range(100)]
        self.updateIndicator(self.angle)
        self.angleReferenceGenerator()
        self.root.mainloop()

    def updateIndicator(self,angle):
        angle=angle*pi/180
        point1=self.center-np.matrix([self.lineLength*sin(angle),self.lineLength*cos(angle)])
        point2=point1+np.matrix([self.lineWidth*cos(angle),-self.lineWidth*sin(angle)])
        point3=self.center+np.matrix([self.lineWidth*cos(angle),-self.lineWidth*sin(angle)])
        edge1=[ceil(point1[0,0]),ceil(point1[0,1])]
        edge2=[ceil(point2[0,0]),ceil(point2[0,1])]
        edge3=[ceil(point3[0,0]),ceil(point3[0,1])]
        self.indicator=self.canvas.create_polygon(self.center,edge1,edge2,edge3,fill='red')

    def moveLeft(self,event):
        self.angle=self.angle+2
        self.canvas.delete(self.indicator)
        self.updateIndicator(self.angle)

    def moveRight(self,event):
        self.angle=self.angle-2
        self.canvas.delete(self.indicator)
        self.updateIndicator(self.angle)

    def angleReferenceGenerator(self):
        global total_angle_disp
        if self.angleReference:
            popped=self.angleReference.pop()
            if popped==1:
                self.angle=self.angle+2
            else:
                self.angle=self.angle-2
            self.canvas.delete(self.indicator)
            self.updateIndicator(self.angle)
            self.root.after(100,self.angleReferenceGenerator)
            total_angle_disp+=abs(self.angle)
            self.w = Message(text = f"Total angle displacement: {total_angle_disp:.0f}°", bg='white', fg='black', width=75)
            self.w.place(relx=0.095, rely=0.06, anchor=CENTER)

total_angle_disp=0  #total angle displacement
if __name__ == "__main__":
    pass
    root=Tk()
    heading=HeadingIndicator(root)
