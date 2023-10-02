#TankCity

#Create a board/draw a game board
#Create main Tank
#Create enemy Tank
#Create Main object that must be secured
#Draw all objects on game board
#Randomize enemy Tank movements and apearance
#Let user to control main Tank
#Create main Tanks bullets
#Create enemy tank bullets
#Game win / lose
#Main menu
#Greeting
#Score Colletion


import random
import time
import os



def goodTank():
    '''Returns goodTank drawing'''
    return "🥙"

def goodTankCoord():
    '''Returns goodTank coordinates x and y'''
    return {
        "x" : 17,
        "y" : 17
    }
goodTank = goodTank()
goodTankCoord = goodTankCoord()


def greeting():
    '''Prints greeting to the user'''
    print("HelloWorld!")
    time.sleep(1)
    os.system('clear')
    print("What's going on?")
    time.sleep(1)

# greeting()



    
def gameBoard():
    '''Draws gameBord'''
    # board = []
    for y in range(0,19):
        for x in range(0,37):
            if x == goodTankCoord["x"] and y == goodTankCoord["y"]:
                print(goodTank)
            elif x == 0 or x == 36:
                print("|", end="")
            elif y == 0 or y == 18:
                print("-", end="") 
            else:
                print(" ", end="")
        print("")

gameBoard()
            
        