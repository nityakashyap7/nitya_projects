import re
import csv
from game import Game


class CustomGame(Game):
    GAME_RECORD_FILE = "save.csv"

    def __init__(self):
        # self._highscore = 0
        self._topPlayers = []
        self._firstRun = False
        self._name = input("Enter your name: ")

        try:
            with open(CustomGame.GAME_RECORD_FILE) as infile:
                reader = csv.reader(infile)
                nameFound = False

                for line in reader:
                    self._topPlayers.append(tuple((line[0],float(line[1]))))
                    if self._name in line:
                        nameFound = True

                if nameFound:
                    print(f"Welcome back {self._name}")
                else:
                    print(f"Welcome to the game, {self._name}")
        except FileNotFoundError:
            print(f"Welcome to the game, {self._name}")
            self._firstRun = True
            print("first run")
        print(self._topPlayers)
        self._timeLimit = input("Enter time limit (20-60s), or press Enter for 20s: ")
        m = re.search(r'^[^-\d]*(\d+)[^.\d]*$', self._timeLimit, re.I)
        try:
            self._timeLimit = int(m.group(1))
            if not 20 <= self._timeLimit <= 60:
                raise ValueError
            else:
                print(f"{self._timeLimit}s time limit")
        except (AttributeError, ValueError):
            print("invalid input. The limit is being set to the default 20s")
            self._timeLimit = 20
        super().__init__(self._timeLimit)

    def __recordNewScore(self, score, writeMode):
        with open(CustomGame.GAME_RECORD_FILE, writeMode) as outfile:
            writer = csv.writer(outfile)
            writer.writerow([self._name, score])

    def printTopPlayers(self):
        print(f"Top players: ")


    def play(self):
        self.mainloop()
        print(f"Your score is: {self._score}")
        normalizedScore = round(self._score / self._timeLimit, ndigits=1)
        highscore = self._topPlayers[0][1]
        for player in self._topPlayers:
            if player[1] > highscore:
                highscore = player[1]
        print("normalized score", normalizedScore)
        print("highscore", highscore)
        if self._firstRun:
            print("Congratulations! Your name is the first in the list of top players")
            self.__recordNewScore(normalizedScore, 'w')
            self._topPlayers = [self._name]
            self.printTopPlayers()
        elif normalizedScore > highscore:
            print("greater than")
            print("Congratulations! Your name is entered in the list of top players")
            self.__recordNewScore(normalizedScore, 'w')
            self._topPlayers = [self._name]
            self.printTopPlayers()
        elif normalizedScore < highscore:
            print("less than")
            print("Good game. Try again to beat the best score")
        else:
            print("equal to")
            print("Congratulations! Your name is entered in the list of top players")
            if self._name not in self._topPlayers:
                self.__recordNewScore(normalizedScore, 'a')
                self._topPlayers.append(self._name)
            self.printTopPlayers()



cg = CustomGame()
cg.play()
