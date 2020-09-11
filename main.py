import re
import random
import time
import threading
import configparser
import getpass

with open("data/songs.txt", "r") as songs:
    lineCount = songs.read().splitlines()

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
    raise SystemExit
    # bestUser, bestPoints = "", -1
    # for line in scoreFile:
    #     name, score = line.split(':')
    #     if score > bestPoints:
    #         bestUser = username
    #         bestPoints = points
    # print(f"Best Points {bestPoints}")
    # print(f"Best User {bestUser}")

    # for line in scoreFile.readlines():
    #     user, score = line.split(':')
    #     if score.isdigit() and points > score:
    #         points = int(score)

    # if int(points) > score:
    #     scoreFile.write(f"{username}:{points}")
    # scoreList = []
    # for line in scoreFile.readlines():
    #     user, score = line.split(':')
    #     score = int(score.strip())
    #     name = name.strip()
    #     scoreList.append(f"{username}:{points}")
    #     print(scoreList)

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
