#import user
import re

with open("data/songs.txt", "r") as songs:
    for line in songs:
        songName, artistName = line.split(',')
        #print(f"Song is {songName} by {artistName}")
        print(re.sub('[^A-Z]', ' _ ', songName))