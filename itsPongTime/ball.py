import table, random

class ball:

    def __init__ (self, table, w=14, h=14, colour="red", xSpd=6, ySpd=4, xStart=0, yStart=0):
        self.w = w
        self.h = h
        self.x = xStart
        self.y = yStart
        self.colour = colour

        self.xStart = xStart
        self.yStart = yStart
        self.xSpd = xSpd
        self.ySpd = ySpd

        self.table = table
        self.circle = self.table.drawOval(self)
        self.noHits = 0

    def startPos (self):
        self.x = self.xStart
        self.y = self.yStart
    
    def startBall (self, xSpd, ySpd):
        self.xSpd = -xSpd if random.randint(0, 1) else xSpd
        self.ySpd = -ySpd if random.randint(0, 1) else ySpd
        self.startPos()
    
    def moveNext (self):
        self.x += self.xSpd
        self.y += self.ySpd


        twMinusWMinus3 = (self.table.w - (self.w - 3))
        thMinusHMinus3 = (self.table.h - (self.h - 3))

        prevNoHits = self.noHits
        # hitsToAdd = random.randint(-prevNoHits, prevNoHits)

        if(self.x <= 3):
            self.noHits += 1
            # self.xSpd = random.randint(-10 - hitsToAdd, 10 + hitsToAdd)
            self.x = 3
            self.xSpd *= -1

        if(self.x >= twMinusWMinus3):
            self.noHits += 1
            # self.xSpd = random.randint(-10 - hitsToAdd, 10 + hitsToAdd)
            self.x = twMinusWMinus3
            self.xSpd *= -1
        
        if(self.y <= 3):
            self.noHits += 1
            # self.ySpd = random.randint(-10 - hitsToAdd, 10 + hitsToAdd)
            self.y = 3
            self.ySpd *= -1
        
        if(self.y >= thMinusHMinus3):
            self.noHits += 1
            # self.ySpd = random.randint(-10 - hitsToAdd, 10 + hitsToAdd)
            self.y = thMinusHMinus3
            self.ySpd *= -1


        if(prevNoHits != self.noHits):
            print("I hit something......", self.noHits)

        x1 = self.x
        x2 = x1 + self.w

        y1 = self.y
        y2 = y1 + self.h

        self.table.moveItem(self.circle, x1, y1, x2, y2)