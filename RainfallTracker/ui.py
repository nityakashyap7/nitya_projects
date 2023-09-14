"""
Nitya Kashyap
Lab 4
CIS 41A
2/23/2023
Description: This program shows the cumulative rainfall in Santa Clara Valley, using
data containers, classes, objects, and exception handling
"""

from rainfall import Rainfall
from watershed import Watershed


class UI:
    def __init__(self):
        """
        constructor/init magic method.
        accepts no parameters (except self)
        """
        # supposed to raise IOError here:
        try:
            self._rainfallObj = Rainfall()
        except IOError:
            print(self._rainfallObj)
    def __getNum(self, prompt, low, high=None): # helper method, thus private
        """
        Prompt the user until a valid input is obtained.
        :param prompt: string that the user should be prompted with
        :param low: the lowest valid int number
        :param high: the highest valid int number (optional parameter)
        :return: validated user choice as an int
        """
        isValid = False
        while not isValid:
            try:
                userChoice = int(input(prompt))
                if high == None:
                    if userChoice >= low:
                        isValid = True
                        return userChoice
                    else:
                        raise Exception(f"Invalid input. Enter value at least {low}\n")
                elif low <= userChoice <= high:
                    isValid = True
                    return userChoice
                else:
                    raise Exception(f"Invalid input. Enter value from {low} to {high}\n")
            except ValueError:
                print("Invalid input. Choice is a positive number\n")
            except Exception as exceptionObj:
                print(exceptionObj)

    def printOneWatershed(self):
        """
        Prints rainfall amount for each sensor in selected watershed
        :return: none
        """
        watersheds = list(self._rainfallObj.getAllWatersheds())
        promptString = ""
        i = 1
        for watershed in watersheds:
            promptString += f"{i}. {watershed}\n"
            i += 1
        promptString += "Enter a number choice: "
        watershedNum = self.__getNum(promptString, 1, i-1)
        watershedName = watersheds[watershedNum - 1]
        watershedObj = self._rainfallObj.getWatershedObj(watershedName)
        if len(watershedObj.getCities()) > 0:
            print(f"Sensors for {watershedName} watershed, which includes:")
            print(', '.join(watershedObj.getCities()))
        else:
            print(f"Sensors for {watershedName} watershed (no city information):")
        sensors = watershedObj.getSensors()
        for sensor in sensors:
            print(f"{sensor:35s}{sensors[sensor]:>5.2f}")  # right justified

    def printAvgRainfall(self):
        """
        Prints average rainfall (sorted from highest to lowest) of the watersheds
        :return: none
        """
        avgs = self._rainfallObj.calcAvgRainfall()
        print(f"Watershed{' ' * 10}Inches")
        for average in sorted(avgs, reverse=True):
            print(f"{avgs[average]:19s}{average:>5.2f}")

    def printMaxSensors(self):
        """
        Prints the top N sensors that have recorded the most rainfall
        :return: none
        """
        N = self.__getNum("Enter number of sensors: ", 1)
        sensors = self._rainfallObj.getAllSensors()
        if N > len(sensors):
            N = len(sensors)
        for rainfallAmt in (sorted(sensors, reverse=True))[:N]:  # default start @ 0
            print(f"{sensors[rainfallAmt]}: {rainfallAmt}")

    def run(self):
        """
        displays menu, does appropriate function call for chosen menu option, repeats until user quits
        :return: none
        """
        quit = False
        while not quit:
            choiceNum = self.__getNum("1. Data for one watershed\n2. Watershed by average rainfall\n3. Max sensors\n"
                                      "4. Quit\nEnter choice: ", 1,4)
            if choiceNum ==1:
                self.printOneWatershed()
            elif choiceNum == 2:
                self.printAvgRainfall()
            elif choiceNum == 3:
                self.printMaxSensors()
            elif choiceNum == 4:
                quit = True
            print()


obj = UI()
obj.run()


# Unit Testing Code:
# ui.printOneWatershed()
# ui.printAvgRainfall()
# ui.printMaxSensors(50)
