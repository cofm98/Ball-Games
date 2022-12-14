import sys
sys.stdout.write("Hello?: ")
weekID = int(sys.stdin.readline())
sys.stdout.write("Welcome to week: "+str(weekID))


def display ():
    sys.stdout.write("Pick a number: ")
    numberFirst = int(sys.stdin.readline())
    sys.stdout.write("Number is: "+str(numberFirst))
display()