import re
import random
import getpass

songs = open("data/songs.txt", "r") # <- Opens the 'songs.txt' file.
lineCount = songs.read().splitlines() # <- Counts up the lines and splits them.

points = 0 # Global points variable.
username = "" # Stored username of the currently logged in user.

with open("data/message.txt", "r") as message: # Opens the 'message.txt' file.
    print(message.read()) # Prints out a welcome message from the 'message.txt' file.

def welcome():
    '''
    Starting function that allows for
    the user to login or register.
    '''
    hasAccount = input("\nDo you already have an account? [y/n] ") # Asks the user to input whether they have an account.
    if hasAccount.lower() == "y":
        login()
    if hasAccount.lower() == "n":
        register()
    else:
        welcome() # Restarts the welcome screen if the input is invalid.

def login():
    global username
    '''
    This function allows the user to login
    with a pre-existing account. Password is
    protected using the 'getpass' library,
    though this feature is not essential.
    '''
    nameInput = input("Enter your username: ").lower() # Allows the user to input their username.
    passInput = getpass.getpass('Enter your password: ') # Allows the user to input their password. Protected by the 'getpass' library.
    with open("data/users.txt", "r") as users: # Opens the 'users.txt' file.
        if (nameInput + ":" + passInput + "\n") in users.readlines(): # Uses the data inputted by the user to see if their account is in the file.
            print("Logged in successfully.")
            username = nameInput # Sets 'username' to their input so that it can be used later. NOTE: Likely unnecessary, could just use nameInput.
            game()
        else:
            print("Username or Password is incorrect!") 
            login() # If the account details are invalid, call the login function again.

def register():
    '''
    This function lets the user create a new
    account while running the game. Password is
    protected using the 'getpass' library,
    though this feature is not essential.
    '''
    nameInput = input("Enter your desired username: ") # Allows the user to input their desired username.
    passInput = getpass.getpass("Enter your desired password: ") # Allows the user to input their desired password. Visually protected by the 'getpass' library.
    with open("data/users.txt", "a+") as users:
        users.write(nameInput + ":" + passInput + "\n") # Writes account details to 'users.txt' in the same format as the login function.
        print(f"Created account for '{nameInput}'") # NOTE: Could ask user to retype password before registration to verify that they have typed it correctly?
    login()

def gameOver():
    global points
    global username
    '''
    This function prints the user's score and logs
    the score of the user in 'scores.txt'
    '''
    print("\nGame over!")
    print(f"Your score: {points}\n")
    with open("data/scores.txt", "a+") as scoreFile:
        scoreFile.write(f"{username}:{points}\n") # Writes user's score to the file
    topScores()

def topScores():
    '''
    This function prints out the Top 5 Scores
    and the players who got them.
    '''
    with open("data/scores.txt", "r") as scoreFile:
        scoreList = {} # Creates a dictionary to store scores
        scoreLines = scoreFile.readlines() # Reads each line of the score list
        for line in scoreLines: # Loops through each line of the score file
            topName, topScore = line.split(':') # Splits the name and score into different variables from the ':'
            topScore = int(topScore) # Turn the top score into an integer
            if topName not in scoreList or topScore > scoreList[topName]: # Checks if the current user is not in the dictionary or if this is that users highest score
                scoreList[topName] = topScore # Inserts the user and its score into the dictionary
        sortedList = sorted(scoreList.items(), key=lambda x: x[1], reverse=True) # Sorts the list in descending order. Uses the lambda to only sort by the 2nd element, which is the user score. 
        topFive = sortedList[0:5] # Gets a slice of the top 5 elements in the dictionary
        for i in range(5):
            print(f"{i+1}. {topFive[i][0]} - {topFive[i][1]}") # Prints the top 5 results

def game():
    '''
    Function for main game flow.
    '''
    global points
    line = random.choice(lineCount) # <- Chooses a random line from the 'songs.txt' file.
    songName, artistName = line.split(',') # <- Splits the line in two from the ',' and assigns a variable to both sides.
    print(re.sub('[^A-Z]', ' _ ', songName) + f"by {artistName}") # <- Uses a regular expression to replace lower case letters with underscores.
    guess = input("What is your guess? ") # <- Allows for the user to input their song guess.
    if guess.lower() == songName.lower() or guess == songName: # <- Checks the guess in normal and lowercase.
        print("Correct! +3 Points")
        points = points + 3
        game() # <- Since the user got it right, the game will restart.
    else:
        print("Incorrect! One more guess..!")
        print(re.sub('[^A-Z]', ' _ ', songName) + f"by {artistName}")
        guess = input("What is your guess? ")
        if guess.lower() == songName.lower() or guess == songName:
            print("Correct! +1 Points")
            points = points + 1 # <- Gives only 1 point instead of 3 points due to getting it right on the second try.
            game()
        else:
            gameOver() # <- Calls the gameOver function.

welcome()
