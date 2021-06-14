from random import randint
class Game():
    # RPS = {1: "rock", 2:"paper", 3:"scissor"}
    pinput = ""
    rndm = 0
    
    def playerInput(self):
        print("\nEnter 1 for rock; 2 for paper; or 3 for scissors")
        self.pinput = input("or type 'quit' to quit: ")
        if self.pinput == "1":
            print("> You chose rock")
        elif self.pinput == "2":
            print("> You chose paper")
        elif self.pinput == "3":
            print("> You chose scissors")
        elif self.pinput.lower() == "quit":
            quit()
        else:
            print("Invalid answer")


    def computerInput(self):
        self.rndm = randint(1,3)
        return self.rndm
    #     if rndm == 1:
    #         print("< I chose rock")
    #         return rndm
    #     elif 2:
    #         print("< I chose paper")
    #         return rndm
    #     elif 3:
    #         print("< I chose scissors")
    #         return rndm
    
    # def rock(self):
    #     print(f"> You chose {self.RPS[1]}")

    # def paper(self):
    #     print(f"> You chose {self.RPS[2]}")

    # def scissors(self):
    #     print(f"> You chose {self.RPS[3]}")

    def decideVictor(self):
        self.computerInput()
        if self.pinput == "1":
            if self.rndm == 1:
                print("< I chose rock")
                print("Tie Game!")
            elif self.rndm == 2:
                print("< I chose paper")
                print("I Win!")
            elif self.rndm == 3:
                print("< I chose scissors")
                print("You win!")
        elif self.pinput == "2":
            if self.rndm == 1:
                print("< I chose rock")
                print("You win!")
            elif self.rndm == 2:
                print("< I chose paper")
                print("Tie Game!")
            elif self.rndm == 3:
                print("< I chose scissors")
                print("I win!")
        elif self.pinput == "3":
            if self.rndm == 1:
                print("< I chose rock")
                print("I win!")
            elif self.rndm == 2:
                print("< I chose paper")
                print("You win!")
            elif self.rndm == 3:
                print("< I chose scissors")
                print("Tie Game!")

    def play(self):
        print("Rock, Paper, Scissors!\nCan you beat me?")
        while self.playerInput() != "quit":
            self.decideVictor()

def main():
    Game().play()

main()