def enter_metric():
    su = []
    print ("Enter the sudoku values row by row")
    for i in range(9):
        su.append(input().split(' '))
        for j in su[i]:
            if j is '0' or (len(j) !=1) or (not j.isdigit()):
                print ("Not a valid suduku")
                return False
        if len(su[i]) != 9:
            print ("Not a valid row entry")
            return False
    return su

def check(su):
    if not su:
        return False
    count = 0
    for j in range (0,9):
        for n in range(0,9):
            if su[j].count(su[j][n]) <= 1:
                count = count + 0
            else:
                count = count + 1

    cols = [[row[i] for row in su] for i in[0,1,2,3,4,5,6,7,8]]
    leg = 0
    for i in range(0,9):
        for j in range(0,9):
            if cols[i].count(cols[i][j]) <= 1:
                leg = leg + 0
            else:
                leg = leg + 1
    angel = []
    for t in range(3):
        ang = su[t]
        for u in range(3):
            angel.append(ang[u])
    foot = 0
    for be in range(9):
        if angel.count(angel[be]) <= 1:
            foot = foot + 0
        else:
            foot = foot + 1
    if count + leg + foot == 0:
        return True
    else:
        return False
 #   return "Invalid"

sudu = enter_metric()
print (check(sudu))
