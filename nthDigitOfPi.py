#!/usr/bin/env python3
# nthDigitOfPi.py - script that takes an input and returns Pi to that number of digits.

import math


def nthDigitOfPiMath():
    pi = math.pi
    try:
        r = int(input('How many digits of Pi do you want? '))
        if r < 0:
            print('You must enter a positive number.')
    except ValueError:
        print('That was not an integer.')
    print(round(pi, r))

def nthDigitOfPiString():
    pi2 = ('3.14159265358979323846264338327950288419716939937'
           '5105820974944592307816406286208998628034825342117'
           '0679821480865132823066470938446095505822317253594'
           '0812848111745028410270193852110555964462294895493'
           '0381964428810975665933446128475648233786783165271'
           '2019091456485669234603486104543266482133936072602'
           '4914127372458700660631558817488152092096282925409'
           '1715364367892590360011330530548820466521384146951')
    try:
        t = int(input('How many digits of Pi do you want? ')) + 2
        if t < 0:
            print('You must enter a positive number.')
    except ValueError:
        print('That was not an integer.')
    print(pi2[:12])


if __name__ == '__main__':
    nthDigitOfPiMath()
    nthDigitOfPiString()
