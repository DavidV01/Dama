

#možná zbytečné
def check_entry(stones,queens):
    if (stones<=12) & (queens==0):
        return True
    elif (stones<=10) & (queens<=1):
        return True
    elif (stones<=8) & (queens<=2):
        return True
    elif (stones<=6) & (queens<=3):
        return True
    elif (stones<=4) & (queens<=4):
        return True
    elif (stones<=2) & (queens<=5):
        return True
    elif (stones==0) & (queens<=6):
        return True
    else:
        return False