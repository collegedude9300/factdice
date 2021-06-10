import random
def dicefunc():
    dice= random.randint(0,9)
    print (" Dice number (1-9) is: ")
    print(dice)
    if dice == 1:
        print ("If you multiply anything by 1, it always results in that number.")
    elif dice == 2:
        print ("Even though anything multiplied by 2 is a composite number, 2 itself is prime.")
    elif dice == 3:
        print ("Fact about three.")
    elif dice == 4:
        print ("There are four quarters in a dollar.")
    elif dice == 5:
        print ("Anything ending in 5, or 0 is divisable by 5.")
    elif dice == 6:
        print ("An insect has six legs.")
    elif dice == 7:
        print ("There are seven days in a week.")
    elif dice == 8:
        print ("An octopus has eight legs.")
    elif dice == 9:
        print ("There are nine planets")
    else:
        print ("No zeroes or negatives allowed.")
dicefunc()
dicefunc()
dicefunc()
dicefunc()
dicefunc()
