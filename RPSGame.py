# import the random package so that we can generate random numbers
from random import randint

player_wins = 5 
computer_wins = 5
# choices is an array => a container that can hold multiple items
# arrays are 0-based -> the first item is 0, the second is 1, etc
choices = ["Rock", "Paper", "Scissors"]
player = False

print("""
Player Wins:{}
Computer Wins:{}""".format(player_wins, computer_wins))

# make the computer choose a weapon from the choices array at random
computer_choice = choices[randint(0, 2)]

# print the choise to the terminal window
print("Computer chooses: ", computer_choice)

# set up our loop
while player is False:
    # set player to True by making a selection
    print("Choose your weapon!")
    player = input("Rock, Paper or Scissors?\n")

    print(player, "\n")


    # check for a tie = choices are the same
    if player == computer_choice:
        print("Tie! You live to shoot another day")

    # check to see if the computer choice beats our choice or not
    elif player == "Rock":
        if computer_choice == "Paper":
            # computer won. crap!
            print("You lose! Copmuter chooses:", computer_choice)
            player_wins -=1
        else:
            # we win! such winning
            print("You win! Copmuter chooses:", computer_choice, player, "smashes", computer_choice)
            computer_wins -=1

    elif player == "Paper":
        if computer_choice == "Scissors":
            print("You lose! Copmuter chooses:", computer_choice, computer_choice, "cut", player)
            player_wins -=1
        else:
            print("You win! Copmuter chooses:", computer_choice, player, "covers", computer_choice)
            computer_wins -=1

    elif player == "Scissors":
        if computer_choice == "Rock":
            print("You lose! Copmuter chooses:", computer_choice, computer_choice, "smashes", player)
            player_wins -=1
        else:
            print("You win! Copmuter chooses:", computer_choice, player, "cut", computer_choice)
            computer_wins -=1
    elif player == "quit":
        exit()
    else:
        print("Check your spelling... that's a not a valid choice\n")

    print("""
Player Wins:{}
Computer Wins:{}""".format(player_wins, computer_wins))

    # reset the game loop and start over again


    if player_wins == 0:
        print("Computer won the game")
        play_again = input("Would you like to play again? (Y/N) >")
        if (play_again == "Y"):
            player_wins = 5
            computer_wins = 5
            continue
        else:
            exit()

    elif computer_wins == 0:
        print("You won the game")
        play_again = input("Would you like to play again? (Y/N) >")
        if (play_again == "Y"):
            player_wins = 5
            computer_wins = 5
            continue
        else:
            exit()

    if player_wins > computer_wins:
        print ("You're winning!")
    elif player_wins < computer_wins:
        print ("You're in trouble, you're losing")
    else:
        print("The game is tied")

    player = False
    computer_choice = choices[randint(0, 2)]
