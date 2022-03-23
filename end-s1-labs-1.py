# JRI 2/26/22

def same_case(a, b):

    upper = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ') # all of the upper and lower case letters stored in two variables
    lower = ('abcdefghijklmnopqrstuvwxyz')

    if a in upper and b in upper:
        return "upper case"
    elif a in lower and b in lower:
        return "lower case"
    elif a in upper and b in lower:
        return 0
    elif a in lower and b in upper:
        return 0
    else:
        return -1 