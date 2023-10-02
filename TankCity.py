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


def water():
    '''Returns water drawing'''
    return "🌊"
def bullet():
    '''Returns bullet drawing'''
    return "🪨"
    
def explosion():
    '''Returns explosion drawing'''
    return "💥"

def forest():
    '''Returns forest drawing'''
    return "🌲"
def wall():
    '''Returns wall drawing'''
    return "🗄"

def eagle():
    '''Returns eagle drawing'''
    return "🕊"
    
def goodTank():
    '''Returns goodTank drawing'''
    return "👼"

def badTank():
    '''Returns badTank drawing'''
    return "👿"

def explosionCoord():
    '''Returns explosion coordinates x and y'''
    return {
        "x" : 7,
        "y" : 7
    }

def waterCoord():
    '''Returns water coordinates x and y'''
    return {
        "x" : 9,
        "y" : 9
    }


def forestCoord():
    '''Returns forest coordinates x and y'''
    return {
        "x" : 3,
        "y" : 3
    }
    
def bulletCoord():
    '''Returns bullet coordinates x and y'''
    return {
        "x" : 10,
        "y" : 10
    }
def wallCoord():
    '''Returns wall coordinates x and y'''
    return {
        "x" : 2,
        "y" : 2
    }
def eagleCoord():
    '''Returns eagle coordinates x and y'''
    return {
        "x" : 17,
        "y" : 17
    }

def goodTankCoord():
    '''Returns goodTank coordinates x and y'''
    return {
        "x" : 2,
        "y" : 12
    }

def badTankCoord():
    '''Returns badTank coordinates x and y'''
    return {
        "x" : 12,
        "y" : 2
    }
forest = forest()
wall = wall()
eagle = eagle()
bullet = bullet()
water = water()
waterCoord = waterCoord()
bulletCoord = bulletCoord()
explosion = explosion()
explosionCoord = explosionCoord()
forestCoord = forestCoord()
wallCoord = wallCoord()
eagleCoord = eagleCoord()
goodTank = goodTank()
goodTankCoord = goodTankCoord()
badTank = badTank()
badTankCoord = badTankCoord()


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
            elif x == badTankCoord["x"] and y == badTankCoord["y"]:
                print(badTank)
            elif x == eagleCoord["x"] and y == eagleCoord["y"]:
                print(eagle)  
            elif x == wallCoord["x"] and y == wallCoord["y"]:
                print(wall)
            elif x == forestCoord["x"] and y == forestCoord["y"]:
                print(forest)
            elif x == explosionCoord["x"] and y == explosionCoord["y"]:
                print(explosion)
            elif x == bulletCoord["x"] and y == bulletCoord["y"]:
                print(bullet)
            elif x == waterCoord["x"] and y == waterCoord["y"]:
                print(water)
            # elif x == 0 or x == 36:
            #     print(" ", end="")
            elif y == 0 or y == 18:
                print("-", end="") 
            else:
                print(" ", end="")
        print("")

gameBoard()
            
        