from random import randint as r
class Game():
    RPS = {1: "rock", 2:"paper", 3:"scissor"}

    def playerInput(self):
        print("\nEnter 1 for rock; 2 for paper; or 3 for scissors")
        pinput = input("or type 'quit' to quit: ")
        if pinput == "1":
            self.rock()
        elif pinput == "2":
            self.paper()
        elif pinput == "3":
            self.scissors()
        elif pinput.lower() == "quit":
            quit()
        else:
            print("Invalid answer")


    def computerInput(self):
        rndm = r(1,3)
        if rndm== 1:
            print("I chose rock")
        if rndm == 2:
            print("I chose paper")
        if rndm == 3:
            print("I chose scissors")
            if self.scissors() == self.RPS[3]:
                print("Player scissors")
    
    def rock(self):
        print(f"You chose {self.RPS[1]}")

    def paper(self):
        print(f"You chose {self.RPS[2]}")

    def scissors(self):
        print(f"You chose {self.RPS[3]}")

    def decideVictor(self):
        # IF PLAYER CHOOSE 1,2,3
        # if COMP CHOSE 1,2,3
        # DECIDE WHO WINS
        pass

    def play(self):
        while self.playerInput() != "quit":
            self.computerInput()

def main():
    Game().play()

main()