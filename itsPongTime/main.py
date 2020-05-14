from tkinter import *

import ball
import bat
import random
import table

def runGame(scoreLeft_, scoreRight_):

    xVel = random.randint(7, 10)
    yVel = random.randint(7, 10)

    xPos = 300
    yPos = 200

    window = Tk()
    window.title("Ping Pong")

    tableActual = table.table(window, horizNet=False)
    ballActual = ball.ball(table=tableActual, xSpd=xVel, ySpd=yVel, w=24, h=24, colour="red", xStart=xPos, yStart=yPos)

    lBat = bat.bat(table=tableActual, w=15, h=100, xPos=20, yPos=150, colour="blue")
    # rBat = bat.bat(table=tableActual, w=15, h=100, xPos=575, yPos=150, colour="yellow")

    def gameFlow(scoreLeft, scoreRight):
        leftColl = lBat.detectCollision(ballActual)
        # righColl = rBat.detectCollision(ballActual)

        ballActual.moveNext()

        if ballActual.x <= 3:
            restart(False)
            scoreRight += 1
        elif ballActual.x + ballActual.w >= tableActual.w - 3:
            restart(False)
            scoreLeft += 1

        def gf ():
            gameFlow(scoreLeft, scoreRight)
            # print(scoreLeft)
            # print(scoreRight)

        window.after(50, gf)


    def restart (space):

        if(space):
            scoreLeft_ = 0
            scoreRight_ = 0

        ballActual.stop()
        ballActual.startPos()
        lBat.startPos()
        # rBat.startPos()

        tableActual.moveItem(lBat.rect, 20, 150, 35, 250)
        # tableActual.moveItem(rBat.rect, 575, 150, 590, 250)

        ballActual.startBall()

    def spaceRestart (master):
        restart(True)

    window.bind("w", lBat.moveUp)
    window.bind("s", lBat.moveDown)
    # window.bind("<Up>", rBat.moveUp)
    # window.bind("<Down>", rBat.moveDown)
    window.bind("<space>", spaceRestart)

    gameFlow(scoreLeft_, scoreRight_)

    window.mainloop()


if __name__ == "__main__":
    runGame(0, 0)
