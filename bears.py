def bears(n):
    print(n)

    if n == None:
        raise ValueError('bears > 42')

    if n == 42:
        return True

    if n < 42:
        print("here")
        return False

    if n % 2 == 0: #it return all the way to 150 and then into this if infinitely
        print("%2")
        bool2 = bears(int(n/2))
        if bool2:
            return True

    if n % 4 == 0 and int(str(n)[-1]) != 0 and int(str(n)[-2]) != 0:
        print("%4")
        bool4 = bears(n - (int(str(n)[-2])*int(str(n)[-1])))
        if bool4:
            return True

    if n % 3 == 0 and int(str(n)[-1]) != 0 and int(str(n)[-2]) != 0:
        print("%3")
        bool3 = bears(n - (int(str(n)[-2])*int(str(n)[-1])))
        if bool3:
            return True

    if n % 5 == 0:
        print("%5")
        bool5 = bears(n - 42)
        if bool5:
            return True

    return False
