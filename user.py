loggedIn = False
loginRegister = input("Do you have an account? [y/n] ")
if loginRegister.lower() == "n":
        registerAcc = input("Would you like to register an account? [y/n] ")
        if registerAcc.lower() == "y":
            nameInput = input("Enter your desired username: ")
            passInput = input("Enter your desired password: ")
            with open('data/users.txt', 'a+') as users:
                users.write(f"\n{nameInput}:{passInput}")  
                print(f"Successfully created account with name {nameInput} and password {passInput}")
                loginRegister = input("Would you like to log in now? [y/n] ")

if loginRegister.lower() == "y":
    nameInput = input("Enter your username: ")
    passInput = input("Enter your password: ")
    with open("data/users.txt", "r") as users:
        if (nameInput + ":" + passInput + "\n") in users.readlines():
              loggedIn == True
              print("Logged in successfully.")
        else:
            print("Username or Password is incorrect!")
    # with open('data/users.txt', 'r') as users:
    #     for line in users:
    #         username, password = line.split(':')
    #         if username == nameInput:
    #             if password == passInput:
    #                 loggedIn = True
    #                 break
    #             else:
    #                 print("Username or Password is incorrect!")

    if loggedIn == True:
        print("Logged in successfully.")