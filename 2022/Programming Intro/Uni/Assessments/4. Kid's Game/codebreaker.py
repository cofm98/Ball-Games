import sys, random

possibleCodes = ["A","B","C","D","E","F"]
guesses = []
code = []

for number in range(5):
    code.append(possibleCodes[random.randrange(0,5)])

def compare() -> bool:
    if("".join(code) == userInput):
        print("Code was correct!")
        return True
    else:
        outCode = []
        for eachAnswerID in range(len(code)):
            #print("Checking {} against {} at {}".format(userInput[eachAnswerID], code[eachAnswerID], str(eachAnswerID)))
            if(code[eachAnswerID] == userInput[eachAnswerID]):
                outCode.append(code[eachAnswerID])
            else:
                outCode.append("x")
                
        print("-".join(outCode))
        return False

correct = False
while not correct:
    
    userInput = sys.stdin.readline()[0:5]
    guesses.append(userInput)
    correct = compare()
    sys.stdin.flush()
