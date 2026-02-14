import random

#function to take user input
def userplay():

    #Take user input and return
    print( "Enter your selection (Rock, Paper, or Scissors):")
    selection = input()

    return selection

#function to generate the computer's choice
def computerplay():

    #generate a number between 1 and three to make a choice
    randomnum = random.randrange(1,3,1)

    #map that random number to a game relevant choice
    if randomnum == 1:
        computerchoice = "Rock"
    elif randomnum == 2:
        computerchoice = "Paper"
    else:
        computerchoice = "Scissors"
    return computerchoice

def wincheck(computer, player):
    #set variable to change on a win condition
    playerwon = 0

    #enumerate win conditions for player
    if computer == "Rock" and player == "Paper":
        playerwon = 1
    elif computer == "Scissors" and player == "Rock":
        playerwon = 1
    elif computer == "Paper" and player == "Scissors":
        playerwon = 1

    return playerwon


#Start game
print("Welcome to Rock, Paper, Scissors!\n")
print("Rock, Paper Scissors... ")

#Get moves
playermove = userplay()
computermove = computerplay()
print("computer throws down: " + computermove)

#Show results
playerwon = wincheck(computermove, playermove)
if playerwon == 1:
    print("You win!")
elif playerwon == 2:
    print("It's a draw!")
else:
    print("You lose!")



