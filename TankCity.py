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
from termcolor import colored

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
        "x" : None,
        "y" : None
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
    
# def bulletCoord():
#     '''Returns bullet coordinates x and y'''
#     return {
#         "x" : 10,
#         "y" : 10
#     }
def wallCoordFirstLvl():
    '''Returns 1lvl walls coordinates x and y'''
    return [
        {
        "x" : 2,
        "y" : 2
        },
        {
        "x" : 2,
        "y" : 3
        },
        {
        "x" : 2,
        "y" : 4
        },  
        {
        "x" : 2,
        "y" : 5
        },  
        {
        "x" : 2,
        "y" : 6
        }    
    ]


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
# bullet = bullet()
water = water()
waterCoord = waterCoord()
# bulletCoord = bulletCoord()
explosion = explosion()
explosionCoord = explosionCoord()
forestCoord = forestCoord()
# wallCoord = wallCoord()
eagleCoord = eagleCoord()
goodTank = goodTank()
goodTankCoord = goodTankCoord()
badTank = badTank()
badTankCoord = badTankCoord()
wallCoordFirstLvl = wallCoordFirstLvl()
shoot = False

def greeting():
    '''Prints greeting to the user'''
    print("HelloWorld!")
    time.sleep(1)
    os.system('clear')
    print(colored("What's going on?", "red"))
    time.sleep(1)

# greeting()

def control():
    '''Handles user input (instruction for action)'''
    print("For action, write and instruction here: up, down, right, left, shoot")
    user_action = (input("Action: ")).lower()
    (x, y) = goodTankCoord["x"], goodTankCoord["y"]
    if user_action == "left":
        if x > 0:
            goodTankCoord["x"] = goodTankCoord["x"] - 1
            print(colored("TO THE WEST!", "green"))
            print(goodTankCoord["x"])
    elif user_action == "right":
        if x < 37:
            goodTankCoord["x"] = goodTankCoord["x"] + 1
            print(colored("TO THE EAST!", "green"))
            print(goodTankCoord["x"])
    elif user_action == "up":
        if y > 0:
            goodTankCoord["y"] = goodTankCoord["y"] - 1
            print(colored("TO THE SOUTH!", "green"))
            print(goodTankCoord["y"])
    elif user_action == "up":
        if y < 17:
            goodTankCoord["y"] = goodTankCoord["y"] + 1
            print(colored("TO THE NORTH!", "green"))
            print(goodTankCoord["y"])
    elif user_action == "shoot":
        print(colored("SHOOT!", "red"))
        
    #this loops through bullet y's from goodTank. 
    #!!!! need to incorporate this into general gameloop
        return True
        
    elif user_action == "quit":
        print(colored("SURREND!", "white"))
        return False
        
        
   
control()

def gameBoard():
    '''Draws gameBord'''
    # board = []
    for y in range(0,19):
        for x in range(0,37):
            if x == goodTankCoord["x"] and y == goodTankCoord["y"]:
                print(goodTank, end="")
            elif x == badTankCoord["x"] and y == badTankCoord["y"]:
                print(badTank, end="")
            elif x == eagleCoord["x"] and y == eagleCoord["y"]:
                print(eagle, end="")  
            # elif i = 0:
            #     for i in wallCoordFirstLvl:
            #         if x == wallCoordFirstLvl["x"] and y == wallCoordFirstLvl["y"]:
            #             print(wall, end="")
            #             i+=1
            #--------!!!! fix this part!!!!
            elif x == forestCoord["x"] and y == forestCoord["y"]:
                print(forest, end="")
            elif x == explosionCoord["x"] and y == explosionCoord["y"]:
                print(explosion, end="")
            # elif x == bulletCoord["x"] and y == bulletCoord["y"]:
            #     print(bullet, end="")
            elif x == waterCoord["x"] and y == waterCoord["y"]:
                print(water, end="")
            # elif x == 0 or x == 36:
            #     print(" ", end="")
            elif y == 0 or y == 18:
                print("-", end="") 
            else:
                print(" ", end="")
        print("")

# gameBoard()
def bullet_true(shoot):
    if shoot == True:
        column = goodTankCoord["y"]
        while column > 1:
            explosionCoord["y"] = goodTankCoord["y"] - 1
            explosionCoord["x"] = goodTankCoord["x"]
            column -= 1
            if column == 1:
                return False
        return explosionCoord["y"], explosionCoord["x"]

# shoot = 

def game():
    # greeting()
    while True:
        gameBoard()
        control()
        # if bullet_true() is not False:
        #     return bullet_true()
        # else: 
        #     shoot = False
            #----------------incorporate bullet movement if bullet IS
        
            
                
            
        #somewhere here should be asked if the bullet was shot, if yes - then bullet continues to move up, if not - breaks the loop
        os.system('clear')
        




game()