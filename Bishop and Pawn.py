# link to problem https://app.codesignal.com/arcade/intro/level-9/6M57rMTFB9MeDeSWo

def bishopAndPawn(bishop, pawn):
    xb = int(ord(bishop[0]) - 96)
    yb = int(bishop[1])

    xp = int(ord(pawn[0]) - 96)
    yp = int(pawn[1])

    if xb == xp:
        return False

    c = xb + yb
    d = xp + yp
    if (abs(c - d)) % 2 == 0:
        return True
    else:
        return False

