''' Solution to Between Two Sets
WITHOUT use of built-in math functions (except for sqrt())

Problem: https://www.hackerrank.com/challenges/between-two-sets
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#


def getGCF(a, b):
    a = int(a)
    b = int(b)
    while a != b:
        if (a % b) == 0:
            return b
        if (b % a) == 0:
            return a

        if a > b:
            a = a - b
        else:
            b = b - a

    return a


def getLCM(a, b):
    a = int(a)
    b = int(b)
    return int((a * b) / getGCF(a, b))


def getArrayProperty(num_arr, prop='gcf', lcm_limit=None):
    ''' Get LCM/GCF of an array
    '''
    if prop is 'gcf':
        func = getGCF
    elif prop is 'lcm':
        func = getLCM
    else:
        raise Exception('Unsupported operation.')

    while len(num_arr) > 1:
        # separate to even/odd-indexed terms
        even = num_arr[::2]
        odd = num_arr[1::2]

        new_arr = []
        for a, b in zip(even, odd):
            val = func(a, b)
            if prop is 'lcm' and lcm_limit is not None:
                if val > lcm_limit:
                    return -1

            new_arr.append(val)

        if len(even) > len(odd):
            new_arr.append(even[-1])

        num_arr = new_arr

    res = num_arr[0]
    return res


def getPrimesLessThanX(x):
    ''' a.k.a. Sieve of Eratosthenes
    '''
    x = int(x)
    if x <= 2:
        return [2]

    e = list(range(2, x))
    for i in range(0, int(math.sqrt(x)) + 1):
        if i == len(e):
            break

        if e[i] != 0:
            for j in range(i+1, len(e)):
                if (e[j] % e[i]) == 0:
                    e[j] = 0

    return [i for i in e if i != 0]


def getNumFactors(num):
    ''' Get number of factors
    '''
    primes = getPrimesLessThanX(int(math.sqrt(num))+1)
    num_factors = 1
    for p in primes:
        cnt = 0
        while (num % p) == 0:
            num /= p
            cnt += 1

        if cnt > 0:
            num_factors *= (cnt + 1)

    if num > 1:
        num_factors *= 2

    return num_factors


def getTotalX(a, b):
    # get LCM of a
    a_lcm = getArrayProperty(a, prop='lcm', lcm_limit=min(b))

    if a_lcm == -1:
        return 0

    # divide each element of b by a's LCM
    b_small = []
    for e in b:
        if (e % a_lcm) == 0:
            b_small.append(int(e/a_lcm))
        else:
            return 0

    # get GCF of b_small
    # (this number that determines how many between numbers there are)
    magic_num = getArrayProperty(b_small, prop='gcf')

    # get number of factors of magic_num
    return getNumFactors(magic_num)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))
    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')
    fptr.close()
