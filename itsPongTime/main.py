from tkinter import *
import table, ball, bat, random


def runGame():
    xVel = random.randint(7, 10)
    yVel = random.randint(7, 10)

    xPos = random.randint(24, 500 - 24)
    yPos = random.randint(24, 500 - 24)

    window = Tk()
    window.title("Ping Pong")

    tableActual = table.table(window, horizNet=False)
    ballActual = ball.ball(table=tableActual, xSpd=xVel, ySpd=yVel, w=24, h=24, colour="red", xStart=xPos, yStart=yPos)

    lBat = bat.bat(table=tableActual, w=15, h=100, xPos=20, yPos=150, colour="blue")
    rBat = bat.bat(table=tableActual, w=15, h=100, xPos=575, yPos=150, colour="yellow")

    def gameFlow():
        leftColl = lBat.detectCollision(ballActual)
        righColl = rBat.detectCollision(ballActual)

        # if leftColl[0]:
        #     print("LCOL: ", leftColl[1])
        # elif righColl[0]:
        #     print("RCOL: " + righColl[1])

        ballActual.moveNext()
        window.after(50, gameFlow)

    window.bind("w", lBat.moveUp)
    window.bind("s", lBat.moveDown)
    window.bind("<Up>", rBat.moveUp)
    window.bind("<Down>", rBat.moveDown)

    gameFlow()

    window.mainloop()


if __name__ == "__main__":
    runGame()
