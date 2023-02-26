import sys

class FrontEndUI():
    def __init__(self, back_end):
        self.__backend = back_end
        pass
    #This is called by the original program. Some variables have not been declared within the class. i.e., not being 
    # a class member (self.) since they are not required for the class to function, and will not be needed in other
    # sections of this class.
    def show_ui(self):
        is_correct = False
        #This content is in order for the program to correctly load the specific file the user wants,
        # such that if they make an error there is availability for them to correct and mention
        # another file they would like to open.
        while is_correct != True:
            sys.stdout.write("File to load (.csv): ")
            self.__data_file = self.__backend.get_input(sys.stdin.readline())
            sys.stdout.write("Confirm you would like to load file: " + self.__data_file + ".csv? [Y/N]:\n")
            is_correct = self.__backend.InputAsBool(sys.stdin.readline())
        self.__data_file = self.__backend.get_load_file(self.__data_file)
        self.__backend.Check_File(self.__data_file)
        self.__data = self.__backend.Get_Data(self.__data_file)
        option = ""
        self.__modified = False
        #Looping the menu is the most efficient way to ensure the menu is always opened unless the
        # user closes it. i.e., enters "Q" into the selection menu.
        # The variables stored within this block are not imperitive to the functioning of the class as a whole
        # therefore they are not stored within "self."
        while option != "Q":
            main_menu = self.__backend.get_main_menu(self.__data_file, self.__modified)
            sys.stdout.write(main_menu)
            menu_input = sys.stdin.readline()
            option = self.__backend.get_input(menu_input, "main")
            #In case the user wants to add another record, the system iterates through each stored data value
            # this cannot be changed in any way further
            # The variables stored within this block are not imperitive to the functioning of the class as a whole
            # therefore they are not stored within "self."
            if option == "A":
                sys.stdout.write("First Name: ")
                f_name = sys.stdin.readline()
                f_name = self.__backend.get_input(f_name)
                sys.stdout.write("Last Name: ")
                l_name = sys.stdin.readline()
                l_name = self.__backend.get_input(l_name)
                happy = None
                #This code block ensures that the happy variable is entered correctly by the user
                while happy == None:
                    sys.stdout.write("Is " + f_name + " " + l_name + " happy? [Y/N]: ")
                    happy = self.__backend.InputAsBool(sys.stdin.readline())
                city_services = None
                #This code block ensures that the city services variable is entered correctly by the user
                while city_services == None:
                    sys.stdout.write("How happy are they about city services [1-5]: ")
                    city_services = self.__backend.get_score(sys.stdin.readline(), 1, 5)
                housing = None
                #This code block ensures that the housing variable is entered correctly by the user
                while housing == None:
                    sys.stdout.write("How happy are they about housing [1-5]: ")
                    housing = self.__backend.get_score(sys.stdin.readline(), 1, 5)
                schooling = None
                #This code block ensures that the schooling variable is entered correctly by the user
                while schooling == None:
                    sys.stdout.write("How happy are they about the schooling [1-5]: ")
                    schooling = self.__backend.get_score(sys.stdin.readline(), 1, 5)
                police = None
                #This code block ensures that the police variable is entered correctly by the user
                while police == None:
                    sys.stdout.write("How happy are they about the police [1-5]: ")
                    police = self.__backend.get_score(sys.stdin.readline(), 1, 5)
                street_maintenance = None
                #This code block ensures that the street maintenance variable is entered correctly by the user
                while street_maintenance == None:
                    sys.stdout.write("How happy are they about street maintenance [1-5]: ")
                    street_maintenance = self.__backend.get_score(sys.stdin.readline(), 1, 5)
                community_events = None
                #This code block ensures that the community events variable is entered correctly by the user
                while community_events == None:
                    sys.stdout.write("How happy are they about community events [1-5]: ")
                    community_events = self.__backend.get_score(sys.stdin.readline(), 1, 5)
                self.__data = self.__backend.add_record(self.__data, f_name, l_name, happy, city_services, housing, schooling, police, street_maintenance, community_events)
                self.__modified = True
            #In case the user wants to change the file, it is most effective to ensure the file hasn't been saved
            # or not, then change the file in the same method the original opening occurred when the program first
            # starts
            elif option == "C":
                if(self.__modified):
                    sys.stdout.write("Would you like to save?")
                    if self.__backend.InputAsBool(sys.stdin.readline()) == True:
                        self.__backend.Save_Data(self.__data_file, self.__data)
                is_correct = False
                while is_correct != True:
                    sys.stdout.write("File to load (.csv): ")
                    self.__data_file = sys.stdin.readline()
                    sys.stdout.write("Confirm you would like to load file: " + self.__data_file + ".csv? [Y/N]:\n")
                    is_correct = self.__backend.InputAsBool(sys.stdin.readline())
                self.__data_file = self.__backend.get_load_file(self.__data_file)
                self.__backend.Check_File(self.__data_file)
                self.__data = self.__backend.Get_Data(self.__data_file)
                self.__modified = False
            #When saving the file it is imperitive to ensure that the modified variable returns back to false 
            # otherwise data may end up incorrect
            elif option == "S":
                self.__backend.Save_Data(self.__data_file, self.__data)
                self.__modified = False
                sys.stdout.write("Saved " + self.__data_file + " successfully!\n")
            #Reading all data entries cannot be done more efficiently than this method.
            elif option == "R":
                sys.stdout.write(self.__backend.Show_Records(self.__data))
            #Prior to quitting, ensure that the file has been saved much similar to changing file.
            elif option == "Q":
                if self.__modified:
                    sys.stdout.write("Would you like to save?")
                    if self.__backend.InputAsBool(sys.stdin.readline()) == True:
                        self.__backend.Save_Data(self.__data_file, self.__data)
            else:
                sys.stdout.write("Error: Please enter an item from the menu\n")
