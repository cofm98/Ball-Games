import sys
sys.stdout.write("Welcome to Age Processor 3000 MAX")

ageGroups = [18,30,50,70]

def CheckAge():
    if(age < ageGroups[0]):
        sys.stdout.write("You're a young whipper snapper!")
    elif(age < ageGroups[1]):
        sys.stdout.write("At least you're not a teenager anymore")
    elif(age < ageGroups[2]):
        sys.stdout.write("Would you like to go out for a glass of wine and cheese?")
    elif(age < ageGroups[3]):
        sys.stdout.write("Do you plan on going to the Bahamas during your retirement?")
    else:
        sys.stdout.write("Enjoy the Bahamas!")

while(True):
    age = input("\n\nWhat is your age?\n")
    try:
        age = int(age)
        CheckAge()
    except:
        if(age == "exit"):
            break
        sys.stdout.write("ERROR: INVALID INPUT")

    


# if Number1:
#     sys.stdout.write("You are a child")
# if Number2:
#     sys.stdout.write("You are a young adult")
# if Number3:
#     sys.stdout.write("You are a mature adult")
# if Number4:
#     sys.stdout.write("You are middle aged")
# if Number5:
#     sys.stdout.write("Enjoy your retirement!!")