def markCliffs(r, c, m, y, x, d):
    a = r - 1
    while a >= 0 and d != 'd':
        if m[a][c] == 1:
            m[a][c] = -1
            markCliffs(a, c, m, y, x, 'u')
        else:
            break
        a -= 1
    
    a = r + 1
    while a < y and d != 'u':
        if m[a][c] == 1:
            m[a][c] = -1
            markCliffs(a, c, m, y, x, 'd')
        else:
            break
        a += 1

    a = c - 1
    while a >= 0 and d != 'r':
        if m[r][a] == 1:
            m[r][a] = -1
            markCliffs(r, a, m, y, x, 'l')
        else:
            break
        a -= 1
    
    a = c + 1
    while a < x and d != 'l':
        if m[r][a] == 1:
            m[r][a] = -1
            markCliffs(r, a, m, y, x, 'r')
        else:
            break
        a += 1

def countCliffs(m):
    y = len(m)
    x = len(m[0])

    l = 0
    for r in xrange(y):
        for c in xrange(x):
            if m[r][c] == 1:
                l += 1
                m[r][c] = -1
                markCliffs(r, c, m, y, x, 'r')

    return l


seaMap = [[1,0,1], 
 [1,1,0], 
 [0,0,0]]

print countCliffs(seaMap)