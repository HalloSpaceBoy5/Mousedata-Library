import mouse
from mouse import *


def getMouseX(): #Finds the X coordinate on the screen in pixels output is an integer (0,0 is in the top left)
    moo1 = str(mouse.get_position())
    list1=[]
    list1=moo1.split(",")
    x =list1[0].split("(")
    return int(x[1])

def getMouseY(): #Finds the Y coordinate on the screen in pixels output is an integer (0,0 is in the top left)
    moo2 = str(mouse.get_position())
    list=[]
    list=moo2.split(",")
    y =list[1].split(")")
    return int((y[0]))

def getMouseCoords(): #Finds both the X and Y coordinate on the screen in pixels output is a string (0,0 is in the top left)
    return str(mouse.get_position())

def waitForActivity(): #Will stop the program until mouse ovement is detected
    sMouPos = mouse.get_position()
    while True:
        if sMouPos != mouse.get_position():
            return

def gotoOrigin(): #Will move the mouse to the origin of the screen
    mouse.move(0,0)

def goto(x,y): #Will move the mouse to coordinates specified by the args
    mouse.move(x,y)


