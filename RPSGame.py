# import the random package so that we can generate random numbers
from random import randint

# choices is an array => a container that can hold multiple items
# arrays are 0-based -> the first item is 0, the second is 1, etc
choices = ["Rock", "Paper", "Scissors"]
player = False

player_lives = 5
computer_lives = 5

# make the computer choose a weapon from the choices array at random
computer = choices[randint(0, 2)]

# def win or lose function


def winorlose(status):
    print("Called win or loose function")
    print("***********************************")
    print("you", status, " ! Would you like to play again")
    choice = input ("Y / N:")

    #reset the lives
    if choice == "Y" or choice == "y":
        #change global variables
        global player_lives
        global computer_lives
        global player
        global computer

        player_lives = 5
        computer_lives = 5
        player = False
        computer = choices[randint(0, 2)]

    elif choice == "N" or choice == "n":
        print("You chose to quit")
        print("***********************************")
        exit()

# showe the computer's choice to the terminal window
print("computer chooses: ", computer)

# set up our loop
while player is False:
    print("=====================================")
    print ("player lives", player_lives, "/5")
    print ("computer lives", computer_lives, "/5")
    print("=====================================")
    # set player to True by making a selection
    print("Choose your weapon!\n")
    player = input("Rock, Paper or Scissors?\n")
    print("player chooses:", player)

    # check for a tie = choices are the same
    if (player == computer):
        print("Tie! You live to shoot another day")

    # check to see if the computer choice beats our choice or not
    elif player == "Rock":
        if computer_choice == "Paper":
            # computer won. crap!
            player_lives = player_lives - 1
            print("You lose!", computer, "covers", player)
        else:
            # we win! such winning
            computer_lives = computer_lives - 1
            print("You win!", player, "smashes", computer)

    elif player == "Paper":
        if computer_choice == "Scissors":
            player_lives = player_lives - 1
            print("You lose!", computer_choice, "cut", player)

        else:
            computer_lives = computer_lives - 1
            print("You win!", player, "covers", computer)

    elif player == "Scissors":
        if computer_choice == "Rock":
            player_lives = player_lives - 1
            print("You lose", computer, "smashes", player)
        else:
            computer_lives = computer_lives - 1
            print("You win", player, "cut", computer)
    elif player == "quit":
        exit()

    else:
        print("Check your spelling... that's a not a valid choice\n")

    # check for win or lose
    if player_lives is 0:
        winorlose("lose")

    if computer_lives is 0:
        winorlose("won")

    # reset the game loop and start over again
    player = False
    computer_choice = choices[randint(0, 2)]
