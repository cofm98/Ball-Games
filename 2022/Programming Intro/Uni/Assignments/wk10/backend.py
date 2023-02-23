class Electricity:
    #Public
    time : str
    temp : float
    humidity : float
    windSpeed : float
    generalDiffusion : float
    diffusion : float
    zone1 : float
    zone2 : float
    zone3 : float
    totalPowerUsage : float
    averagePowerUsage : float
    minPowerUsage : float
    maxPowerUsage : float
    #Private
    __stats : dict = {
                "total" : float(),
                "average" : float(),
                "min" : float(),
                "max" : float()
            }
    @property
    def stats(self) -> dict:
        return self.__stats
    @stats.setter
    def stats(self, stats : dict):
        self.__stats = stats
    def __str__ (self) -> str:
        output : str = ""
        output +=   "Time: " + self.time
        output += "\n" + str(self.temp) + "*C @ " + str(self.humidity) + "%"
        output += "\nWind: " + str(self.windSpeed) + "KM/h"
        output += "\nDiffusion - General: " + str(self.generalDiffusion) + " Specific: " + str(self.diffusion)
        output += "\nZones - 1: " + str(self.zone1) + "kWh, 2: " + str(self.zone2) + "kWh, 3: " + str(self.zone3) + "kWh"
        output += "\n"
        return output
    def __repr__ (self) -> str:
        return "Electricity('"+self.time+"',"+str(self.temp)+","+str(self.humidity)+","+str(self.windSpeed)+","+str(self.generalDiffusion)+","+str(self.diffusion)+","+str(self.zone1)+","+str(self.zone2)+","+str(self.zone3)+")"
    #Functions
    def __init__ (self, time : str, temp : float, humidity : float, windSpeed : float, generalDiffusion : float, diffusion : float, zone1 : float, zone2 : float, zone3 : float):
        self.time = time
        self.temp = temp
        self.humidity = humidity
        self.windSpeed = windSpeed
        self.generalDiffusion = generalDiffusion
        self.diffusion = diffusion
        self.zone1 = zone1
        self.zone2 = zone2
        self.zone3 = zone3
        self.__Calculate()
    def ToList (self) -> list:
        return [self.time, self.temp, self.humidity, self.windSpeed, self.generalDiffusion, self.diffusion, self.zone1, self.zone2, self.zone3]
    def GetZones (self) -> list:
        return [self.zone1, self.zone2, self.zone3]
    def __Calculate (self) -> dict:
        #Highest zone:
        tempHighestZone = self.zone1
        if(self.zone2 > tempHighestZone):
            tempHighestZone = self.zone2
        if(self.zone3 > tempHighestZone):
            tempHighestZone = self.zone3
        self.__stats["max"] = tempHighestZone
        #Lowest zone:
        tempLowestZone = self.zone1
        if(self.zone2 < tempLowestZone):
            tempLowestZone = self.zone2
        if(self.zone3 < tempLowestZone):
            tempLowestZone = self.zone3
        self.__stats["min"] = tempLowestZone
        #Total zones:
        self.__stats["total"] = self.zone1 + self.zone2 + self.zone3
        #Average zones:
        self.__stats["average"] = self.__stats["total"] / 3
        return self.__stats

class Power_File:
    #Private
    __data : list
    __url : str
    __modified = False
    @property
    def data(self):
        return self.__data
    @property
    def url(self):
        return self.__url
    @property
    def isModified(self):
        return self.__modified
    def __init__ (self, file_location : str):
        self.__url = file_location
    #Functions
    def File_Check (self) -> bool:
        check = False
        try:
            open(self.__url, "x")
            check = False
        except:
            check = True
        return check
    def File_Load (self):
        output = list()
        file = open(self.__url, "r")
        allLines = file.readlines()
        for eachLine in allLines:
            valueSet = eachLine.strip().split(",")
            output.append(Electricity(valueSet[0],
                                            float(valueSet[1]),
                                            float(valueSet[2]),
                                            float(valueSet[3]),
                                            float(valueSet[4]),
                                            float(valueSet[5]),
                                            float(valueSet[6]),
                                            float(valueSet[7]),
                                            float(valueSet[8])))
        file.close()
        self.__data = output
        return None
    def File_Save (self) -> bool:
        attempt = True
        try:
            file = open(self.__url, "w")
            toFile = list()
            x = 0
            while x < len(self.__data):
                record = self.__data[x].ToList()
                toFile.append(",".join(str(eachVal) for eachVal in record))
                x+=1
            file.write("\n".join(toFile))
            file.close()
        except:
            attempt = False
        finally:
            self.__modified = False
            return attempt
    def Append (self, val : Electricity):
        self.__data.append(val)
        self.__modified = True
    def GetRecordsToString (self) -> str:
        output : str = ""
        x = 0
        while x < len(self.__data):
            output += "["+str(x)+"]: "+repr(self.__data[x]) + "\n" + str(self.__data[x])+("-"*20)+"\n"
            x+=1
        return output

class Backend_Manager:
    #Private
    __input_histroy : list = list()
    #Functions
    def CheckIntInput(self, input : str, min : int, max : int) -> int:
        try:
            input = int(input)
            if input > max or input < min:
                input = -1
        except:
            input = -1
        finally:
            self.__input_histroy.append(input)
            return input
    def ConfirmYesNo (self, input : str) -> bool:
        output = None
        input = (input.strip().lower() + " ")[0]
        while output == None:
            if(input == "y"):
                output = True
            elif(input == "n"):
                output = False
        self.__input_histroy.append(input)
        return output
    def OpenedFilesToString(self, current : Power_File, others : list) -> str:
        output : str = ""
        output += "-=[ Current: " + current.url + " ]=-\n"
        x : int = 0
        while x < len(others):
            output += str(x + 1) + ": " + others[x].url
            if(others[x].isModified):
                output+="*"
            output += "\n"
            x+=1
        return output