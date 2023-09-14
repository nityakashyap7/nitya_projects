"""
Nitya Kashyap
Lab 5
CIS 41A
"""

import re
import csv
from game import Game


class CustomGame(Game):
    GAME_RECORD_FILE = "save.csv"

    def __init__(self):
        '''
        constructor/init magic method.
        accepts no parameters (except self)
        creates a CustomGame object, prompts user for name and time limit
        '''
        self._highscore = 0
        self._topPlayers = []
        self._firstRun = False
        self._name = input("Enter your name: ").strip() # shd include strip() so that no extra whitespace

        try:
            with open(CustomGame.GAME_RECORD_FILE) as infile:
                reader = csv.reader(infile)

                nameFound = False

                for line in reader:
                    self._topPlayers.append(line[0])
                    self._highscore = float(line[1])
                    # ^^ this is a bit of repetition, since all the highscores in the file are the same at
                    # any point in time. but if I take the highscore simply from the first line, then
                    # the name on the first line gets skipped in the for loop, since the input marker has
                    # been moved to the 2nd line, and I'm not sure how to move the input marker back
                    # to the beginning of the file in Python; I only know how to do that in C++.
                    # So I hope this implementation is okay
                    # I do fully realize that it requires the interpreter to repeat some work
                    if self._name in line:
                        nameFound = True

                if nameFound:
                    print(f"Welcome back {self._name}")
                else:
                    print(f"Welcome to the game, {self._name}")

        except FileNotFoundError:
            print(f"Welcome to the game, {self._name}")
            self._firstRun = True

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
        """
        helper method (hence private), writes a new score to the csv file (either write or append mode)
        :param score: float of user's normalized score
        :param writeMode: either "w" for write or "a" for append
        :return: nothing
        """
        with open(CustomGame.GAME_RECORD_FILE, writeMode) as outfile:
            writer = csv.writer(outfile)
            writer.writerow([self._name, score])

    def printTopPlayers(self):
        """
        prints to console the names of the top players
        :return: nothing
        """
        print(f"Top players:",', '.join(self._topPlayers))

    def play(self):
        """
        calls the mainloop() function to take care of GUI, calculates the normalized score,
        prints appropriate result message to console (which, in some cases, includes list of top players)
        :return: nothing
        """
        self.mainloop()
        print(f"Your score is: {self._score}")
        normalizedScore = round(self._score / self._timeLimit, ndigits=1)

        if self._firstRun:
            print("Congratulations! Your name is the first in the list of top players")
            self.__recordNewScore(normalizedScore, 'w')
            self._topPlayers = [self._name] # nothing in list yet, so this is the first
            self.printTopPlayers()

        elif normalizedScore > self._highscore:
            print("Congratulations! Your name is entered in the list of top players")
            self.__recordNewScore(normalizedScore, 'w')
            self._topPlayers = [self._name] # previous names are eliminated because they're no longer the best
            self.printTopPlayers()

        elif normalizedScore == self._highscore:
            print("Congratulations! Your name is entered in the list of top players")
            if self._name not in self._topPlayers:
                self.__recordNewScore(normalizedScore, 'a')
                self._topPlayers.append(self._name) # preceding names not erased because those are still highest score
            self.printTopPlayers()

        else:
            print("Good game. Try again to beat the best score")


cg = CustomGame()
cg.play()
