import re
import random

with open("data/songs.txt", "r") as songs:
    lineCount = songs.read().splitlines()

username = ""
points = 0

def logIn():
    global username
    nameInput = input("Enter your username: ")
    passInput = input("Enter your password: ")
    with open("data/users.txt", "r") as users:
        if (nameInput + ":" + passInput + "\n") in users.readlines():
            print("Logged in successfully.")
            username = nameInput
            game()
        else:
            print("Username or Password is incorrect!")

def gameOver():
  global username
  print("Game over!")
  print(f"Your score: {points}")
  with open("data/scores.txt", "r"):
    print("test")

def game():
    global points
    line = random.choice(lineCount)
    songName, artistName = line.split(',')
    print(re.sub('[^A-Z]', ' _ ', songName) + f"by {artistName}")
    guess = input("What is your guess? ")
    if guess == songName:
        print("Correct! +3 Points")
        points = points + 3
        game()
    else:
      print(re.sub('[^A-Z]', ' _ ', songName) + f"by {artistName}")
      guess = input("What is your guess? ")
      if guess == songName:
          print("Correct! +1 Points")
          points = points + 1
          game()
      else:
        gameOver()   

logIn()
