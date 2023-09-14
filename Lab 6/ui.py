"""
Nitya Kashyap
CIS 41A
Lab 6
3/21/2023
"""

from ranking import Ranking

class UI:
    def __init__(self):
        done = False
        while not done:
            filename = input("enter a filename: ")
            try:
                if len(filename) == 0:
                    self._RObj = Ranking()
                else:
                    self._RObj = Ranking(filename)
                done = True
            except IOError:
                print("file not found, please try again.")
        print(f"Ranking for {self._RObj.getNumLanguages()} languages from {self._RObj.getFileName()}")

    def printByRank(self):
        '''
        uses a generator to print out the languages in order of descending rank
        :return: none
        '''
        g = self._RObj.RankGen()
        print("Printing one language at a time\nAfter each language, press Enter to continue, any other key to stop")
        end = False
        while not end:
            if input() == "":
                try:
                    lang = next(g)
                    print(lang[0], lang[1])
                except StopIteration:
                    print("no more languages left to print\n\n")
                    end = True
            else:
                end = True

    def printByChange(self):
        '''
        uses a generator to print out the languages in order of descending change
        :return: none
        '''
        valid = False
        while not valid:
            choice = input("positive or negative change? (n/p): ")
            if choice.lower() == "p":
                pos = True
                valid = True
            elif choice.lower() == "n":
                pos = False
                valid = True
            else:
                print("invalid choice, try again.")
        g = self._RObj.ChangeGen(pos)
        for lang in g:
            print(lang[0], "\t", lang[1])

    def printInfo(self):
        '''
        prints out the name, rank, and change for each language inputed
        :return: none
        '''
        languages = input("Enter language names, separated by comma: ").split(",")
        languages = [v.strip() for v in languages]
        info = self._RObj.searchLang(*(languages))
        print("Language", " "*16, "Rank", " "*4, "Change", " "*4)
        for lst in info:
            if len(lst) == 1:
                print(f"{lst[0]:25s}")
            else:
                print(f"{lst[0]:25s}", "\t\t".join(lst[1:]))

    def run(self):
        '''
        runs the program, calling the other methods to do the printing, etc.
        :return: none
        '''
        funcD = {
            "r" : self.printByRank,
            "c" : self.printByChange,
            "l" : self.printInfo,
        }
        end = False
        while not end:
            choice = input("r. Languages by ranking\nc. Languages by change\nl. Language info\nq. Quit\nEnter choice: ")
            choice = choice.lower()
            if choice == "q":
                end = True
            elif choice in funcD:
                funcD[choice]()
                print()
            else:
                print("r, c, l, or q only")


UI().run()