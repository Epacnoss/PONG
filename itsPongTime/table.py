from tkinter import *

class table:
    def __init__ (self, window, colour="black", netColour="green", w=600, h=400, horizNet=False):
        self.w = w
        self.h = h
        self.colour = colour

        self.canvas = Canvas(window, bg=self.colour, height=h, width=w)
        self.canvas.pack()
        
        av = (w + h) / 2
        dashWidth = av / 200
        hdw=dashWidth / 2 # hdw=HalfDashWidth
        dashTuple = (15,23)

        if not horizNet:
            self.canvas.create_line(w/2 - hdw, 0, w/2 - hdw, h, width=dashWidth, fill=netColour, dash=dashTuple)
        else:
            self.canvas.create_line(0, h/2 - hdw, w, h/2 - hdw, width=dashWidth, fill=netColour, dash=dashTuple)
    
    def drawRect (self, rect):
        x1 = rect.x
        x2 = x1 + rect.w

        y1 = rect.y
        y2 = y1 + rect.h

        c = rect.c
        
        return self.canvas.create_rectangle(x1, y1, x2, y2, fill=c)

    def drawOval (self, oval):
        x1 = oval.x
        x2 = x1 + oval.w

        y1 = oval.y
        y2 = y1 + oval.h

        c = oval.colour
        
        return self.canvas.create_oval(x1, y1, x2, y2, fill=c)
    
    def moveItem (self, item, x1, y1, x2, y2):
        self.canvas.coords(item, x1, y1, x2, y2)
    
    def removeItem (self, item):
        self.canvas.delete(item)
    
    def changeItemColour (self, item, c):
        self.canvas.itemconfigure(item, fill=c)