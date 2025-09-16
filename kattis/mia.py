s0 = 1
s1 = 1
r0 = 1
r1 = 1

def points(x, y):
    v = 0
    if (x == 1 and y == 2) or (y == 1 and x == 2):
        v = 3
    elif (x == y):
        v = 2
    else:
        v = 1
    return v
        
def compare_d(x1, x2, y1, y2):
    if max(x1, x2) > max(y1, y2):
        print("Player 1 wins.")
        return
    elif max(x1, x2) < max(y1, y2):
        print("Player 2 wins.")
        return
    else:
        if min(x1, x2) > min(y1, y2):
            print("Player 1 wins.")
            return
        elif min(x1, x2) < min(y1, y2):
            print("Player 2 wins.")
            return
        else:
            print("Tie.")

def compare_r(x1, x2, y1, y2):
    xp = (max(x1, x2) * 10) + min(x1, x2)
    yp = (max(y1, y2) * 10) + min(y1, y2)
    
    if xp > yp:
        print("Player 1 wins.")
    elif yp > xp:
        print("Player 2 wins.")
    else:
        print("Tie.")

while True:
    l = input().split()
    s0 = int(l[0])
    s1 = int(l[1])
    r0 = int(l[2])
    r1 = int(l[3])

    if s0 == 0 and s1 == 0 and r0 == 0 and r1 == 0:
        break

    sp = points(s0, s1)
    rp = points(r0, r1)
    
    if sp > rp:
        print("Player 1 wins.")
    elif sp < rp:
        print("Player 2 wins.")
    else:
        if sp == 2:
            compare_d(s0, s1, r0, r1)
        else:
            compare_r(s0, s1, r0, r1)
