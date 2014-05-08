import random

## Superclass for HumanPlayer and Computer Player.
class Player:
    
    def __init__(self, name):
        self.name = name

    ## Returns name of Player
    def getName(self):
        return self.name

    def getGuess(self):
        return 0



class HumanPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    ## Overrides the base class function - gets int 0-100 from user.        
    def getGuess(self):
        return int(input("Please enter a number between 0 and 100:"))


class ComputerPlayer(Player):
    def __init__(self, name):
        super().__init__(name)
        self.lastGuess = 0
        self.low = 0
        self.high = 100

    ## Overrides the base class function - gets int between low and high values.
    def getGuess(self):
        self.lastGuess = random.randint(self.low, self.high)
        return self.lastGuess

    ## Takes answer from CheckForWin() and asjusts internal low and high values
    def lastAnswer(self, hOl):
        if hOl == "high":
            self.high = (self.lastGuess - 1)

        if hOl == "low":
            self.low = (self.lastGuess + 1)

        return

    ## Clears Values for new game.
    def clearValues(self):
        self.lastGuess = 0
        self.low = 0
        self.high = 100
        

def guessingGame(player1, player2): 
    answer = random.randint(0, 100)

    ## Clears Computer Player values for game
    if type(player1) is ComputerPlayer:
        player1.clearValues()
    if type(player2) is ComputerPlayer:
        player2.clearValues()
        
    while(True): 
        print(player1.getName()+"'s turn to guess: ", end="") 
        guess = player1.getGuess() 
        if checkForWin(player1, guess, answer): 
            return 
        print(player2.getName()+"'s turn to guess: ", end="") 
        guess = player2.getGuess() 
        if checkForWin(player2, guess, answer): 
            return 
 
 
def checkForWin(player, guess, answer): 
    print(player.getName(),"guesses", guess) 
    if answer == guess: 
        print("You're right! You win!\n") 
        return True 
    elif answer < guess: 
        print("Your guess is too high.\n")
        if type(player) is ComputerPlayer:
            player.lastAnswer("high")
    else: 
        print("Your guess is too low.\n") 
        if type(player) is ComputerPlayer:
            player.lastAnswer("low")
    return 


def main():
    random.seed()
    humanOne = HumanPlayer("Human Player 1")
    humanTwo = HumanPlayer("Human Player 2")
    computerOne = ComputerPlayer("Computer Player 1")
    computerTwo = ComputerPlayer("Computer Player 2")

    guessingGame(humanOne, humanTwo)
    
    guessingGame(humanOne, computerOne)

    guessingGame(computerOne, computerTwo)






main()

    
    
