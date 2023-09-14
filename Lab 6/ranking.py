"""
Nitya Kashyap
CIS 41A
Lab 6
3/21/2023
"""

import re

class Ranking:
    '''
    {
    lang1: [ranking, change]
    lang2: [ranking, --]
    lang3: [ranking, change]
    }
    '''
    def __init__(self, file="lab6.txt"):
        self._filename = file
        self._numLanguages = 0
        self._minChange = 0   # needed later for sorting languages by change
        # ^^ FYI: python also has a infinity number!!
        print("created ranking obj")

        self._table = {}
        with open(file) as infile:
            for line in infile:
                for row in re.finditer(r"<tr>(.*?)</tr>", line):   # each
                    lst = re.findall(r"<td>(.+?)%*</td>", row.group())
                    if len(lst) == 6:
                        self._table[lst[3]] = [float(lst[4]), float(lst[5])]
                        self._numLanguages += 1
                        if self._minChange > float(lst[5]):
                            self._minChange = float(lst[5])
                    elif len(lst) == 3:
                        self._table[lst[1]] = [float(lst[2]), "(no change info)"]
                        self._numLanguages += 1


    def _getTable(self): # method for testing purposes
        return self._table

    def getNumLanguages(self):
        '''
        :return: number of languages in dictionary
        '''
        return self._numLanguages

    def getFileName(self):  # this had to be done here because the default file name is not known to UI class
        '''
        :return: name of the file that the data was read in from
        '''
        return self._filename

    def _sortByRank(self, k):
        return self._table[k][0]

    def _sortByChange(self, k):
        try:
            float(self._table[k][1])
        except ValueError:
            return self._minChange - 1  # pushes languages with no change data to the very bottom of sorted dictionary
        return self._table[k][1]

    def RankGen(self):
        '''
        Contains enerator expression of all languages sorted by rank (descending)
        :return: generator
        '''
        gen = ([v, self._table[v][0]] for v in sorted(self._table, key=self._sortByRank, reverse=True))
        return gen

    def ChangeGen(self, pos):
        '''
        Generator function to yield languages sorted by change (descending)
        :param pos: boolean, get all positive changes or negative changes
        :return: list of language name and change
        '''
        count = 0
        for value in sorted(self._table, key=self._sortByChange, reverse=True):
            if count == 20: # stop at 20 because all entries after that don't have change data
                break
            if pos:
                if self._table[value][1] > 0:
                    yield [value, self._table[value][1]]
            else:
                if self._table[value][1] < 0:
                    yield [value, self._table[value][1]]
            count += 1

    def searchLang(self, *args):
        '''
        retrieves data on each of the languages passed in
        :param args: a tuple of language names
        :return: list of language name, rank, change grouped in a list for every language searched
        '''
        output = []
        for lang in args:
            found = False
            for key in self._table:
                if lang.lower() == key.lower():
                    output.append([key,str(self._table[key][0]),str(self._table[key][1])])
                    found = True
            if not found:
                output.append([f"{lang} not found"])
        return output

# Method testing code (pls ignore):
# def sortedList(lst):
#     for element in sorted(lst):
#         yield element
#
# myList = [3, 1, 4, 1, 5, 9]
# for element in sortedList(myList):
#     print(element)
#
# r = Ranking()
# print(r.searchLang("C","f#","peRl"))
# print(r._getTable())
# g = r.ChangeGen(True)
# for val in g:
#     print(val)
# # for lang in g:
# #     print(lang)
#
# print(r.getNumLanguages())

