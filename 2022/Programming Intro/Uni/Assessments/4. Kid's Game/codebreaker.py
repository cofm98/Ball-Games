import sys, random, string

# codebreaker.py
# RMIT University - Introduction to Programming - COSC2452
# Charlie Morrison - S3654889
# 27 DEC 22

#Code concatenation
#Uses sys.stdout.write
#Uses sys.stdin.readline
#Good naming convention for functions, variables, and file
#Varaible data types
#One or more logic operator with numerical value
#Uses if, elif and else clauses
#Adds values to lists and displays them. No dicts/tuples
#While loops for repetition
#One python file with all code contained.
#Only allowed to call main function outside main code

#No nesting
#Repeating usage of functions

possibleCodes = list(string.ascii_uppercase[0:6])
charLimCode = "A-F"
currentHint = []
guesses = []
guessLimit = 8
password = "1337"

#This function will generate a new code. This code is the one that is being broken.
def generateCode () -> list:
    '''Generates a new code for the game to use'''
    code = []
    for number in range(5):
        code.append(possibleCodes[random.randrange(0,5)])
    return code

#This function checks an input between a specific interger range, and will return False if it is not correct.
#Not correct, being not a number or outside the range
#Otherwise, if the input is correct, it will return the output value as an integer.
#This function is not marked as an int since it may return a bool value; False.
#A better way to create this function would possibly be to restrict it to a while loop since it is the only way which this function is called.
#Another way to improve this function would be to return NaN, or None, or another number placeholder which has no value associated.
def checkInput (min : int, max : int):
    output = sys.stdin.readline()
    try:
        output = int(output)
    except:
        return False
    if(output < min or output > max):
        return False
    flush()
    return output

#It would be easier to do this every time a cmd flush is required, however, it is simpler to call this function
# and it will make the input tidy
def flush () -> None:
    '''Flush inputs'''
    sys.stdin.flush()
    sys.stdout.flush()

#This function compares the input and the wanted-code. It will change the currentHint value to the correct values.
#The better way to do this function would possibly be to add more of the lines of code into the game function rather than the compare function.
#This function does more than just compare, as it does all required steps after comparing the data. A better use of this function
# would be to make the output be a list from being the 'currentHint' variable
def compare(guess : str, code : list) -> bool:
    '''Compare inputs within game, the main function system for the game'''
    global guesses
    global currentHint
    if(len(guess) > 5):
        guess = guess.upper()[0:5]
        for eachLetter in guess:
            if(eachLetter not in possibleCodes):
                sys.stdout.write("Letter [{}] is not in range [{}]".format(eachLetter, charLimCode))
                return False
        guesses.append([*guess])
        if("".join(code) == guess):
            sys.stdout.write("Code has been cracked!\n\n")
            if(len(guesses) > 0):
                for eachGuessID in range(len(guesses)):
                    sys.stdout.write("[{}] - ".format(str(eachGuessID+1)) + "-".join(guesses[eachGuessID]) + "\n")
            sys.stdout.write("[C] -[{}]".format("-".join(code)) + "\n")
            sys.stdout.write("It took only " + str(len(guesses)) + " guesses to get it right!\n")
            sys.stdout.write("""                     ___..-.---.---.--..___
               _..-- `.`.   `.  `.  `.      --.._
              /    ___________\   \   \______    \
              |   |.-----------`.  `.  `.---.|   |
              |`. |'  \`.        \   \   \  '|   |
              |`. |'   \ `-._     `.  `.  `.'|   |
             /|   |'    `-._o)\  /(o\   \   \|   |\
           .' |   |'  `.     .'  '.  `.  `.  `.  | `.
          /  .|   |'    `.  (_.==._)   \   \   \ |.  \         _.--.
        .' .' |   |'      _.-======-._  `.  `.  `. `. `.    _.-_.-'\\
       /  /   |   |'    .'   |_||_|   `.  \   \   \  \  \ .'_.'     ||
      / .'    |`. |'   /_.-'========`-._\  `.  `-._`._`. \(.__      :|
     ( '      |`. |'.______________________.'\      _.) ` )`-._`-._/ /
      \\      |   '.------------------------.'`-._-'    //     `-._.'
      _\\_    \    | AMIGA  O O O O * * `.`.|    '     //
     (_  _)    '-._|________________________|_.-'|   _//_
     /  /      /`-._      |`-._     / /      /   |  (_  _)
   .'   \     |`-._ `-._   `-._`-._/ /      /    |    \  \
  /      `.   |    `-._ `-._   `-._|/      /     |    /   `.
 /  / / /. )  |  `-._  `-._ `-._          /     /   .'      \
| | | \ \|/   |  `-._`-._  `-._ `-._     /     /.  ( .\ \ \  \
 \ \ \ \/     |  `-._`-._`-._  `-._ `-._/     /  \  \|/ / | | |
  `.\_\/       `-._  `-._`-._`-._  `-._/|    /|   \   \/ / / /
              /    `-._  `-._`-._`-._  ||   / |    \   \/_/.'
            .'         `-._  `-._`-._  ||  /  |     \
           /           / . `-._  `-._  || /   |      \
          '\          / /      `-._    ||/'._.'       \
           \`.      .' /           `-._|/              \
            `.`-._.' .'               \               .'
              `-.__\/                 `\            .' '
                                       \`.       _.' .'
                                        `.`-._.-' _.'
                                          `-.__.-'\n""")
            return True
        else:
            outCode = []
            for eachAnswerID in range(len(code)):
                if(code[eachAnswerID] == guess[eachAnswerID]):
                    outCode.append(code[eachAnswerID])
                else:
                    outCode.append("x")
            currentHint = outCode
            return False
    else:
        sys.stdout.write("Less than 5 letters!\n")
        return False

#This is the primary function for the game, called when running the game and in a loop until complete.
# it is used to clean up the main function, seperating it from the settings and making the program into a more readable state.
# This function would be more useful if it handled more of the game functions which are embedded within the 'compare' function
def game () -> bool:
    '''Call the main game'''
    #Import the main settings, it would be more efficient to have these values be non-globals and all references to these variables would be contained within this function
    # This would require re-engineering the function 'compare.'
    global guesses
    global currentHint
    global code
    #Correct is false until made correct
    correct = False
    #Regenerate a new code as soon as the game is opened
    code = generateCode()
    #Clear all guesses from any previous attempts
    guesses = []
    #Clear the previous currentHint variable in case this is not the first game played in this instance of the game
    currentHint = []
    #Loop the function until correct
    while not correct:
        #Limit the guesses to the limitation, set within the settings
        if(len(guesses) < guessLimit):
            #Send out a menu of the requirements, formatted with the variables set within the settings.
            sys.stdout.write("\nThe code is 5 letters [X-X-X-X-X]. Any letter from {}.\nBe warned! You only have {} guesses!\n".format(charLimCode, str(guessLimit)))
            #If there is a current hint tell the user what their hint is this round.
            #The current hint is an array of 5 values either a correct answer at a certain point or x representing an incorrect answer. 
            if(len(currentHint) > 0):
                sys.stdout.write("     [" + "-".join(currentHint) + "]\n")
            #If there are any attempted guesses, let the user know all their guesses up until this point
            if(len(guesses) > 0):
                for eachGuessID in range(len(guesses)):
                    sys.stdout.write("[{}] - ".format(str(eachGuessID+1)) + "-".join(guesses[eachGuessID]) + "\n")
            #Read the user's input guess
            userInput = sys.stdin.readline().strip()
            flush()
            #Run the user's guess through the compare function, it would be more efficient to make the compare function send through a list.
            # The output list would be the same as the currentHint variable, and then the correct/incorrect checks would be done through this function further
            correct = compare(userInput, code)
        #This is in case more than X (guessLimit) guesses have been made, and it will close the game and hold correct as a False value in case future updates are made, this optimises compatibility.
        else:
            sys.stdout.write("\nMore than {} guesses have been attempted!\n".format(str(guessLimit)))
            break
    #The function then outputs whether the user was correct in the end of the game, a True or False value
    return correct


#This is the function to call the settings menu, since it is a long set of if and elif statements with little complex logic, it is useful to be 
# combined into one large code block, seperated from the main function.
def settings () -> bool:
    '''Call the settings menu'''
    #Fetch the variables shared to amend them permanently in the settings
    global guessLimit
    global charLimCode
    global possibleCodes
    #Fetch the password input
    sys.stdout.write("Settings Password: ")
    passwordInput = sys.stdin.readline().strip()
    flush()
    #Check if the password is correct
    if(passwordInput != password):
        return False
    #Repeat the settings until completed, broken by return functions within
    while True:
        #Write up the main settings
        sys.stdout.write("["+"="*16+"]\n"+" "*5+"Settings\n")
        sys.stdout.write("1. Guess Limiter\n")
        sys.stdout.write("2. Character Bounds\n")
        sys.stdout.write("3. Hint Limiter (Not yet implemented)\n")
        sys.stdout.write("4. Back to Menu\n")
        #Ensure settings value is valid, and between 1-4, each option
        settings_input = False
        while settings_input == False:
            settings_input = checkInput(1, 4)
        #Open the guess limiter setting upon option #1
        if(settings_input == 1):
            #Guess Limiter - Write up the menu
            sys.stdout.write("["+"="*16+"]\nGuess Limiter\n")
            sys.stdout.write("1. Easy (8 Guesses)\n")
            sys.stdout.write("2. Medium (6 Guesses)\n")
            sys.stdout.write("3. Hard (4 Guesses)\n")
            sys.stdout.write("4. Impossible (2 Guesses)\n")
            #Ensure settings value is valid, and between 1-4
            guess_limiter = False
            while guess_limiter == False:
                guess_limiter = checkInput(1,4)
            #When the option is set to easy (1), set the guess limit to 8
            if(guess_limiter == 1):
                guessLimit = 8
            #When the option is set to medium (2), set the guess limit to 6
            elif(guess_limiter == 2):
                guessLimit = 6
            #When the option is set to hard (3), set the guess limit to 4
            elif(guess_limiter == 3):
                guessLimit = 4
            #When the option is set to impossible (4), set the guess limit to 2
            elif(guess_limiter == 4):
                guessLimit = 2
        #Open the character bounds settings upon option #2 being selected
        elif(settings_input == 2):
            #Character Bounds - Write up the menu
            sys.stdout.write("["+"="*16+"]\nCharacter Bounds\n")
            sys.stdout.write("1. Normal [A-F]\n")
            sys.stdout.write("2. Hardmode [A-Z]\n")
            #Ensure settings value is valid and between 1 and 2
            char_limits = False
            while not char_limits:
                char_limits = checkInput(1,2)
            #Set the character limits to be contrained within the first 6 characters
            if(char_limits == 1):
                charLimCode = "A-F"
                possibleCodes = list(string.ascii_uppercase[0:6])
            #If option 1 isn't selected; only option 2 is available at this point, set the entire alphabet to the possible codes
            else:
                charLimCode = "A-Z"
                possibleCodes = list(string.ascii_uppercase)
        #The hint limiter hasn't been implemented, so return a statement telling the user it isn't yet available for choice. Return back to the main settings menu after that
        elif(settings_input == 3):
            #Hint Limiter
            sys.stdout.write("Not yet implemented.\n")
        #Otherwise if no other options are selected, only option 4 is available, break the while statement and close the settings menu
        else:
            #Quit
            return True


#The main function. Called in a while loop
def main () -> bool:
    #Send the main menu
    sys.stdout.write(" "*4+"CODE BREAKER" + '''\n ____________________________________________________
T ================================================= |T
| ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|[L
| __________________________________________________[|
|I __==___________  ___________     .  ,. _ .   __  T|
||[_j  L_I_I_I_I_j  L_I_I_I_I_j    /|/V||(g/|   ==  l|
lI _______________________________  _____  _________I]
 |[__I_I_I_I_I_I_I_I_I_I_I_I_I_I_] [__I__] [_I_I_I_]|
 |[___I_I_I_I_I_I_I_I_I_I_I_I_L  I   ___   [_I_I_I_]|
 |[__I_I_I_I_I_I_I_I_I_I_I_I_I_L_I __I_]_  [_I_I_T ||
 |[___I_I_I_I_I_I_I_I_I_I_I_I____] [_I_I_] [___I_I_j|
 | [__I__I_________________I__L_]                   |
 |                                                  |
 l__________________________________________________j\n\n''')
    sys.stdout.write("["+"="*16+"]\n"+" "*7+"MENU\n")
    sys.stdout.write("1. Play\n")
    sys.stdout.write("2. Settings\n")
    sys.stdout.write("3. Exit\n")
    
    #Check for the user's input from a value of 1-3
    input_menu = False
    while input_menu == False:
        input_menu = checkInput(1, 3)
    #If play (1), load the game function
    if(input_menu == 1):
        game()
    #Otherwise, if settings (2), load the settings function
    elif(input_menu == 2):
        settings()
    #Otherwise, if exit (3), close the menu by returning false and this will set the variable below (running) to false, closing the program
    else:
        return False
    #This will return True if 1 or 2 options are selected and after they have completed running
    return True

running = True
while running:
    running = main()