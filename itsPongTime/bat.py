import tableclass bat:    def __init__(self, table, w=15, h=15, xPos=50, yPos=50, colour="green", xSpd=23, ySpd=23):        self.w = w        self.h = h        self.x = xPos        self.y = yPos        self.c = colour        self.xStart = xPos        self.yStart = yPos        self.xSpd = xSpd        self.ySpd = ySpd        self.table = table        self.rect = self.table.drawRect(self)    def moveUp(self, master):        self.y -= self.ySpd        if self.y <= 0:            self.y = 0        x1 = self.x        x2 = x1 + self.w        y1 = self.y        y2 = y1 + self.h        self.table.moveItem(self.rect, x1, y1, x2, y2)    def moveDown(self, master):        self.y += self.ySpd        if self.y >= self.table.h - self.h:            self.y = self.table.h - self.h        x1 = self.x        x2 = x1 + self.w        y1 = self.y        y2 = y1 + self.h        self.table.moveItem(self.rect, x1, y1, x2, y2)    def moveLeft(self, master):        self.x -= self.xSpd        farRight = self.table.w - self.w        if self.x <= 0:            self.x = 0        x1 = self.x        x2 = x1 + self.w        y1 = self.y        y2 = y1 + self.h        self.table.moveItem(self.rect, x1, y1, x2, y2)    def moveRight(self, master):        self.x += self.xSpd        farRight = self.table.w - self.w        if self.x >= farRight:            self.x = farRight        x1 = self.x        x2 = x1 + self.w        y1 = self.y        y2 = y1 + self.h        self.table.moveItem(self.rect, x1, y1, x2, y2)    def startPos(self):        self.x = self.xStart        self.y = self.yStart    def detectCollision(self, ball):        collisionDir = "miss"        collision = False        #Bat Vars        bottom = self.y        top = bottom + self.h        left = self.x        right = left + self.w        # vCentre = top + (self.h / 2)        # hCentre = top + (self.w / 2)        #Ball Vars        bottomB = ball.y        topB = bottomB + ball.h        leftB = ball.x        rightB = leftB + ball.w        r = (rightB - leftB) / 2  # radius        # vCentreB = topB + r        # hCentreB = leftB + r        if bottomB > top:            print("bb > top")            if topB < bottom:                print("tb < bot")                if rightB > left:                    print("rb > left")                    if leftB < right:                        collision = True # we get lots of collision data, then we lose, then we get no more data.....                        print("COLLISION")        if collision:            if (topB > top - r) and (bottomB < bottom + r) and (rightB > right) and (leftB <= right):                collisionDir = "E"                ball.x_speed = abs(ball.x_speed)            elif (leftB > left - r) and (rightB < right + r) and (bottomB > bottom) and (topB <= bottom):                collisionDir = "S"                ball.y_speed = abs(ball.y_speed)            elif (leftB > left - r) and (rightB < right + r) and (topB < top) and (bottomB >= top):                collisionDir = "N"                ball.y_speed = -abs(ball.y_speed)            elif (topB > top - r) and (bottomB < bottom + r) and (leftB < left) and (rightB >= left):                collisionDir = "W"                ball.x_speed = -abs(ball.x_speed)            else:                collisionDir = "miss"            # if sideSweetSpot and (collisionDir == "W" or collisionDir == "E"):            #     adj = (-(vCentre - vCentreB)) / (self.h / 2)            #     ball.ySpd = feel * adj            # if topSweetSpot and (collisionDir == "N" or collisionDir == "S"):            #     adj = (-(hCentre - hCentreB)) / (self.w / 2)            #     ball.xSpd = feel * adj        # if(collision):        #     print(collisionDir)        return collision, collisionDir