#!/usr/bin/env python

from random import randint

def ornament():
    if randint(0, 99) > 80:
        return "!@#$%^&"[randint(0, 6)]
    else:
        return ' '

def bough(n, last=False):
    first = '/' + "".join([ornament() for m in range(0, n * 2 - 1)]) + '\\'
    if last:
        second = '/' + '_' * (n * 2 + 1)  + '\\'
    else:
        second = '/' + "".join([ornament() for m in range(0, n * 2 - 1)]) + '\\'
    return [first, second]

def tree(height):
    return (['*'] +
            sum([bough(n) for n in range(1, (height - 1) // 2)], []) +
            bough((height - 1) // 2, True) +
            ['| |'])

print '\n'.join([s.center(80) for s in tree(20)])
