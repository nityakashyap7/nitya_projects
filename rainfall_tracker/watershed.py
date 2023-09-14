"""
Nitya Kashyap
Lab 4
CIS 41A
2/23/2023
Description: This program shows the cumulative rainfall in Santa Clara Valley, using
data containers, classes, objects, and exception handling
"""


class Watershed:
    # def __init__(self, name, cities=[]):
    # should NOT use default args that are mutable containers!!
    # python tries to be as efficient as possible, so each watershed object's city list will share the exact
    # same list! You'll get all the objects writing to the same list in memory and overwriting previous data!
    def __init__(self, name, cities=None):
        """
        constructor/init magic method.
        :param name: watershed name
        :param cities: list of cities in the watershed (optional)
        """
        self._name = name
        self._sensors = {}
        # revised:
        if cities:
            self._cities = cities
        else:
            self._cities = []

    def setSensors(self, sensor, rainAmt):
        """
        populates Rainfall sensor attribute
        :param sensor: string name of sensor
        :param rainAmt: float value of rainfall
        :return: none
        """
        self._sensors[sensor] = rainAmt

    def getSensors(self):
        """
        gets Rainfall sensor attribute
        :return: dictionary
        """
        return self._sensors

    def getName(self):
        """
        gets name of watershed
        :return: string
        """
        return self._name

    def getCities(self):
        """
        gets list of cities covered by the watershed
        :return: list
        """
        return self._cities

    def calcAvg(self):
        """
        computes and returns the average rainfall amount of all the sensors in the watershed
        :return: float
        """
        return sum(self._sensors.values()) / len(self._sensors)

# Unit Testing Code:
# for printOneWatershed:
# test = Watershed("West Valley", ['Sunnyvale', 'Cupertino', 'San Jose', 'Santa Clara', 'Campbell', 'Saratoga',
# 'Monte Sereno', 'Los Gatos'], {'Valley Christian': 45.75, 'West Yard': 18.82})
# test.printOneWatershed()
# print(test.calcAvg())
# print(test) #repr
# print(test.getName())
# print(test.getSensors())
# print(test.getCities())
