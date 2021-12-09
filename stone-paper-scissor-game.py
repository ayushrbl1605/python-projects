import random
def game(pName,pChoice):
    computerChoices= ["stone","paper","scissor"]
    computerChoice = random.choice(computerChoices)
    print("Computer Choice is " + computerChoice)
    print("player choice : " + pChoice.lower())
    playing = "y"

    if (pChoice.lower() != "s" and pChoice.lower() != "p" and pChoice.lower() != "x"):
        print( f"It's a Wrong entry {pName} " )
    else:
        if (pChoice.lower() == "s"):
            if (computerChoice == "scissor"):
                print(pName + " wins")
            elif (computerChoice == "paper"):
                print("Computer wins")
            else:
                print("It's a draw")
        elif (pChoice.lower() == "p"):
            if (computerChoice == "stone"):
                print(pName + " Wins")
            elif (computerChoice == "scissor"):
                print("Computer wins")
            else:
                print("It's a draw")
        else:
            if (computerChoice == "paper"):
                print(pName + " Wins")
            elif (computerChoice == "stone"):
                print("Computer wins")
            else:
                print("It's a draw")
    playing = (input("Do you want to play again (y/n) : "))
    if (playing == "y"):
        playerChoice = input("Input Player Choice : Stone(s) , Paper (p), Scissor (x): ")
        game(playerName, playerChoice)
    else:
        print( f"It's an end,thank you for playing the game {playerName}")


playerName = input("Enter your name: ")
playerChoice = input("Input Player Choice : Stone(s) , Paper (p), Scissor (x): ")
game(playerName, playerChoice)