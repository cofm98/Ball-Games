import sys
import random
import time

# Include two or more string variables with values

sys.stdout.write("Think of a number between 0 and 100 and I will try to guess it. Just say \"higher\" or \"lower\".\n")
guessedAnswers = []
maxNumber = 100
minNumber = 0
rudeCount = 0

correct = False
while not correct:
    guess = random.randint(minNumber, maxNumber)
    if(minNumber == maxNumber - 1):
        if(minNumber in guessedAnswers and maxNumber in guessedAnswers):
            sys.stdout.write("Wait it has to be {} or {}. You're not playing right!".format(str(minNumber), str(maxNumber)))
            break
        else:
            sys.stdout.write("Oh! It has to be... ")
    while(guess in guessedAnswers):
        guess = random.randint(minNumber, maxNumber)
    answer = input("Is it {}?".format(str(guess)))

    if(answer.lower() == "higher"):
        minNumber = guess
        guessedAnswers.insert(-1, guess)
    elif(answer.lower() == "lower"):
        maxNumber = guess
        guessedAnswers.insert(-1, guess)
    elif(answer.lower() == "no" and rudeCount < 3):
        guessedAnswers.insert(-1, guess)
        rudeCount+=1
        sys.stdout.write("You're not going to make this easy are you... ")
    elif(answer.lower() == "no"):
        sys.stdout.write("Look, if you didn't want to play you could've told me. ")
        break
    elif(answer.lower() == "yes"):
        correct = True
        sys.stdout.write("I knew I could get it! ")
        break
    else:
        sys.stdout.write("Sorry, I didn't quite catch that. ")

time.sleep(4)
exit()