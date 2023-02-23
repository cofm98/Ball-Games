##############
# frontend.py
# Charlie Morrison
##############

import sys
import backend

class FrontEnd_Manager:

    def __init__(self):
        self.__backend_manager = backend.Backend_Manager()
        self.__main()

    def __AddRecord(self, obj : backend.Power_File)->list:
        '''Adds a new record through user input'''
        sys.stdout.write("Adding record...\n")

        valid_input = False
        while valid_input == False:
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
                valid_input = True
            except:
                sys.stdout.write("Invalid input..Please try again\n")

        sys.stdout.write("\nAdded record:\nTime: "
        +time+"\nTemperature: "
        +str(temp)+"\nHumidity: "
        +str(humd)+"\nWind Speed: "
        +str(wnds)+"\nGeneral Diffusion: "
        +str(gend)+"\nDiffusion: "
        +str(diff)+"\nZone 1 Power Consumption: "
        +str(zon1)+"kW\nZone 2 Power Consumption: "
        +str(zon2)+"kW\nZone 3 Power Consumption: "
        +str(zon3)+"kW\n")

        output = obj.Append(backend.Electricity(time, temp, humd, wnds, gend, diff, zon1, zon2, zon3))
        return output

    def __ConfirmSave (self) -> bool:
        sys.stdout.write("Changes have been made, would you like to save?\n[Y/N]: ")
        inp = self.__backend_manager.ConfirmYesNo(sys.stdin.readline())
        return inp

    def __CheckAnyModified (self, checks : list) -> bool:
        output = -1
        x = 0
        while x < len(checks):
            if(checks[x].isModified):
                output = True
                break
            x+=1
        return output
    def __SaveAll (self, to_save : list) -> bool:
        output : bool = True
        x : int = 0
        while x < len(to_save):
            if(to_save[x].File_Save() == False):
                output = False
                break
            x+=1
        return output

    def __main (self)->bool:
        '''Main program'''
        currentFile = backend.Power_File("values.csv")
        currentFile.File_Check()
        currentFile.File_Load()
        other_files : list = [currentFile]
        user_input = 0
        while(user_input != 6):
            main_menu = "\n[" + currentFile.url + "]"
            if(currentFile.isModified == True):
                main_menu += "*"
            main_menu += "\n1. Add a record\n2. Display all added records\n3. Save Changes\n4. Opened Files\n5. Open New\n6. Exit\nChoice: "
            sys.stdout.write(main_menu)

            user_input = self.__backend_manager.CheckIntInput(sys.stdin.readline(), 1, 6)

            if(user_input == -1):
                sys.stdout.write("Invalid Input\n")
            elif(user_input == 1):
                self.__AddRecord(currentFile)
            elif(user_input == 2):
                sys.stdout.write(currentFile.GetRecordsToString())
            elif(user_input == 3):
                if(currentFile.File_Save()):
                    sys.stdout.write("File Successfully Saved\n")
                else:
                    sys.stdout.write("File Unsuccessfully Saved\n")
            elif(user_input == 4):
                if(len(other_files) > 1):
                    sys.stdout.write(self.__backend_manager.OpenedFilesToString(currentFile, other_files))
                    sys.stdout.write("Select Working File: ")
                    user_input = self.__backend_manager.CheckIntInput(sys.stdin.readline(), 1, len(other_files))
                    currentFile = other_files[user_input - 1]
                else:
                    sys.stdout.write("No other files are opened.\n")
            elif(user_input == 5):
                sys.stdout.write("File to open (.csv): ")
                newFileURL = sys.stdin.readline().strip() + ".csv"
                currentFile = backend.Power_File(newFileURL)
                currentFile.File_Check()
                currentFile.File_Load()
                other_files.append(currentFile)
            elif(user_input == 6):
                saved = None
                if self.__CheckAnyModified(other_files):
                    if(self.__ConfirmSave()):
                        saved = self.__SaveAll(other_files)
                if saved == True:
                    sys.stdout.write("Shutting Down")
                else:
                    sys.stdout.write("Save Failed. Would you like to shutdown anyway?\n[Y/N]: ")
                    input = self.__backend_manager.ConfirmYesNo(sys.stdin.readline())
                    if input == True:
                        sys.stdout.write("Shutting Down")
                    else:
                        sys.stdout.write("Returning to Main Menu...\n")
                        user_input = 0

        return True

program = FrontEnd_Manager()
