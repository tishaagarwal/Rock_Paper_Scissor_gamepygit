import pyttsx3
from random import randint

# moves for player
moves = ["rock", "paper", "scissor"]

# speak
speaker = pyttsx3.init()
# it will say something
speaker.say("Welcome to the  game")
# it will wait to listen
speaker.runAndWait()

while True:
    computer = moves[randint(0, 2)]
    speaker.say("choose rock paper or scissor ")
    speaker.runAndWait()
    player = input("(rock, paper,scissor)?(end game)").lower()
    # lower = lower case
    if player == "end game":
        print("Game has ended")
        speaker.say("Game has ended ")
        speaker.runAndWait()
        break
    elif player == computer:
        print("Tie !!")
        speaker.say("Tie , try again")
        speaker.runAndWait()

    elif player == "rock":
        if computer == "paper":
            print("LOSE!!")
            speaker.say("lose try again ")
            speaker.runAndWait()

        else:
            speaker.say("You won ")
            speaker.runAndWait()
            print("Win..", player, "beats", computer)


    elif player == "paper":
        if computer == "scissor":
            speaker.say("lose try again ")
            speaker.runAndWait()
            print("LOSE!!")

        else:
            speaker.say("You won ")
            speaker.runAndWait()
            print("Win..", player, "beats", computer)

    elif player == "scissor":
        if computer == "rock":
            speaker.say("lose try again ")
            speaker.runAndWait()
            print("LOSE!!")
        else:
            speaker.say("You won ")
            speaker.runAndWait()
            print("Win..", player, "beats", computer)

    else:
        print("Check your spelling....")
        speaker.say("choose rock paper or scissor ")
        speaker.runAndWait()
