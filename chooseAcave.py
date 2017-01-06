from random import randint as rand
from time import sleep as sleep

def game():
    # Choose A Cave game menu
    print("Welcome to Choose A Cave!!! (A game of luck and... um... luck)")
    print("To play the game, type 'play'. To learn how to play, type 'info'. To see credits, type, well, you get it.")
    gamecmd = input("Type 'play' or 'info' or 'credits':")
    if gamecmd == "play":
      pass
    if gamecmd == "info":
      print("Just pick a random number from 1 to eight and hope you get it right!")
      sleep(0.5)
      print("The game will now start.")
      sleep(3)
    if gamecmd == "credits":
      print("Created by Kabir Bhatia")
      sleep(0.5)
      print("Coding by Tripp Lyons and Kabir Bhatia")
      sleep(0.5)
      print("Special Thanks to Tripp Lyons and Ronak Monga for helping to bring this game to life!")
      sleep(0.5)
      print("The game will now start.")
      sleep(3)


    lives = 3
    score = 0
    while lives > 0:
        print("--------------------------------------------------------------")
        print("With "+str(lives)+" lives left, you hope to make it out alive...")
        print("Eight caves lay ahead of you, six are filled with zombies.")
        choice = -1
        isgood = False
        while not isgood:
            try:
                choiceInput = input("Pick a cave (1-8): ")
                choice = int(choiceInput)
                isgood = 1 <= choice <= 8
            except ValueError:
                pass

        rnd = rand(0, 8)
        if rnd in range(0, 2):
            print("Yikes! A zombie attacks you, and you try to escape but you are weak.")
            sleep(0.5)
            print("You were eaten by the zombie. GAME OVER!")
            lives = 0
        elif rnd in range(2, 6):
            print("Oh no! A zombie attacks you, but you are able to get away in time.")
            sleep(0.5)
            print("You lose a life!")
            lives -= 1
            score += 1
        else:
            print("This cave was free of zombies... phew!")
            score = score + 1

    print("==============================================================")
    print("Score: "+str(score))


def inputfromchoices(prompt, choices):
    i = input(prompt)
    while i not in choices:
        i = input(prompt)

    return i


def main():
    userwantstoplay = True
    while userwantstoplay:
        game()
        userwantstoplay = inputfromchoices("Would you like to play again? [\"yes\", \"no\"]: ", ["yes", "no"]) == "yes"

main()
