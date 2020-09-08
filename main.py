#import user
import re
import random

points = 0
with open("data/songs.txt", "r") as songs:
    lineCount = songs.read().splitlines()
    #songName, artistName = line.split(',')
    #print(f"Song is {songName} by {artistName}")

def addPoints(num: int):
    points = points + num

def game():
    line = random.choice(lineCount)
    songName, artistName = line.split(',')
    print(re.sub('[^A-Z]', ' _ ', songName))
    guess = input("What is your guess? ")
    if guess == songName:
        addPoints(3)
        print("Correct!")
        game()
    print(f"Your score: {points}")

game()