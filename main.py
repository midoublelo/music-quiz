import re
import random
import time
import threading
import configparser
import getpass
import operator

songs = open("data/songs.txt", "r")
lineCount = songs.read().splitlines()

# with open("data/songs.txt", "r") as songs:
#     lineCount = songs.read().splitlines()

# config = SafeConfigParser()
# config.read('settings.ini')

# config = configparser.ConfigParser()
# config['accounts'] = {'Registration': 'False'}
# config['countdown'] = {'Enabled': 'False',
#                         'Timer': '15'}
# with open("config.ini", 'w') as configfile:
#     config.write(configfile)

# config = configparser.ConfigParser()
# config.read('config.ini')

# timerEnabled = config['countdown']['enabled']
timerEnabled = False
# timer = config['countdown']['timer']
timer = 15

points = 0
username = ""

with open("data/message.txt", "r") as message:
    print(message.read())

def welcome():
    hasAccount = input("Do you already have an account? [y/n] ")
    if hasAccount.lower() == "y":
        login()
    if hasAccount.lower() == "n":
        register()
    else:
        welcome()

def login():
    global username
    nameInput = input("Enter your username: ").lower()
    passInput = getpass.getpass('Enter your password: ')
    with open("data/users.txt", "r") as users:
        if (nameInput + ":" + passInput + "\n") in users.readlines():
            print("Logged in successfully.")
            # print(timerEnabled)
            username = nameInput
            game()
        else:
            print("Username or Password is incorrect!")
            login()

def register():
        nameInput = input("Enter your desired username: ")
        passInput = getpass.getpass("Enter your desired password: ")
        with open("data/users.txt", "a+") as users:
            users.write(nameInput + ":" + passInput + "\n")
            print(f"Created account for '{nameInput}'")
        login()

def gameOver():
    global username
    global points
    print("Game over!")
    print(f"Your score: {points}")
    with open("data/scores.txt", "a+") as scoreFile:
        scoreFile.write(f"{username}:{points}\n")
    topScores()

def topScores():
    scores = {}
    with open("data/scores.txt", "r") as scoreFile:
        for line in scoreFile.readlines():
            scores[line.split("'")[0].strip()] = int(line.split(':')[1].strip())
            # songName, artistName = line.split(',')
    print(sorted(scores.items(), key=lambda x: x[1])[::-1])[:5]


# def countdown():
#     global timer
#     for i in range(timer):
#         time.sleep(1)
#         timer -= 1
#         if timer == 0:
#             print("\nTimes up!\nType anything to close the game.")
#             gameOver()
#             exit()

def game():
    global points
    global timer
    # if timerEnabled == True:
    #     t = threading.Thread(target=countdown)
    line = random.choice(lineCount)
    songName, artistName = line.split(',')
    print(re.sub('[^A-Z]', ' _ ', songName) + f"by {artistName}")
    if timerEnabled == True:
        # t.start()
        guess = input(f"What is your guess? ({timer}s): ")
    else:
        guess = input("What is your guess? ")
    if guess.lower() == songName.lower() or guess == songName:
        print("Correct! +3 Points")
        points = points + 3
        timer = 15
        game()
    elif timer != 0:
        print("Incorrect! One more guess..!")
        print(re.sub('[^A-Z]', ' _ ', songName) + f"by {artistName}")
        if timerEnabled == True:
            guess = input(f"What is your guess? ({timer}s): ")
        else:
            guess = input("What is your guess? ")
        if guess.lower() == songName.lower() or guess == songName:
            print("Correct! +1 Points")
            points = points + 1
            timer = 15
            game()
        else:
            gameOver()

welcome()
