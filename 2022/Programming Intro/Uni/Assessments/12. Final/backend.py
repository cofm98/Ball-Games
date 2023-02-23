import sys

#The best way to declare this class is to ensure all data is being saved appropriately with certain naming conventions.
# other than that, there are no arithmetic or analysis of data within the declaration. Therefore, there is no further improvements
# of this class other than using dictionaries, enums, structs, or other datatypes which are not assessable within this criteria.
class Happiness:
    name = ""
    last_name = ""
    happy = False
    happy_city_services = 0
    happy_housing = 0
    happy_schooling = 0
    happy_police = 0
    happy_street_maintenance = 0
    happy_community_events = 0
    #In order to correctly assign all data to the object, it is most effective to do it through a function in order to reduce any data-loss through accidentally not
    # declaring a particular element. The only improvement on this may be that the variables could be in order of above, just to improve readability. Other than that, there are no functionl
    # changes which are appriopriate to an initialise function.
    def __init__ (self, name : str, last_name : str, happy : bool, happy_city_services : int, happy_housing : int, happy_schooling : int, happy_police : int, happy_street_maintenance : int, happy_community_events : int):
        self.happy = happy
        self.name = name
        self.last_name = last_name
        self.happy = happy
        self.happy_city_services = happy_city_services
        self.happy_housing = happy_housing
        self.happy_schooling = happy_schooling
        self.happy_police = happy_police
        self.happy_street_maintenance = happy_street_maintenance
        self.happy_community_events = happy_community_events
    #The get_name function is useful to quickly get a formatted version of someone's name. This may be further appropriate in order to 
    # enhance the usability, such as the program may send people emails based on what their scores were.
    def get_name (self) -> str:
        return self.name + " " + self.last_name


class BackEndManager:
    def __init__(self):
        pass
    #The primary function of this function is to get a list of Happiness record objects which have been saved within a file, based on the fileURL variable.
    # It is common practice to declare the output variable within this program. This ensures it is simple to follow the tracks of what the variable is equal to, and what
    # it changes to throughout the running of the program.
    #Since this function SHOULD always be fetching a file which is certain to be there, it will not be returning errors for opening a file which does not exist.
    # This does bring in an opportunity to declare how this code could be improved, however it may not always consistently be useful.
    # The improvement would be, within this function, to check whether the file exists prior to attempting to open it. However, this is completed by the common format within
    # the frontend.py code. This does provide for opportunities of expansion, possibly creating a single datafile which contains all entries, therefore allowing the 'town' file be
    # broken up into different regions, yet still adding to one overarching town file.
    #The disadvantage of needing to check for the file's existance so regularly, is that it will slow down the program because it is relying on other mechanical factors such as
    # read/write speeds, and other IO operation speeds.
    #Then the file is completely processed within a readline loop and closed once the function has concluded. There are not further efficient ways to conduct this.
    def Get_Data (self, fileURL : str) -> list:
        output = []
        file = open(fileURL, "r")
        nextLine = file.readline()
        #This loop ensures that the entire file has been read. A more efficient use of this would be to instead use file.readlines() which would return an entire array of each line,
        # making us able to use a for-loop, which are regularly far more efficient than a while loop. The other technique is an inline-for loop, or recursion, which relies upon the
        # functional programming paradigm, which is available in most modern programming languages such as JavaScript, C++, C#, and Python. However, this standard does not meet the
        # functional requirements of this program. Therefore, it is necessary read through each individual line in this program, and there is no further better method.
        #The code within the while loop is a simple run-through, ensuring the data is accurate and that the original file has not been modified. If it has, the system will throw errors
        # and not compute any further.
        # There are no further ways to increase the efficiency of this programming block, other than enhancing the problem-handling features within. If the files remain unmodified,
        # however, there should be no issues with handling the errors within. The output block at the end appends the formatted line, including integers, strings, and a boolean value.
        while nextLine != "":
            unformatted = self.Split_Data(nextLine[:-1])
            likes_the_town = False
            if unformatted[2] == "1":
                likes_the_town = True
            x = 3
            each_preference = []
            #The below loop is required in order to go through the final 6 values within the code, and it will try to parse each and every value into an integer.
            # This is where the problem handling falls-short within the program, as it could be done from an earlier stage - however, if this is done, it will not be certain
            # where specifically the error is being thrown from. For example, if it were prior to opening a file, it would not be certain as to which line the error occurred on.
            # This enhances the problem-solving aspect of it, however it still does rely on the fact that the data has remained unmodified within the csv.
            while x < len(unformatted):
                try:
                    each_preference.append(int(unformatted[x]))
                except:
                    sys.stdout.writelines(unformatted[x] + " is not typeof int")
                finally:
                    x+=1
            formatted = Happiness(unformatted[0], unformatted[1], likes_the_town,
                                    each_preference[0], each_preference[1], each_preference[2],
                                    each_preference[3], each_preference[4], each_preference[5])
            output.append(formatted)
            nextLine = file.readline()
        file.close()
        return output

    #The split_data function replicates what the list function of split(str) does. Therefore, it may be more efficient to utilise the library form, as it would be programmed
    # through a different paradigm as this, and therefore will be utilising less variables, lines of code and therefore, require less CPU load.
    # The output is declared as always at the beginning, to ensure that we know which form of data we are outputting and there can be no confusing, placing an integer into a
    # string array, resulting in a type error.
    def Split_Data (self, to_array : str) -> list[str]:
        output = [""]
        n = 0
        #This loop will execute through each individual line of code, and if it is a comma, as CSV file work, it will go to the next array item. This will not work with
        # line breaks, however it can simply be implimented with [ if n+1 < len(array) and to_array[n] + to_array[n+1] == "\n" ]. The usage of this would be additional, if
        # the program were reading the entire file in one line, rather than reading individual lines. Therefore, this feature has not been included, as it would be redundant
        # and never enter that segment of the code block.
        while n < len(to_array):
            #This code block segment is to ensure that once the comma is approached, it will add a new element for the code the continue to execute through; as seen in the
            # elif statement below. The program appends a new value to the output array, and it must be a string, otherwise it may carry a none values and adding a string to a None
            # will not work the way intended, and may throw a type error.
            if(to_array[n] == ","):
                output.append("")
            #Within this code block there are no further effiencies which can be made. Grabbing the latest output array item, and adding the current segment the program is scanning within.
            else:
                output[len(output) - 1] += to_array[n]
            n+=1
        return output

    #This function will save the data to a file. The only further effiency to this program would be to output a True/False value at the end, possibly representing whether it had
    # failed. However, it may introduce further complexities within the frontend.py code, and therefore the way this function has been programmed is in order to
    # increase the readability of the frontend code.
    def Save_Data (self, fileURL : str, data : list) -> str:
        input = ""
        x = 0
        #Looping through the data list, it is required to ensure that all values we are placing into the input string are also strings, in order to not return a type error.
        # adding a number to a string does not work. There are no further efficiencies to this code block which can be made. The (input+=str) section is repeated in order to increase
        # the readability of this code, it is possible to do this within one line. However, I have broken up each section into 3 so it does not end up being a 300+ column line line.
        while x < len(data):
            happy = "0"
            if(data[x].happy == True):
                happy = "1"
            input += data[x].name + "," + data[x].last_name + "," + happy + ","
            input += str(data[x].happy_city_services) + "," + str(data[x].happy_housing) + "," + str(data[x].happy_schooling) + ","
            input += str(data[x].happy_police) + "," + str(data[x].happy_street_maintenance) + "," + str(data[x].happy_community_events)
            input += "\n"
            x+=1
        file = open(fileURL, "w")
        file.write(input)
        file.close()
        return input

    #This function is designed in order to check whether a file exists. I have asked a question whether it is allowed, however I did not receive a response.
    # There are no further ways this function may be improved, as it will open and close a file - by creating one. If it cannot create one, it has never opened the file
    # in the first place. It will return a boolean value back to the frontend stating either 'no, the file exists, and hasn't been created' or, 'yes, this file did not exist,
    # so I have created a new one'. The only slight difference would include a true/false for whether the file exists, and then requiring another function to create the file.
    # Doing so would create a high amount of overload to I/O, and therefore should be minimised at every available opportunity. As, if the product is scaled it would
    # not function properly.
    def Check_File (self, fileURL : str) -> bool:
        output = True
        #This try statement is due to the fact that the open(str, "x") returns an error on the event that the file already exists. Essentially, it is trying to create a file,
        # and the error is "file already exists". However, this is handled gracefully within the program in order to reduce user confusion. There is no further efficiencies which
        # may be brought into this system.
        try:
            file = open(fileURL, "x")
            file.close()
            sys.stdout.write("File Created!\n")
        except:
            output = False
            sys.stdout.write("File Found!\n")
        return output

    #This system transfers the unreadable format of the object into a readable format, used for reading the data in mass. It repeats through each individual object through a list
    # However, this cannot be made further efficient as it is required in order to display all records to the user. It does not process data, it just translates it from a 
    # computer format into a readable human format.
    def Show_Records (self, data : list):
        x = 0
        output_str = ""
        while x < len(data):
            are_they_happy = "No"
            if(data[x].happy == True):
                are_they_happy = "Yes"
            output_str += "-==[" + data[x].get_name() + "]==-\n"
            output_str += "Is " + data[x].get_name() + " generally happy? " + are_they_happy + "\n"
            output_str += "Happiness Scores for Public Services:\n - Services: " + str(data[x].happy_city_services) + "\n"
            output_str += " - Cost of Housing: " + str(data[x].happy_housing) + "\n"
            output_str += " - Schooling: " + str(data[x].happy_schooling) + "\n"
            output_str += " - Policing: " + str(data[x].happy_police) + "\n"
            output_str += " - Street Maintenance: " + str(data[x].happy_street_maintenance) + "\n"
            output_str += " - Community Events: " + str(data[x].happy_community_events) + "\n\n"
            x+=1
        sys.stdout.write(output_str)

    #This is one of the menu items within the frontend. It is within the backend, since it would be more reliable to place it into the hands of a backend developer. This is 
    # since the object would have to be changed by both the frontend and the backend developer in order to achieve the given outcome. If there are any modifications to the
    # dataset that the administration would like to make, such as including how happy the citizen is about the dog teaching classes, it would require a change to the backend
    # class. Placing this function and procedure into the frontend would possibly make updates for the backend and frontend inconsistent and the class being of different versions
    # within the overall project. This code follows a bounding ball, and is readable.
    def add_record (self, data : list) -> list:
        sys.stdout.write("First Name: ")
        f_name = sys.stdin.readline().strip()
        sys.stdout.write("Last  Name: ")
        l_name = sys.stdin.readline().strip()
        happy = self.confirm("Is " + f_name + " " + l_name + " happy?")
        sys.stdout.write("> Happiness Scores for Public Services [1->5]...\n")
        city_services = self.get_score(" - City Services", 1, 5)
        housing = self.get_score(" - Cost of Housing", 1, 5)
        schooling = self.get_score(" - Schooling", 1, 5)
        policing = self.get_score(" - Policing", 1, 5)
        street_maintenance = self.get_score(" - Street Maintenance", 1, 5)
        community_events = self.get_score(" - Community Events", 1, 5)
        new_record = Happiness(f_name, l_name, happy, city_services, housing, schooling, policing, street_maintenance, community_events)
        data.append(new_record)
        return data

    #This function intends to get user input, and ensure it is correct. It is mostly utilised by the function above, however it offers versatility for other applications
    # as it contains a minimum and a maximum limitation. This limitation is useful since it can be transferred from one application into many.
    # There are very few ways this function may be improved any further, since it formats the question into a common format so that the user does not
    # experience any unusual artifacts within the questioning format.
    #The function firstly declares the score to be the minimum value - 1, in order for it to be able to trigger the while loop. Doing this reduces the amount of variable the
    # program is processing, and ensures that the while loop is initially triggered, starting the question.
    def get_score (self, question : str, min : int, max : int) -> int:
        score = min - 1
        #The most effective method is to ask the question, try and convert it into an integer - append and errors - and then to output it back to the location the function has been
        # called from. This code block segements all of these within, and therefore no further efficiencies can be made. Within the assessment criteria, it does mention that try
        # /except/finally blocks should not contain minimal amounts of code, however, this is the simplest way in order to achieve the given outcome.
        while score < min or score > max:
            sys.stdout.write(question + " [" + str(min) + "-" + str(max) + "]: ")
            try:
                score = int(sys.stdin.readline())
            except:
                sys.stdout.write("Invalid Input: Not a Number\n")
            finally:
                if(score < min or score > max):
                    sys.stdout.write("Invalid Input: Not Within Range " + str(min) + " - " + str(max) + "\n")
        return score

    #This function simply returns the main menu back to the frontend, this is due that it requires to check whether the file has been modified. The modification of the file
    # changes the output, and therefore the if statement has been placed in. The output+= repetition may be able to reduce in order to just one line, however that line would be extensively long.
    # There is no requirement for the strings to be formatted into a single line, and this does increase the readability of the program.
    def get_main_menu (self, current_file : str, modified : bool) -> str:
        output = "\n  ________________\n"
        output+= " / TOWN HAPPINESS \\"
        # Rather than breaking the line as above, it is done here just in case the file has been modified, adding an asterisk. This makes it noticeable to the user that they have
        # unsaved changes, making it more user-friendly. This has no other simpler way to be done, other than by using ternary operators, which are not within the functional
        # requirements. This would be done by doing [ output += modified ? "*\n" : "\n"; ]
        if modified:
            output += "*\n"
        else:
            output += "\n"
        output+= " | [A]dd Record   |\n"
        output+= " | Show [R]ecords |\n"
        output+= " | [C]hange File  | (" + current_file + ")\n"
        output+= " | [S]ave Records |\n"
        output+= " | [Q]uit         |\n"
        output+= " | Option: "
        return output

    #This system is in order to accurately fetch a menu, through to a submenu. Since the program does not utilise submenus, it has not been necessary to include any further lines
    # other than the main menu. Unfortunately, reflecting back on this program, it was not used as often as it would have been useful.
    # However, this function is as efficient as the program demands of it. It may be increased by using builtin functions such as array contains operators, such as str in list.
    # Though, this does not exist within the functional requirements and therefore has been omitted. As mentioned within the frontend.py, where this function is majorly called from,
    # The final output may be "EI", representing that there was an error in processing the response. Error: Input. This could be made further efficient by possibly adding another
    # variable after [ menu_type : str = None ] as [ "question : str" ], this is since it would increase the useability of this function in different parts of the program.
    def get_input (self, menu_type : str = None) -> str:
        output = ""
        #This code block is executed if the function is called in its most basic format [ get_input() ]. This fragment cannot be made any further efficient.
        if(menu_type == None):
            output = sys.stdin.readline().strip()
        #This code block is within the main menu, it cannot be made any further efficient. The strange input handling is so it cannot return an error. This may cause a debate
        # whether it is just sloppy programming; avoiding errors where necessary, or whether it is efficient usage of concatenation. I have found that this technique reduces
        # programming time, and returns the same errors no matter what. The only shortfall within this, is that if the user inputs "QER", for example, it will grab the first 
        # letter "Q", and process the later functions off that. This may be what is intended, or not. It must be declared within a requirement in order to achieve the desired
        # result.
        elif(menu_type == "main"):
            input = (sys.stdin.readline().strip().upper() + " ")[0]
            #This segment of the code cannot be made any further efficient, other than by using the tools which python provides, such as the "in" operator and checking whether the
            # input exists within a list of acceptable inputs.
            if input == "A" or input == "C" or input == "Q" or input == "R" or input == "S":
                output = input
            else:
                output = "EI"
        return output

    #This function is efficient as possible within the requirements. As python is a language which approves of changing the datatype of a variable, it may be able to 
    # handle more exceptions simpler. This function exists in order to get the load file, and not to load that file. This improves transferrability for the frontend, however
    # may cause confusion to a frontend developer. Therefore, the only major efficiency enhancement I could find is that it may be conjoined within multiple functions in order
    # to reduce the size of the frontend code.
    def get_load_file (self) -> str:
        input = False
        output = ""
        #This while loop is necessary as it awaits for the user to be happy with their inputs. Loading an incorrect file may cause detrimental issues for a user depending on
        # their audience. Therefore, two steps of getting a readline input are made, both are through another command. Double confirming for the sake of safety.
        while input == False:
            sys.stdout.write("Load File (csv): ")
            output = self.get_input() + ".csv"
            input = self.confirm("Are you sure you would like to load "+output+"?")
        return output

    #Confirming the user's input is an essential part of this program, this function is very similar in terms of the get_input function, however it only processes a 
    # 'yes' or 'no' answer. The added benefit to this, if the user does not understand, eventhough they may enter "Yes" as the word completely, it will still function properly
    # as intended. This was done purposely in order to continue with the same functional requirement placed on by the input processing which is conducted within the get_input
    # function. The output remains False at the start, and the while loop disregards it, and continues until the input is correct. By being bound by datatype consistency,
    # the code appropriately processes these values as is most appropriate.
    def confirm (self, text : str) -> bool:
        output = False
        input = ""
        #This code block is highly similar to the get_input process, and the reasoning for the input being placed as so is explained within that code comment.
        # Other than that, this code works as efficiently as possible, checking only against the input which in the first loop will not be either y, nor n.
        while input != "Y" and input != "N":
            sys.stdout.write(text+"\n[Y]es/[N]o: ")
            input = (sys.stdin.readline().strip().upper() + " ")[0]
            #This short if, elif block contains a somewhat complex set of instructions, in order to make this function achieve its goal. In the event of being Y, the output is changed
            # Another loop will not be made. In the event of not being N, there were not valid inputs - this is since the input equalling Y has already been checked, and the codeblock
            # will stop if this statement is True. This is the most efficient method to conduct this, there are no further better ways to convert this "y" and "n" string into a 
            # true and false boolean.
            if input == "Y":
                output = True
            elif input != "N":
                sys.stdout.write("Error: Please Enter a Valid Answer (Y/N)\n")
        return output