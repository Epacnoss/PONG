import table, random

class ball:

    def __init__ (self, table, w=14, h=14, colour="red", xSpd=3, ySpd=2, xStart=0, yStart=0):
        self.w = w
        self.h = h
        self.x = xStart
        self.y = yStart
        self.colour = colour

        self.xStart = xStart
        self.yStart = yStart
        self.xSpd = xSpd
        self.ySpd = ySpd
        self.xStartSpd = xSpd
        self.yStartSpd = ySpd
        self.needsToReverse = False

        self.table = table
        self.circle = self.table.drawOval(self)
        self.noHits = 0

    def startPos (self):
        self.x = self.xStart
        self.y = self.yStart
    
    def startBall (self):
        if not self.needsToReverse:
            self.xSpd = self.xStartSpd
            self.needsToReverse = True
        else:
            self.xSpd = -self.xStartSpd
            self.needsToReverse = False

        self.ySpd = 0
        self.startPos()
    
    def moveNext (self):
        self.x += self.xSpd
        self.y += self.ySpd


        twMinusWMinus3 = (self.table.w - (self.w - 3))
        thMinusHMinus3 = (self.table.h - (self.h - 3))

        prevNoHits = self.noHits
        # hitsToAdd = random.randint(-prevNoHits, prevNoHits)

        if self.x <= 3:
            self.noHits += 1
            # self.xSpd = random.randint(-10 - hitsToAdd, 10 + hitsToAdd)
            self.x = 3
            self.xSpd *= -1

        if self.x >= twMinusWMinus3:
            self.noHits += 1
            # self.xSpd = random.randint(-10 - hitsToAdd, 10 + hitsToAdd)
            self.x = twMinusWMinus3
            self.xSpd *= -1
        
        if self.y <= 3:
            self.noHits += 1
            # self.ySpd = random.randint(-10 - hitsToAdd, 10 + hitsToAdd)
            self.y = 3
            self.ySpd *= -1
        
        if self.y >= thMinusHMinus3:
            self.noHits += 1
            # self.ySpd = random.randint(-10 - hitsToAdd, 10 + hitsToAdd)
            self.y = thMinusHMinus3
            self.ySpd *= -1

        x1 = self.x
        x2 = x1 + self.w

        y1 = self.y
        y2 = y1 + self.h

        self.table.moveItem(self.circle, x1, y1, x2, y2)

    def stop(self):
        self.ySpd = 0
        self.xSpd = 0
        print("Ball Stopped")