"""
Nitya Kashyap
Lab 4
CIS 41A
2/23/2023
Description: This program shows the cumulative rainfall in Santa Clara Valley, using
data containers, classes, objects, and exception handling
"""

import csv
from watershed import Watershed


class Rainfall:
    # class attributes
    TXT_INPUT = "city.txt"
    CSV_INPUT = "rainfallEC.csv"

    def __init__(self):
        """
        constructor/init magic method.
        accepts no parameters (except self)
        """
        self._rainfallDict = {}
        try:
            with open(Rainfall.TXT_INPUT) as infile:
                for line in infile:
                    line = line.rstrip()  # rid "\n" at the end
                    lineList = line.split(sep=": ")  # splits watershed from cities
                    watershed = lineList[0]
                    cityList = lineList[1].split(", ")  # splits the cities into elements of another list
                    self._rainfallDict[watershed] = Watershed(watershed, cityList)  # create + store watershed object

            with open(Rainfall.CSV_INPUT) as infile:
                reader = csv.reader(infile)
                for line in reader:
                    watershed = line[2]
                    sensor = line[0]
                    rainAmt = float(line[1])
                    try:
                        watershedObj = self._rainfallDict[watershed]
                    except KeyError:
                        watershedObj = self._rainfallDict[watershed] = Watershed(watershed)
                    watershedObj.setSensors(sensor, rainAmt)
        except IOError as exceptionObj:
            print(exceptionObj)
            raise SystemExit("Please check input files and try again")

    def __repr__(self):
        """
        used for print
        :return: string representation of the object
        """
        return f"Read in data for {', '.join(self._rainfallDict.keys())} watersheds"

    def calcAvgRainfall(self):
        """
        compiles average rainfall of the watersheds
        :return: dictionary of unsorted averages (key = average, value = watershed name)
        """
        averages = {}
        # calculate averages
        for watershed in self._rainfallDict:
            averages[watershed] = self._rainfallDict[watershed].calcAvg()

        flippedDict = dict(zip(averages.values(), averages.keys()))
        return flippedDict

    def getAllSensors(self):
        """
        compiles all sensor data into one dictionary
        :return: dictionary
        """
        sensorDict = {}
        for watershed in self._rainfallDict:
            sensorDict.update(self._rainfallDict[watershed].getSensors())

        # assume that the rainfall data numbers are unique
        flippedDict = dict(zip(sensorDict.values(), sensorDict.keys()))
        return flippedDict

    def getAllWatersheds(self):
        """
        get names of all watersheds
        :return: names of all the watersheds in the rainfall dictionary attribute
        """
        return self._rainfallDict.keys()

    def getWatershedObj(self, watershedName):
        """
        get the watershed object's details, given its name
        :param watershedName: name of selected watershed, for which info is needed
        :return: Watershed object
        """
        return self._rainfallDict[watershedName]


# Unit Testing Code:
# rainfall = Rainfall()
# print(rainfall.calcAvgRainfall())
# print(rainfall.getAllSensors())
# print(rainfall.getWatershedObj("Pajaro"))
# print(rainfall.getAllWatersheds())

