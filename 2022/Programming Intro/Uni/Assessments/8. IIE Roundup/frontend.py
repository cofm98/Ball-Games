import sys
import backend

#Main function. This is the primary function of the front-end.
#Firstly, we will fetch the string for which file the user would like to modify.
# We must get this first as prior to modifying any data, we will be required to
# know which data we are modifying.
#After getting the name of the file, we will check whether it exists. It is possible
# to place this backend function, checking whether the file exists, inside the 
# backend function of Get_Data. This has not been done in case of any situations
# where it would not be practicable to append the existance of a file,
# as this will open and close the file in order to check whether it is there.
# Possibly unnecessary functions to run in future applications.
#After we have checked if the file exists, the program will fetch the 
# data within the file. It will send this to a variable named "data" since this
# will be a universally used naming convention throughout the program. There is 
# no better opportunity to load this data, as soon as the menu is loaded the data
# will be accessed. Therefore, we must do it firstly.
#After fetching the data and ensuring all required files exist, we will be required
# to set up all local variables which will not change during each phase of the
# program. I.e., when the menu is returned to:
#The first variable is the 'option' variable. This states the option which the
# menu is currently handling. This must be declared prior to its initial usage;
# when it is checked to ensure the program has not been requested to be closed.
#The next variable which must be declared is the 'modified' variable. Essentially,
# this variable is used in order to ensure the data is being saved only when necessary.
def main():
    file = backend.get_load_file()
    backend.Check_File(file)
    data = backend.Get_Data(file)
    option = ""
    modified = False
    #Within the while loop for the main function, there are many if checks to ensure the menu is going to
    # the correct location. This is an element of front-end programming, where we will send the menu
    # to the right place.
    #This has been a while loop since we are ensuring that the menu has not been quit, when the option
    # is equal to 'Q', it will be once the menu has been quit from the user. It is no longer necessary
    # to continue to display the menu. This may be possible to place into a variable such as while 'running',
    # as 'running' is a boolean variable. However, if we re-use the 'option' variable we have
    # reduced code-redundancy, and re-used variables. The 'while running' would only be useful if there
    # are other times which the user could quit the program other than the main menu.
    #Within this loop, we firstly declare a variable for 'main_menu', which we will send through
    # the file destination, i.e., data.csv for example, and the boolean value whether it has been
    # modified, since the menu differs slightly when it has been modified. We fetch it from a function
    # on the back end, just in case there are any modifications to the menu and we do not need to see a
    # large wall of text, making the code look neater and ensuring that all values are being appropriately
    # assigned in any manner that may be complex.
    #We then write the main menu, there is no other way to go around this. We may be able to use the flush function;
    # sys.stdout.flush(), however since python is already doing this for us it is not currently necessary.
    #After writing the menu it is most accurate to fetch the user's input and append the results in order
    # to send the user to the next correct menu. This could not be modified, however the internal section is available
    # for growth, making this project further scaleable.
    while option != "Q":
        main_menu = backend.get_main_menu(file, modified)
        sys.stdout.write(main_menu)
        option = backend.get_input("main")
        #Running through the options alphabetically; the first option is 'A', to add more data. We call
        # the backend function to add a record and inform the system that the save data has now been modified.
        # This will be able to be used when the above while loop is re-called, and it will send it through to
        # modify the outcome of the menu.
        #This may not be the most effective use of code, however within the bounds of Python and this project it
        # remains suitable. Within a solely object-orientated paradigm, we would rather have the data and modified
        # factor saved within a single instance of an object, and utilise the data within this object to append
        # additional data relating to the code. For instance, we may have the availability of recent changes so
        # the user is capable of undoing, and we would also have the availability of modifiying multiple files at once
        # without a large amount of re-coding the system. However, within the bounds of this project, it is not
        # necessary to include such in-depth details.
        if(option == "A"):
            data = backend.add_record(data)
            modified = True
        #Continuing in alphabetical order, we check the user's input to equal 'C', to change the file being used.
        # This has been mentioned above, for the add record check, if we had the program as a class and instance,
        # we would be capable of not closing the current file, but just opening a new file without losing data.
        # However, before we change the file the program will always ask 'would you like to save', this will ensure
        # the user will not lose any data by accident, or save data which he/she did not intent to save.
        # After we have saved the data, the program follows a pattern which is consistent with starting the program.
        # This process is talked about further within the description of the function definition statements.
        elif(option == "C"):
            #If the user would like to save, then the data must be saved - and if the program saves the data, it
            # must declare that the file is no longer modified, as the data within the program is now the exact same
            # within the file. Closing and opening the program will result in the same data within. There is no further
            # effecient way to conduct this operation within the bounds of this program and criteria.
            if backend.confirm("Would you like to save?"):
                backend.Save_Data(file, data)
                modified = False
            file = backend.get_load_file()
            backend.Check_File(file)
            data = backend.Get_Data(file)
        #If the user decides to save the file, we will follow the exact same procedure as mentioned above within the
        # change file statement. The program, however, will not ensure whether you would like to save, as you have
        # selected the option intentionally. This code is a near-replication of the above code in the saving process.
        # Consistency is the method in which a user becomes quickly familiar with a program, utilising repetition through
        #-out the program ensures that the user will be more aware of what they are doing, and not be making accidents
        # within the data.
        elif(option == "S"):
            backend.Save_Data(file, data)
            modified = False
            sys.stdout.write("Saved " + file + " successfully!\n")
        #If the user chooses to see the records, show the records. The only further efficiency of this part of the
        # program would be to have a user input stating 'Press enter to continue', so that the menu does not overlap
        # itself and possibly hides the data above.
        elif(option == "R"):
            backend.Show_Records(data)
        #If the user quits, check whether the file has been modified. There is no further effient method in order to
        # conduct the desired outcomes. If the confirm statement was here instead, then the user have just opened
        # the file and looked at one part of data, then closed the system. They would feel anxious if they were asked
        # to save before quitting, because they would feel they have modified some data incidentally.
        # Therefore, to ensure user comfort, it is appropriate to check whether the file has been modified prior to
        # asking for confirmation to saving the file.
        elif(option == "Q"):
            if(modified):
                if backend.confirm("Would you like to save before quitting?"):
                    backend.Save_Data(file, data)
        #The final option is in the event a menu item has not been selected correctly. This is built in within the 
        # backend function, that it will return "EI", representing "Error:Input". This is not a common practice through
        #-out the industry, since it may cause confusion amongst many developers on the same project. However, this is
        # a solo developed project, therefore it is practical to use personalised error messages in case it may be required
        # in a more complex application of user input.
        else:
            sys.stdout.write("Error: Please enter an item from the menu\n")

main()
