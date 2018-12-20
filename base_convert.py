
def convert(num, b):
    # print('num:', num, 'b:', b)
    baseDict ={ #dictionary for bases over 9. Could also just add 1-9 and then have one return statement
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F'
    }

    if b > 16:
        raise ValueError('only accepts bases <=16')
    elif b < 2:
        raise ValueError('only accepts bases >= 2')


    """Recursive function that returns a string representing num in the base b"""
    if num // b == 0:  #basecase when num is not divisible by b
        return str(num)

    if num % b > 9 and num % b <= 15:
        return str(convert(num // b, b)) + baseDict[num % b] #converts bases to chars
    else:
        return  str(convert(num // b, b)) + str(num % b) #regular return statement. Need to return convert first otherwise the chars will
                                                        # come back in reverse order
