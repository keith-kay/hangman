import random
import time

# Initisl steps to invite in the game

print("\nWelcome to Hangman!\n")
name = input("\nWhat is your name?")
print("Hello " + name + "! Good Luck")
time.sleep(1)
print("Loading")
time.sleep(2)
print("The game is about to start! \n Let us play Hangman")
time.sleep(3)

# Parameters we require to execute
def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    # a words list to guess from - you can make it as big or as small as you wish
    words_list = ["march", "superb", "fantastic", "splendid", "spiderman", "deathstroke", "mombasa",
                  "chocolate", "cairo", "warsaw"]
    word = random.choice(words_list)
    #print(word)

    length = len(word)
    count = 0 #initially
    display = '_'
    already_guessed = []
    play_game = ""

# this will be a loop to re-execute the game when first attempt is done.
def play_loop():
    global play_game
    play_game = input("Wanna play again? y=yes, n=no\n")
    while play_game not in ["y", "n", "Y", "N"]:
        play_game = input("Wanna play again? y = yes, n = no \n")
    if play_game == "y":
        main()
    elif play_game == "n":
        print("Bye! See you later !")
        exit()

#initializing  all the conditions required for the game

def hangman():
    
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    #limit : you can increase it or decrease it as you like [difficulty level]
    limit = 5
    guess = input("this is  the Hangman word: " + display + "Enter your guess: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid input! try a letter, please!\n")
        hangman()
    elif guess in already_guessed:
        print("Try another letter.\n")
    else:
        count+=1
        if count == 1:
            time.sleep(1)
            # drawing the shape manually, this will take some time:D
            print("   _ _ _ _ _ _ _ _ \n"
                  "  |                \n"
                  "  |                \n"
                  "  |                \n"
                  "  |                \n"
                  "  |                \n"
                  "  |                \n"
                  "  |                \n"
                  "  |                \n"
                  "  |                \n"
                  "  |                \n"
                  " _|_ _ _ _ _ _ _ _ \n")
            print("Wrong guess! " + str(limit - count))
        elif count == 2:
            time.sleep(1)
            print("   _ _ _ _ _ _ _ _ \n"
                  "  |                | \n"
                  "  |                | \n"
                  "  |                | \n"
                  "  |                \n"
                  "  |                \n"
                  "  |                \n"
                  "  |                \n"
                  "  |                \n"
                  "  |                \n"
                  "  |                \n"
                  " _|_ _ _ _ _ _ _ _ \n")
            print("Wrong guess!" + str(limit - count) + "remaining guesses!")
        elif count == 3:
            time.sleep(1)
            print("   _ _ _ _ _ _ _ _ \n"
                  "  |                | \n"
                  "  |                | \n"
                  "  |                | \n"
                  "  |                \n"
                  "  |                \n"
                  "  |                \n"
                  "  |                \n"
                  "  |                \n"
                  "  |                \n"
                  "  |                \n"
                  " _|_ _ _ _ _ _ _ _ \n")
            print("Wrong guess!" + str(limit - count) + "remaining guesses!")
        elif count == 4:
            time.sleep(1)
            print("   _ _ _ _ _ _ _ _ \n"
                    "  |                | \n"
                    "  |                | \n"
                    "  |                | \n"
                    "  |                0 \n"
                    "  |               /|\ \n"
                    "  |                \n"
                    "  |                \n"
                    "  |                \n"
                    "  |                \n"
                    "  |                \n"
                    " _|_ _ _ _ _ _ _ _ \n")
            print("Wrong guess!" + str(limit - count) + "last remaining guess")
        else:
            time.sleep(1)
            print("   _ _ _ _ _ _ _ _ \n"
                    "  |                | \n"
                    "  |                | \n"
                    "  |                | \n"
                    "  |                0 \n"
                    "  |               /|\ \n"
                    "  |                \n"
                    "  |                \n"
                    "  |                \n"
                    "  |                \n"
                    "  |                \n"
                    " _|_ _ _ _ _ _ _ _ \n")
            print("Wrong guess! You are hanged !!")
            print("The word was: ", already_guessed, word)
            play_loop()
    
    if word == "-" * length:
        print("Congrats !!! You are alive!")
        play_loop()
    elif count != limit:
        hangman()


main()
hangman()