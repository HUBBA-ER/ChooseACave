#Choose A Cave game menu
def menu():
  print("Welcome to.... Choose A Cave!! (Or you die)")
  name = input("Enter a name for the leaderboard, please:")
  print("Thank you. To play the game, type 'play' to learn how to play, type 'info' to learn how to play, and credits for credits")
  #Runs menu
menu()
gamecmd = input("Type 'play' or 'info' or 'credits':")
while(gamecmd != "play"):
  if gamecmd == "info":
    print("Just type in a random guessed number between 1 and 8 and hope you get it right... that's all there is to it.")
    doyawanna = input("Want to return to menu? yes or no:")
    if doyawanna == "yes":
        menu()
    else:
        game()
  if gamecmd == "credits":
    print("Created by: Kabir Bhatia, Coding by: Kabir Bhatia and Tripp Lyons, developed by: Tripp Lyons")
    menu()
def game():
    print("gamegamegame")
while(gamecmd == "play"):
    game()
