import sys, random

possibleCodes = ["A","B","C","D","E","F"]
currentHint = []
guesses = []
code = []

for number in range(5):
    code.append(possibleCodes[random.randrange(0,5)])

def compare(guess : str) -> bool:
    if(len(guess) > 5):
        global currentHint
        guess = guess.upper()[0:5]
        for eachLetter in guess:
            if(eachLetter not in possibleCodes):
                sys.stdout.write("Letter [{}] is not in dictionary [A-F]".format(eachLetter))
                return False
        guesses.append([*guess])
        if("".join(code) == guess):
            sys.stdout.write("Code has been cracked!\n")
            if(len(guesses) > 0):
                for eachGuessID in range(len(guesses)):
                    sys.stdout.write("[{}] - ".format(str(eachGuessID+1)) + "-".join(guesses[eachGuessID]) + "\n")
            sys.stdout.write("[C]  [{}]".format("-".join(code)) + "\n")
            sys.stdout.write("It took only " + str(len(guesses)) + " guesses to get it right!")
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

correct = False
while not correct:
    if(len(guesses) < 8):
        sys.stdout.write("\nThe code is 5 letters [X-X-X-X-X]. Any letter from A to F.\nBe warned! You only have 8 guesses!\n")
        if(len(currentHint) > 0):
            sys.stdout.write("     [" + "-".join(currentHint) + "]\n")
        if(len(guesses) > 0):
            for eachGuessID in range(len(guesses)):
                sys.stdout.write("[{}] - ".format(str(eachGuessID+1)) + "-".join(guesses[eachGuessID]) + "\n")
        userInput = sys.stdin.readline()
        correct = compare(userInput)
        sys.stdin.flush()
        sys.stdout.flush()
    else:
        sys.stdout.write("\nMore than 8 guesses have been attempted!")
        correct = True