"""
Nitya Kashyap
Lab 3
CIS 41A
2/4/2023
Description: This program shows the cumulative rainfall in Santa Clara Valley
"""

import csv
import copy

# constants
TXT_INPUT = "city.txt"
CSV_INPUT = "rainfall.csv"
TXT_OUTPUT = "lab3out.txt"


def readData(watershedCities, rainfall):
    """
    populates watershedCities and rainfall dictionaries.
    Prints header with names of watersheds
    :param watershedCities: dictionary of watersheds and their cities
    :param rainfall: dictionary of dictionaries of rainfall sensor data
    :return: none
    """
    # populate the watershedCities dictionary:
    with open(TXT_INPUT) as infile:
        for line in infile:
            line = line.rstrip()  # rid "\n" at the end
            lineList = line.split(sep=": ")  # splits watershed from cities
            watershed = lineList[0]
            cityList = lineList[1].split(", ")  # splits the cities into elements of another list
            watershedCities[watershed] = cityList  # create dictionary entry

    # populate the rainfall dictionary:
    with open(CSV_INPUT) as infile:
        reader = csv.reader(infile)
        for line in reader:
            watershed = line[2]
            sensor = line[0]
            rainAmt = float(line[1])
            if not watershed in rainfall:
                rainfall[watershed] = {}
            rainfall[watershed][sensor] = rainAmt

    print(f"Read in data for {', '.join(watershedCities.keys())} watersheds")

def printOneWatershed(watershedName, watershedCities, rainfall, searchedSet):
    """
    Prints rainfall amount for each sensor in selected watershed
    :param watershedName: string of name of selected watershed
    :param watershedCities: dictionary of watersheds and their cities
    :param rainfall: dictionary of dictionaries of rainfall sensor data
    :param searchedSet: set of searched watersheds and their sensors' rainfall data
    :return: none
    """
    print(f"Sensors for {watershedName} watershed, which includes:")
    print(', '.join(watershedCities[watershedName]))
    for sensor in rainfall[watershedName]:
        print(f"{sensor:35s}{rainfall[watershedName][sensor]:>5.2f}") # right justified
        # also update searchedSet:
        searchedSet.add(f"{watershedName},{sensor},{rainfall[watershedName][sensor]}")

def printAvgRainfall(rainfall):
    """
    Prints average rainfall (from highest to lowest) of the watersheds
    :param rainfall: dictionary of dictionaries of rainfall sensor data
    :return: none
    """
    averages = {}
    # calculate averages
    for watershed in rainfall:
        averages[watershed] = sum(rainfall[watershed].values())/len(rainfall[watershed])

    flippedDict = dict(zip(averages.values(),averages.keys()))

    print(f"Watershed{' '*10}Inches")
    for average in sorted(flippedDict, reverse=True):
        print(f"{flippedDict[average]:19s}{average:>5.2f}")

def printMaxSensors(N, rainfall):
    """
    Prints the top N sensors that have recorded the most rainfall
    :param N: integer number of sensors desired
    :param rainfall: dictionary of dictionaries of rainfall sensor data
    :return: none
    """
    sensorDict = {}
    for watershed in rainfall:
        sensorDict.update(rainfall[watershed])

    if N > len(sensorDict):
        N = len(sensorDict)

    # assume that the rainfall data numbers are unique
    flippedDict = dict(zip(sensorDict.values(),sensorDict.keys()))

    for rainfallAmt in (sorted(flippedDict,reverse=True))[:N]: # default start @ 0
        print(f"{flippedDict[rainfallAmt]}: {rainfallAmt}")

def saveWatershedData(searchedSet):
    """
    Saves all the searched watersheds' sensor data to an output file.
    Duplicate searches are not printed multiple times.
    :param searchedSet: set of searched watersheds + their sensors + sensor data each saved as a string
    :return: none
    """
    with open(TXT_OUTPUT, 'w') as outfile:
        for string in sorted(searchedSet):
            outfile.write(string+"\n")

def getNum(prompt, low, high = None):
    """
    Prompt the user until a valid input is obtained.
    :param prompt: string that the user should be prompted with
    :param low: the lowest valid int number
    :param high: the highest valid int number (optional parameter)
    :return: validated user choice as an int
    """
    isValid = False
    while not isValid:
        userChoice = int(input(prompt))
        if high == None:
            if userChoice >= low:
                isValid = True
                return userChoice
            else:
                print(f"Invalid input. Enter value at least {low}")
        elif low <= userChoice <= high:
            isValid = True
            return userChoice
        else:
            print(f"Invalid input. Enter value from {low} to {high}")

def main():
    watershedCities = {}
    rainfall = {}
    searchedSet = set()  # We cannot use {} to make an empty set in Python
    readData(watershedCities, rainfall)

    quit = False
    while not quit:
        userChoice = getNum("""1. Data for one watershed\n2. Watershed by average rainfall\n3. Max sensors\n4. Quit\
        \nEnter choice: """, 1,4)
        if userChoice == 1:
            promptString = ""
            i = 1
            for watershed in watershedCities:
                promptString += f"{i}. {watershed}\n"
                i += 1
            watershedNum = getNum(promptString + "Enter a number choice: ", 1, i-1)
            printOneWatershed(list(watershedCities.keys())[watershedNum-1], watershedCities, rainfall, searchedSet)
        elif userChoice == 2:
            printAvgRainfall(rainfall)
        elif userChoice == 3:
            numSensors = getNum("Enter number of sensors: ", 1)
            printMaxSensors(numSensors, rainfall)
        else:
            saveWatershedData(searchedSet)
            print("Searched watershed data saved in lab3out.txt")
            quit = True
        print()

main()