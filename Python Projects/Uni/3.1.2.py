import sys

dbl = lambda a: a * 2
def doubleOrNothing (a:int) -> int:
    '''Double the number. Or, if the double is less than the original number, nothing.'''
    result = a * 2;
    if result < 0:
        result = 0;
    return result;

sys.stdout.write(str(dbl(4)));
sys.stdout.write(str(help(doubleOrNothing)))