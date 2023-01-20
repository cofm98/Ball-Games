##############
# frontend.py
# Charlie Morrison
# 3/01/2023
##############

import sys
import backend
from valuesStore import *

def AddRecord()->bool:
    '''Adds a new record through user input'''
    sys.stdout.write("Adding record...\n")
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
        return backend.InvalidInput()
    
    backend.AddToRecords(time,temp,humd,wnds,gend,diff,zon1,zon2,zon3)

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
    return True

def DisplayRecord()->bool:
    '''Displays each and every record in the vals list'''
    sys.stdout.write(backend.GetRecords())
    return True

def MainProgram()->bool:
    '''Main program'''
    sys.stdout.write("\n1. Add a record\n2. Display all added records\n3. Exit\nChoice: ")

    usrInput = backend.CheckMenuInput(sys.stdin.readline())

    if(usrInput == -1):
        sys.stdout.write("Invalid Input\n")
    elif(usrInput == 1):
        AddRecord()
    elif(usrInput == 2):
        DisplayRecord()
    elif(usrInput == 3):
        return backend.Close()
    
    return True



running = True #Is your program running?
while running:
    running = MainProgram()
