# Create Rock Paper Scissors Game

from random import randint

# create a list of play options
t = ['Rock', 'Paper', 'Scissors']

# Assign a random play to the computer using the random package
# randint(a, b) creats a random number between a and b
computer = t[randint(0, 2)]

# set player to False
player = False

while player == False:
    # win by setting player to True
    player = input("Rock, Paper, Scissors? Or Type Exit the end application.Ro ")

    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cuts", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Paper":
            print("You win!", player, "cuts", computer)
        else:
            print("You lose!", computer, "smashes", player)
    elif player == "Exit":
        print("Goodbye!!")
        break
    else:
        print("That is not a valid play. Check your spelling!!")


    # player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0, 2)]


