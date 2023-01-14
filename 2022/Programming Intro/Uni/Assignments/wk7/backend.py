import sys

########################################################################
########################################################################
##                                                                    ##
##         GET ITEM BLOCKS                                            ##
##                                                                    ##
########################################################################
########################################################################

class ElectricityRecord:
    time = str()
    temp = float()
    humidity = float()
    windSpeed = float()
    generalDiffusion = float()
    diffusion = float()
    zone1 = float()
    zone2 = float()
    zone3 = float()
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
    def ToList (this) -> list:
        return [this.time, this.temp, this.humidity, this.windSpeed, this.generalDiffusion, this.diffusion, this.zone1, this.zone2, this.zone3]
   #[time, temp, humd, wnds, gend, diff, zon1, zon2, zon3]

def AppendRecordsFile () -> None:
    try:
        open("values.csv", "x")
        sys.stdout.write("Created Saves Successfully...\n")
    except:
        sys.stdout.write("Loaded Successfully...\n")
    return

def GetRecordsFile () -> list:
    output = list()
    file = open("values.csv", "r")
    allLines = file.readlines()
    for eachLine in allLines:
        valueSet = eachLine.strip().split(",")
        output.append(ElectricityRecord(valueSet[0],
                                        float(valueSet[1]),
                                        float(valueSet[2]),
                                        float(valueSet[3]),
                                        float(valueSet[4]),
                                        float(valueSet[5]),
                                        float(valueSet[6]),
                                        float(valueSet[7]),
                                        float(valueSet[8])))
    file.close()
    return output

def SaveRecords (input) -> None:
    file = open("values.csv", "w")
    toFile = list()
    for eachLine in input:
        record = eachLine.ToList()
        toFile.append(",".join(str(eachVal) for eachVal in record))
    file.write("\n".join(toFile))
    file.close()
    return

def ConfirmSave (input) -> bool:
    sys.stdout.write("Changes have been made, would you like to save?\n[Y/N]: ")
    saved = None
    while(saved == None):
        if(sys.stdin.readline().strip()[0] == "N"):
            saved = False
        elif(sys.stdin.readline().strip()[0] == "Y"):
            saved = True
    return saved
    

def GetList (id:int) -> list:
    '''Get the information list of a selected ID'''
    return vals[id]
def GetTime (id:int) -> str:
    '''Get the time of a selected ID'''
    return vals[id][0]
def GetTemp (id:int) -> float:
    '''Get the temperature of a selected ID'''
    return vals[id][1]
def GetHumidity (id:int) -> float:
    '''Get the humidity of a selected ID'''
    return vals[id][2]
def GetWindSpeed (id:int) -> float:
    '''Get the wind speed of a selected ID'''
    return vals[id][3]
def GetGenDiff (id:int) -> float:
    '''Get the general diffusion flow of a selected ID'''
    return vals[id][4]
def GetDiff (id:int) -> float:
    '''Get the diffusion flow of a selected ID'''
    return vals[id][5]
def GetPowerCulminated (id) -> float:
    return vals[id][6]+vals[id][7]+vals[id][8]
def GetPower (id:int, zone:int=None) -> float:
    '''Get power or power usage levels of a selected ID
    'zone' from 0 -> 2 or None/blank for all 3'''
    output = None
    if zone == None or zone > 2 or zone < 0:
        output = [vals[id][6], vals[id][7], vals[id][8]]
    else:
        output = vals[id][6+zone]
    return output


########################################################################
########################################################################
##                                                                    ##
##         GET FUNCTION BLOCKS                                        ##
##                                                                    ##
########################################################################
########################################################################


def GetPowerTotal(zone:int=None) -> float:
    '''Gets the total amount of power in a zone (or all 3)'''
    amount = 0
    if zone != None and zone >= 0 and zone <= 2:
        for checkId in range(1,len(vals)):
            amount += GetPower(checkId, zone)
    else:
        for checkId in range(1,len(vals)):
            for pwrLevels in GetPower(checkId):
                amount += float(pwrLevels)
    return amount

def GetPowerAverage(zone:int=None) -> float:
    '''Gets the average amount of power in a zone (or all 3)'''
    amount = GetPowerTotal(zone)
    amount /= len(vals)
    return amount

def GetPowerMin(zone:int=None) -> float:
    '''Gets the lowest amount of power in a zone (or all 3)'''
    amount, id = 0
    if zone != None and zone >= 0 and zone <= 2:
        amount += GetPower(1, zone)
        for checkId in range(2, len(vals)):
            check = 0
            check += GetPower(1, zone)
            if check < amount:
                amount = check
                id = checkId
    else:
        for eachZonePwr in GetPower(1):
            amount += eachZonePwr
        for checkId in range(2, len(vals)):
            check = 0
            for pwrLevels in GetPower(checkId):
                check += pwrLevels
            if check < amount:
                amount = check
                id = checkId
    return id

def GetPowerMax(zone:int=None) -> float:
    '''Gets the highest amount of power in a zone (or all 3)'''
    amount, id = 0
    if zone != None and zone >= 0 and zone <= 2:
        amount += GetPower(1, zone)
        for time in range(2, len(vals)):
            check = 0
            check += GetPower(1, zone)
            if check > amount:
                amount = check
                id = time
    else:
        for eachZonePwr in GetPower(1):
            amount += eachZonePwr
        for time in range(2, len(vals)):
            check = 0
            for pwrLevels in GetPower(time):
                check += pwrLevels
            if check > amount:
                amount = check
                id = time
    return id

def InvalidInput()->None:
    '''When invalid input is entered. Returns back to the menu.'''
    sys.stdout.write("!! INVALID INPUT !!\n")
    return

def Close()->None:
    '''Closes the program'''
    sys.stdout.write("Closing...")
    return


########################################################################
########################################################################
##                                                                    ##
##         GENERAL FUNCTIONS                                          ##
##                                                                    ##
########################################################################
########################################################################

def AddToRecords (time:str, temp:float, humidity : float, windSpeed : float, generalDiffuse : float, diffuse : float, zoneOnePower : float, zoneTwoPower : float, zoneThreePower : float) -> list:
    vals.append([time, temp, humidity, windSpeed, generalDiffuse, diffuse, zoneOnePower, zoneTwoPower, zoneThreePower])
    return vals

def AddToRecords (source : list, values:list) -> list:
    source.append(values)
    return source

def StringifyRecords (source : list) -> str:
    output : str = ""
    for eachRecord in source:
        output += "\n\nT: " + eachRecord.time + "\n" + str(eachRecord.temp) + "*C @ " + str(eachRecord.humidity) + "%: " + str(eachRecord.windSpeed) + "km/h gdiff: " + str(eachRecord.generalDiffusion) + " diff: " + str(eachRecord.diffusion) + "\n1: " + str(eachRecord.zone1) + "kWh, 2: " + str(eachRecord.zone2) + "kWh, 3: " + str(eachRecord.zone3) + "kWh"
    return output

def CheckMenuInput (input : str) -> int:
    try:
        input = int(input)
        if input > 4 or input < 0:
            input = -1
    except:
        input = -1
    return input

def GetNewRecordInput () -> ElectricityRecord:
    try:
        sys.stdout.write("Time recorded (DD/MM/YYYY HH:MM): ")
        time=sys.stdin.readline().strip()
        sys.stdout.write("Temperature (C): ")
        temp=float(sys.stdin.readline())
        sys.stdout.write("Humidity (%): ")
        humd=float(sys.stdin.readline())
        sys.stdout.write("Wind Speed (km/h): ")
        wnds=float(sys.stdin.readline())
        sys.stdout.write("General Diffusion: ")
        gend=float(sys.stdin.readline())
        sys.stdout.write("Diffusion: ")
        diff=float(sys.stdin.readline())
        sys.stdout.write("Zone 1 Power Consumption (kW): ")
        zon1=float(sys.stdin.readline())
        sys.stdout.write("Zone 2 Power Consumption (kW): ")
        zon2=float(sys.stdin.readline())
        sys.stdout.write("Zone 3 Power Consumption (kW): ")
        zon3=float(sys.stdin.readline())
    except:
        return InvalidInput()

    sys.stdout.write("\nAdded record:\nTime: "
    +time+"\nTemperature: "
    +str(temp)+"\nHumidity: "
    +str(humd)+"\nWind Speed: "
    +str(wnds)+"\nGeneral Diffusion: "
    +str(gend)+"\nDiffusion: "
    +str(diff)+"\nZone 1 Power Consumption: "
    +str(zon1)+"kW\nZone 2 Power Consumption: "
    +str(zon2)+"kW\nZone 3 Power Consumption: "
    +str(zon3)+"kW")
    
    return ElectricityRecord(time, temp, humd, wnds, gend, diff, zon1, zon2, zon3)