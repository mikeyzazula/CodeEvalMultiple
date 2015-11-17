# Michael Zazula
# Multiples of a Number Challenge - Recursive
import sys

mnfile = sys.argv[1]


def mnumber(file):
    newfile = open(file, "r")

    for line in newfile:
        line = line.split(',')

    
        # value we need to be greater than

        target = int(line[0])

        # the number we need to be greater or equal to the target

        multiple = int(line[1])

        # each time we loop we're going to add this value

        addcontinue = multiple

        #seperate function that does most of the work. 
        findmultiple(multiple, target,addcontinue)



#the function that does most of the work. If multiple is less than target, call findmultiple again with mutliple + addontinue as the first argument. 
def findmultiple(multiple, target, addcontinue):
    if multiple < target:
        findmultiple(multiple + addcontinue , target, addcontinue)
    else:
        print (multiple)

mnumber(mnfile)
