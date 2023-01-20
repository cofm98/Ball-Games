import sys
from valuesStore import *

########################################################################
########################################################################
##                                                                    ##
##         GET ITEM BLOCKS                                            ##
##                                                                    ##
########################################################################
########################################################################

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
    if(zone == None or zone > 2 or zone < 0):
        return [vals[id][6], vals[id][7], vals[id][8]]
    return vals[id][6+zone]


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
    if(zone != None):
        if(zone >= 0 and zone <= 2):
            for checkId in range(1,len(vals)):
                amount += GetPower(checkId, zone)
            return amount
    for checkId in range(1,len(vals)):
        for pwrLevels in GetPower(checkId):
            amount += float(pwrLevels)
    return amount

def GetPowerAverage(zone:int=None) -> float:
    '''Gets the average amount of power in a zone (or all 3)'''
    amount = GetPowerTotal(zone)
    amount/=len(vals)
    return amount

def GetPowerMin(zone:int=None) -> float:
    '''Gets the lowest amount of power in a zone (or all 3)'''
    amount = 0
    id = 1
    if(zone != None):
        if(zone >= 0 and zone <= 2):
            amount += GetPower(1, zone)
            for checkId in range(2, len(vals)):
                check = 0
                check += GetPower(1, zone)
                if(check < amount):
                    amount = check
                    id = checkId
            return id
    for eachZonePwr in GetPower(1):
        amount += eachZonePwr
    for checkId in range(2, len(vals)):
        check = 0
        for pwrLevels in GetPower(checkId):
            check+=pwrLevels
        if(check < amount):
            amount = check
            id = checkId
    return id

def GetPowerMax(zone:int=None) -> float:
    '''Gets the highest amount of power in a zone (or all 3)'''
    amount = 0
    id = 1
    if(zone != None):
        if(zone >= 0 and zone <= 2):
            amount += GetPower(1, zone)
            for time in range(2, len(vals)):
                check = 0
                check += GetPower(1, zone)
                if(check > amount):
                    amount = check
                    id = time
            return id
    for eachZonePwr in GetPower(1):
        amount += eachZonePwr
    for time in range(2, len(vals)):
        check = 0
        for pwrLevels in GetPower(time):
            check+=pwrLevels
        if(check > amount):
            amount = check
            id = time
    return id

def InvalidInput()->bool:
    '''When invalid input is entered. Returns back to the menu.'''
    sys.stdout.write("!! INVALID INPUT !!\n")
    return True

def Close()->bool:
    '''Closes the program'''
    sys.stdout.write("Closing...")
    return False


########################################################################
########################################################################
##                                                                    ##
##         GENERAL FUNCTIONS                                          ##
##                                                                    ##
########################################################################
########################################################################

def AddToRecords (values:list) -> list:
    vals.append(values)
    return vals
def AddToRecords (time:str, temp:float, humidity : float, windSpeed : float, generalDiffuse : float, diffuse : float, zoneOnePower : float, zoneTwoPower : float, zoneThreePower : float) -> list:
    vals.append([time, temp, humidity, windSpeed, generalDiffuse, diffuse, zoneOnePower, zoneTwoPower, zoneThreePower])
    return vals
def GetRecords () -> str:
    output : str = ""
    for eachLine in vals:
        for eachValue in eachLine:
            output += str(eachValue)+", "
        output += "\n"
    return output

def CheckMenuInput (input : str) -> int:
    try:
        input = int(input)
        if(input > 3 or input < 0):
            input = -1
    except:
        input = -1
    return input