##############
# frontend.py
# Charlie Morrison
# 3/01/2023
##############

import sys
import backend

class FrontEnd_Manager:

    backend_manager : backend.Backend_Manager = None

    def __init__(this):
        this.backend_manager = backend.Backend_Manager()
        this.MainProgram()

    def AddRecord(this, obj : backend.Power_File)->list:
        '''Adds a new record through user input'''
        sys.stdout.write("Adding record...\n")

        validInputs = False
        while validInputs == False:
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
                validInputs = True
            except:
                sys.stdout.write()

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

        output = obj.Append(backend.Electricity(time, temp, humd, wnds, gend, diff, zon1, zon2, zon3))
        return output

    def ConfirmSave (this) -> bool:
        sys.stdout.write("Changes have been made, would you like to save?\n[Y/N]: ")
        inp = this.backend_manager.ConfirmYesNo(sys.stdin.readline())
        return inp

    def CheckAnyModified (this, checks : list) -> bool:
        output = -1
        x = 0
        while x < len(checks):
            if(checks[x].modified):
                output = x
        return output
        

    def MainProgram(this)->bool:
        '''Main program'''
        currentFile = backend.Power_File("values.csv")
        currentFile.File_Check()
        currentFile.File_Load()
        otherFiles : list = [currentFile]
        usrInput = 0
        while(usrInput != 6):
            sys.stdout.write("\n["+currentFile.url + "]\n1. Add a record\n2. Display all added records\n3. Save Changes\n4. Opened Files\n5. Open New\n6. Exit\nChoice: ")

            usrInput = this.backend_manager.CheckIntInput(sys.stdin.readline(), 1, 6)

            if(usrInput == -1):
                sys.stdout.write("Invalid Input\n")
            elif(usrInput == 1):
                this.AddRecord(currentFile)
            elif(usrInput == 2):
                sys.stdout.write(currentFile.GetRecordsToString())
            elif(usrInput == 3):
                if(currentFile.File_Save()):
                    sys.stdout.write("File Successfully Saved\n")
                else:
                    sys.stdout.write("File Unsuccessfully Saved\n")
            elif(usrInput == 4):
                if(len(otherFiles) > 1):
                    sys.stdout.write(this.backend_manager.OpenedFilesToString(currentFile, otherFiles))
                    usrInput = this.backend_manager.CheckIntInput(sys.stdin.readline(), 1, len(otherFiles))
                    currentFile = otherFiles[usrInput - 1]
                else:
                    sys.stdout.write("No other files are opened.\n")
            elif(usrInput == 5):
                sys.stdout.write("File to open (.csv): ")
                newFileURL = sys.stdin.readline().strip() + ".csv"
                currentFile = backend.Power_File(newFileURL)
                currentFile.File_Check()
                currentFile.File_Load()
                otherFiles.append(currentFile)
            elif(usrInput == 6):
                if currentFile.modified:
                    if(this.ConfirmSave()):
                        currentFile.File_Save()
                sys.stdout.write("Shutting Down")
        return True

program = FrontEnd_Manager()
