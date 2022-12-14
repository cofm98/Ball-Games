#
# power-consumption.py
# Charlie Morrison
# 14 DEC 22
#
# This is a university project for 'Introduction to Porgramming'
#

import sys

powerzone1 = [34055.6962,29814.68354,29128.10127,28228.86076,27335.6962,26624.81013,25998.98734,25446.07595,24777.72152,24279.49367,23896.70886,23544.3038,23003.5443,22329.11392,22092.1519,21903.79747,21685.06329,21484.55696,21107.8481,20998.48101,20870.88608,20870.88608,20597.46835,20421.26582,20524.55696,20482.02532,20530.63291,20512.40506,20494.17722,20311.89873,20542.78481,20621.77215,20627.8481,20797.97468,20858.73418,21393.41772,22219.74684,21928.10127,21776.20253,21654.68354,21466.32911,20846.58228,19983.79747,18908.35443,18167.08861,18075.94937,18063.79747]

#Total amount of power calculated by adding every individual value within the list (powerzone1) until all values have been added.
#The private variable 'output' is used in order to not have any affect on the main, public, thread running.
def pwr_ttl ():
    '''The total amount of power usage throughout a 24 hour period'''
    output = 0
    #num -> number in the array 'powerzone1' being processed, read through the entire list one-by-one
    #Added the value of 'num' onto 'output' until the total amount is gathered.
    for num in powerzone1:
        output += num
    return output
#Get the avergage power by running the pwr_ttl function (total power) and then dividing it by the total length of values nested within the list
#output -> Output value, the private value to adjust accordingly in order to apply calculations onto.
def pwr_avg ()->float:
    '''Average power usage throughout a 24 period'''
    output = pwr_ttl()
    output/=len(powerzone1)
    return output
#Get the minimum power by grabbing the first value of the powerzone1 list and running through checking if any values are less than this.
#output -> Output value, the private value to adjust accordingly in order to apply calculations onto.
def pwr_min ()->float:
    '''Minimum power usage throughout a 24 hour period'''
    output = powerzone1[0]
    #In order to be able to run through each and every value within powerzone1:
    #num -> Number being checked against
    for num in powerzone1:
        #if number is less than output. We can use not greater than or equal to output, but this will be confusing to read.
        #Set the value to the output so the next iteration will then check if value at position n+1 is further less than this current value, if the conditions are met.
        if(num < output):
            output = num
    return output
#Get the highest power usage by grabbing the first value of powerzone1 and running through checking if any values are higher than this.
#output -> Output value, the private value to adjust accordingly in order to apply calculations onto.
def pwr_max ()->float:
    '''Maximum power usage throughout a 24 hour period'''
    output = powerzone1[0]
    #In order to be able to run through each and every value within powerzone1:
    #num -> Number being checked against
    for num in powerzone1:
        #if number is greater than output. We can use not less than or equal to output, but this will be confusing to read.
        #Set the value to the output so the next iteration will then check if value at position n+1 is further greater than this current value, if the conditions are met.
        if(num > output):
            output = num
    return output
#Get the mode value by assigning the list to 'temp' in order to not impact the integrity of the powerzone list,
#Sorting the list from highest to lowest, using built in functions
#If the length is 'uneven' (i.e., has a length with an even number - starting at 0 causes this opposite) we can simply divide the length of the array by 2 and return the middle value
#If the length is 'even' (as explaned above) we need to add the two closest values together and divide them by two
def pwr_mod ()->float:
    '''Mode power usage; the centre value when sorted from lowest to highest or the midpoint between the two centre values.'''
    temp = powerzone1
    temp.sort()
    #The length of temp modulus 2, if the array length is even it will result in 0, if not it will result in 1. This is the opposite to if the amount of values in the array are odd or even, as the length is one less than the amount of values in the array.
    #output -> Output value, the private value to adjust accordingly in order to apply calculations onto.
    if(len(temp) % 2 == 0):
        output = temp[int(len(temp) / 2)]
    #output -> Output value, the private value to adjust accordingly in order to apply calculations onto.
    else:
        output =    (
                        temp[int((len(temp)-1) / 2)]
                        + 
                        temp[int((len(temp)+1) / 2)]
                    ) / 2
    return output

sys.stdout.write("Average power: {}MW\nMinimum power: {}MW\nMaximum power:{}MW\nNormal power consumption:{}MW\nTotal power supplied to town:{}GW".format(
    str(round(pwr_avg())/1000),
    str(round(pwr_min())/1000),
    str(round(pwr_max())/1000),
    str(round(pwr_mod())/1000),
    str(round(pwr_ttl() / 1000)/1000)));
