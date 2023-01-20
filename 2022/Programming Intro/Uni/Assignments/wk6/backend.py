import sys

########################################################################
########################################################################
##                                                                    ##
##         GET ITEM BLOCKS                                            ##
##                                                                    ##
########################################################################
########################################################################

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
        output.append(valueSet)
    file.close()
    return output

def SaveRecords (input) -> None:
    file = open("values.csv", "w")
    toFile = list()
    for eachLine in input:
        toFile.append(",".join(str(eachVal) for eachVal in eachLine))
    file.write("\n".join(toFile))
    file.close()
    return

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
    for eachLine in source:
        for eachValue in eachLine:
            output += str(eachValue)+", "
        output += "\n"
    return output

def CheckMenuInput (input : str) -> int:
    try:
        input = int(input)
        if input > 3 or input < 0:
            input = -1
    except:
        input = -1
    return input

def GetNewRecordInput () -> list:
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
    
    return [time, temp, humd, wnds, gend, diff, zon1, zon2, zon3]