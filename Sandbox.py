''' 
    Name: Snowball-Mania
    Author: Kyle Yeh
    Date: December 5, 2025
    Class: AP Computer Science Principles
    Python: 3.13
'''

import random
import time

from colorama import Fore, Back, init, Style

init()

def printIntro():
    '''
    ' Param: none
    ' 
    ' Print a welcome message to the user
    ' 
    ' Return: none
    '''
    print("❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️")
    print("❄️  Welcome to Snowball Mania!❄️")
    print("❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️")


def getNamesFromUser():
    '''
    ' Param: none
    ' 
    ' Create a list to hold player names.
    ' Ask the user for their name.  Store it in a variable and add it to the player list.
    ' Print instructions for the user to add more players and to type "DONE" when finished.
    ' Read in the first additional player name.
    ' While the user hasn't typed "DONE", add the new name to the player list and prompt for the next name
    ' After the user is finished entering names, print a "Time to play!" message
    '
    ' Return: the list of player names
    ' 
    '''
    players = []
    myName = input("What is your name? ")
    players.append([myName, 3])
    print("Type the name of the next player you want in the snow battle (or DONE when finished):  ")
    name = input()
    while (name != "DONE"):
        players.append([name, 3])
        name = input()
    print("Great - time to play!")
    return players, myName

def getNamesFromFile():
    filename = input("What is the name of the file you want to read from?  ")
    lines = []
    with open(filename, 'r') as file:
        for line in file:
            lines.append(line.strip())
    players = []
    for name in lines:
        players.append([name, 3])
    return players

def getThrower(players):
    '''
    ' Param: players (list of player names)
    '
    ' Return a randomly chosen player name to be the next thrower.
    '
    ' Return: player name
    '''
    thrower = random.choice(players)
    return thrower

    
def getVictim(players, t):
    '''
    ' Param: players (list of player names), t (the thrower for this round)
    ' 
    ' Select a random player to be the next victim.  
    ' While the victim is the same player as the thrower, randomly select a new victim from the list.
    ' Return the victim's name.
    '
    ' Return: victim's name
    '''
    victim = random.choice(players)
    while (t == victim):
        victim = random.choice(players)
    return victim


def getHitResult():
    '''
    ' Param: none
    ' 
    ' Generate a random number between 1 and 10
    ' If the number is greater than 4 (60% chance), return True
    ' Else, return False
    '
    ' Return: Boolean representing whether or not the snowball hit
    '''
    hitNum = random.randint(1, 10)
    if (hitNum > 4):
        return True
    else:
        return False
    
def playSnowballFightWithHealth(players, userName = ""):
    '''
    ' Param: players (a list of players still in the game)
    '
    ' While there are still multiple players in the game...
    '   - Get the next thrower
    '   - Get the next victim
    '   - Get the next hit result
    '   - If a hit occurred, flip a coin to see if it is a knockout or not.
    '     - If knockout, print a knockout message and remove the victim from the list
    '     - Else, print a hit message but do not remove victim
    '   - Else, print a miss message
    '   - time.sleep(3) - delay execution for three seconds
    ' 
    ' Return: none
    '''
    while (len(players) > 1):
        thrower = getThrower(players)
        print(thrower)

        if (thrower == userName):
            victim = input("You pick up a snowball...who do you want to throw at?  ")
        else:
            victim = getVictim(players, thrower)
        
        hitResult = getHitResult()

        missList = []
        hitSurviveList = []
        koList = []

        missList.append(thrower[0] + " throws at " + victim[0] + " but has really bad aim and misses.")
        missList.append(thrower[0] + " throws at " + victim[0] + " but " + victim[0] + " dodges like a champ!")

        hitSurviveList.append(thrower[0] + " throws at " + victim[0] + " and " + Fore.GREEN + "hits" + Style.RESET_ALL + ", but " + Fore.YELLOW + victim[0] + " survives!" + Style.RESET_ALL)
        hitSurviveList.append(thrower[0] + " throws at " + victim[0] + " and " + Fore.GREEN + "hits" + Style.RESET_ALL + "..." + Fore.YELLOW + victim[0] + " shakes it off and gets back to their feet!" + Style.RESET_ALL)

        koList.append(thrower[0] + " throws and absolutely destroys " + victim[0] + " - " + Fore.RED + victim[0] + " is out of the game!!!" + Style.RESET_ALL)
        koList.append(thrower[0] + " sneakily lobs one at " + victim[0] + " - " + victim[0] + " looks straight up when it comes down and " + Fore.RED + victim[0] + " is out of the game!!!" + Style.RESET_ALL)
        
        if (hitResult == True):
            victim[1] -= 1
            if (victim[1] == 0):
                print(random.choice(koList))
                players.remove(victim)
            else:
                print(random.choice(hitSurviveList))
        else:
            print(random.choice(missList))
        # time.sleep(3)

def playSnowballFightRandom(players, userName = ""):
    '''
    ' Param: players (a list of players still in the game)
    '
    ' While there are still multiple players in the game...
    '   - Get the next thrower
    '   - Get the next victim
    '   - Get the next hit result
    '   - If a hit occurred, flip a coin to see if it is a knockout or not.
    '     - If knockout, print a knockout message and remove the victim from the list
    '     - Else, print a hit message but do not remove victim
    '   - Else, print a miss message
    '   - time.sleep(3) - delay execution for three seconds
    ' 
    ' Return: none
    '''
    while (len(players) > 1):
        thrower = getThrower(players)

        if (thrower == userName):
            victim = input("You pick up a snowball...who do you want to throw at?  ")
        else:
            victim = getVictim(players, thrower)
        
        hitResult = getHitResult()

        missList = []
        hitSurviveList = []
        koList = []

        missList.append(thrower[0] + " throws at " + victim[0] + " but has really bad aim and misses.")
        missList.append(thrower[0] + " throws at " + victim[0] + " but " + victim[0] + " dodges like a champ!")

        hitSurviveList.append(thrower[0] + " throws at " + victim[0] + " and " + Fore.GREEN + "hits" + Style.RESET_ALL + ", but " + Fore.YELLOW + victim[0] + " survives!" + Style.RESET_ALL)
        hitSurviveList.append(thrower[0] + " throws at " + victim[0] + " and " + Fore.GREEN + "hits" + Style.RESET_ALL + "..." + Fore.YELLOW + victim[0] + " shakes it off and gets back to their feet!" + Style.RESET_ALL)

        koList.append(thrower[0] + " throws and absolutely destroys " + victim[0] + " - " + Fore.RED + victim[0] + " is out of the game!!!" + Style.RESET_ALL)
        koList.append(thrower[0] + " sneakily lobs one at " + victim[0] + " - " + victim[0] + " looks straight up when it comes down and " + Fore.RED + victim[0] + " is out of the game!!!" + Style.RESET_ALL)
        
        if (hitResult == True):
            koResult = random.randint(1, 2)     # 1 = not KO, 2 = KO
            if (koResult == 1):
                print(random.choice(hitSurviveList))
            else:
                print(random.choice(koList))
                players.remove(victim)
        else:
            print(random.choice(missList))
        # time.sleep(3)
    
def printOutro(winner):
    '''
    ' Param: name of the winner
    ' 
    ' Print a congratulatory message naming the winner
    '
    ' Return: none
    '''
    print("❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️")
    print("All hail " + winner[0] + ", the Ultimate Student/Snowball Wizard!")
    print("❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️")


def runProgram():
    '''
    ' Param: none
    ' 
    ' Call the method that will print the intro messages
    ' Call the method that will return a list of player names.  Save the list in a variable.
    ' Call the method that will simulate the snowball fight
    ' Call the method that will print the outro messagees
    '
    ' Return: none
    '''
    printIntro()
    # testPlayers = ["Jack", "Sam", "Eliana", "Aanya", "Izaiah", "Audrey", "Elam", "John", "Jared", "Aron", "Sebastien", "Tyler", "Collin", "Taylor", "Will", "Nolan", "Llyden", "Xavier", "Landon", "Mr. Holthouse", "Mr. Yeh"]
    # testPlayers = ["Jack", "Sam", "Eliana", "Aanya", "Izaiah"]
    nameChoice = input("Do you want to (1) input names manually or (2) read from a file?  ")
    if (nameChoice == "1"):
        testPlayers, userName = getNamesFromUser()
    else:
        testPlayers = getNamesFromFile()
        userName = ""
    fightChoice = input("Do you want to (1) play with random knockouts or (2) play with health-based knockouts?  ")
    if (fightChoice == "1"):
        playSnowballFightRandom(testPlayers, userName)
    else:
        playSnowballFightWithHealth(testPlayers, userName)
    printOutro(testPlayers[0])


runProgram()
