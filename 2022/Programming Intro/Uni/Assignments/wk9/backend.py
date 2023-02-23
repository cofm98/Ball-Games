########################################################################
########################################################################
##                                                                    ##
##         GET ITEM BLOCKS                                            ##
##                                                                    ##
########################################################################
########################################################################

class Electricity:
    time = str()
    temp = float()
    humidity = float()
    windSpeed = float()
    generalDiffusion = float()
    diffusion = float()
    zone1 = float()
    zone2 = float()
    zone3 = float()

    stats = {
                "total" : float(),
                "average" : float(),
                "min" : float(),
                "max" : float()
            }
    totalPowerUsage = float()
    averagePowerUsage = float()
    minPowerUsage = float()
    maxPowerUsage = float()
    def __init__ (this, time : str, temp : float, humidity : float, windSpeed : float, generalDiffusion : float, diffusion : float, zone1 : float, zone2 : float, zone3 : float):
        this.time = time
        this.temp = temp
        this.humidity = humidity
        this.windSpeed = windSpeed
        this.generalDiffusion = generalDiffusion
        this.diffusion = diffusion
        this.zone1 = zone1
        this.zone2 = zone2
        this.zone3 = zone3
        this.Calculate()
    def ToList (this) -> list:
        return [this.time, this.temp, this.humidity, this.windSpeed, this.generalDiffusion, this.diffusion, this.zone1, this.zone2, this.zone3]
    def __str__ (this) -> str:
        output : str = ""
        output +=   "Time: " + this.time
        output += "\n" + str(this.temp) + "*C @ " + str(this.humidity) + "%"
        output += "\nWind: " + str(this.windSpeed) + "KM/h"
        output += "\nDiffusion - General: " + str(this.generalDiffusion) + " Specific: " + str(this.diffusion)
        output += "\nZones - 1: " + str(this.zone1) + "kWh, 2: " + str(this.zone2) + "kWh, 3: " + str(this.zone3) + "kWh"
        output += "\n"
        return output
    def __repr__ (this) -> str:
        return "Electricity('"+this.time+"',"+str(this.temp)+","+str(this.humidity)+","+str(this.windSpeed)+","+str(this.generalDiffusion)+","+str(this.diffusion)+","+str(this.zone1)+","+str(this.zone2)+","+str(this.zone3)+")"
    def GetZones (this) -> list:
        return [this.zone1, this.zone2, this.zone3]
    def Calculate (this) -> dict:
        #Highest zone:
        tempHighestZone = this.zone1
        if(this.zone2 > tempHighestZone):
            tempHighestZone = this.zone2
        if(this.zone3 > tempHighestZone):
            tempHighestZone = this.zone3
        this.stats["max"] = tempHighestZone
        #Lowest zone:
        tempLowestZone = this.zone1
        if(this.zone2 < tempLowestZone):
            tempLowestZone = this.zone2
        if(this.zone3 < tempLowestZone):
            tempLowestZone = this.zone3
        this.stats["min"] = tempLowestZone
        #Total zones:
        this.stats["total"] = this.zone1 + this.zone2 + this.zone3
        #Average zones:
        this.stats["average"] = this.stats["total"] / 3
        return this.stats

class Power_File:
    data = list()
    url = str()
    modified = False
    def __init__ (this, file_location : str):
        this.url = file_location

    def File_Check (this) -> bool:
        check = False
        try:
            open(this.url, "x")
            check = False
        except:
            check = True
        return check
    
    def File_Load (this):
        output = list()
        file = open(this.url, "r")
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
        this.data = output
        return None
    
    def File_Save (this) -> bool:
        attempt = True
        try:
            file = open(this.url, "w")
            toFile = list()
            x = 0
            while x < len(this.data):
                record = this.data[x].ToList()
                toFile.append(",".join(str(eachVal) for eachVal in record))
                x+=1
            file.write("\n".join(toFile))
            file.close()
        except:
            attempt = False
        finally:
            this.modified = False
            return attempt
    
    def Append (this, val : Electricity):
        this.data.append(val)
        this.modified = True
    
    def GetRecordsToString (this) -> str:
        output : str = ""
        x = 0
        while x < len(this.data):
            output += "["+str(x)+"]: "+repr(this.data[x]) + "\n" + str(this.data[x])+("-"*20)+"\n"
            x+=1
        return output

class Backend_Manager:
    input_histroy = list()
    def CheckIntInput(this, input : str, min : int, max : int) -> int:
        try:
            input = int(input)
            if input > max or input < min:
                input = -1
        except:
            input = -1
        finally:
            this.input_histroy.append(input)
            return input
    
    def ConfirmYesNo (this, input : str) -> bool:
        output = None
        input = (input.strip().lower() + " ")[0]
        while output == None:
            if(input == "y"):
                output = True
            elif(input == "n"):
                output = False
        return output
    
    def OpenedFilesToString(this, current : Power_File, others : list) -> str:
        output : str = ""
        output += "-=[ " + current.url + " ]=-\n"
        x = 0
        while x < len(others):
            output += str(x + 1) + ": " + others[x].url + "\n"
            x+=1
        return output
