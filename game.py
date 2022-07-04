import random, sys

print("ROCK, PAPPER, SCISSORS")

wins = 0
losses = 0
ties = 0

while True:
    print("%s Win, %s Losses, %s Ties" % (wins, losses, ties))
    
    while True:
        print("Enter Your move: (r)ock (p)aper (s)cissors or (q)uit")
        playermove = input()
        
        if playermove == "q":
            sys.exit()
        if playermove == "r" or playermove == "p" or playermove == "s" :
            break
    if playermove == "r" :
        print("ROCK versus.....")
    elif playermove == "p":
        print("PAPER versus....")
    elif playermove == "s":
        print("SCISSORS versus....")
        
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = "r"
        print("ROCK")
    elif randomNumber == 2:
        computerMove = "p"
        print("PAPER")
    elif randomNumber == 3:
        computerMove = "s"
        print("SCISSORS")
    
    if playermove == computerMove:
        print("it is a tie")
        ties = ties + 1
    elif playermove == "r" and computerMove == "s":
        print("You win! ")
        wins = wins + 1
    elif playermove == "p" and computerMove == "r":
        print("You win!")
        wins = wins + 1
    elif playermove == "s" and computerMove == "p":
        print("You win!")
        wins = wins + 1
        
    elif playermove == "r" and computerMove == "p":
        print("You loss!")
        losses = losses + 1
    elif playermove == "p" and computerMove =="s":
        print("You loss!")
        losses = losses + 1
    elif playermove == "s" and computerMove == "r":
        print("You loss!")
        losses = losses + 1
            
        