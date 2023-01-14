##############
# frontend.py
# Charlie Morrison
# 3/01/2023
##############

import sys
import backend

def AddRecord(recordsList : list)->list:
    '''Adds a new record through user input'''
    sys.stdout.write("Adding record...\n")
    
    inp = backend.GetNewRecordInput()
    output = backend.AddToRecords(recordsList, inp)
    return output

def DisplayRecord(recordsList : list)->bool:
    '''Displays each and every record in the vals list'''
    sys.stdout.write(backend.StringifyRecords(recordsList))
    return True

def MainProgram()->bool:
    '''Main program'''
    backend.AppendRecordsFile()
    allRecords = backend.GetRecordsFile()
    usrInput = 0
    madeModification = False
    while(usrInput != 4):
        sys.stdout.write("\n1. Add a record\n2. Display all added records\n3. Save Changes\n4. Exit\nChoice: ")

        usrInput = backend.CheckMenuInput(sys.stdin.readline())

        if(usrInput == -1):
            sys.stdout.write("Invalid Input\n")
        elif(usrInput == 1):
            allRecords = AddRecord(allRecords)
            madeModification = True
        elif(usrInput == 2):
            DisplayRecord(allRecords)
        elif(usrInput == 3):
            backend.SaveRecords(allRecords)
        elif(usrInput == 4):
            if madeModification:
                if(backend.ConfirmSave()):
                    backend.SaveRecords(allRecords)
            backend.Close()
    return True


MainProgram()
