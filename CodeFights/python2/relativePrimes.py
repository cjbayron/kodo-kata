def getPrimes(x):
    e = range(2, x)
    for i in xrange(0, int(math.sqrt(x)) + 1):
        if e[i] != 0:
            for j in xrange(i+1, len(e)):
                if not e[j] % e[i]:
                    e[j] = 0

    return [i for i in e if i != 0]

p = getPrimes(1010)

def relativePrimes(v):
    c = set(v)

    for x in p:
        d = [i for i in v if not i % x]
        if len(d) > 1:
            c -= set(d)

    return [i for i in v if i in c]