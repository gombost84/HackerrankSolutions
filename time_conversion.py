#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    if s[-2:] == 'AM':
        if s[:2] == '12':
            return('00' + s[2:-2])
        return(s[:-2])
    elif s[:2] == '12':
        return s[:-2]
    elif s[1] == ':':
        return(str(int(s[:1]) + 12) + s[1:-2])
    else:
        return(str(int(s[:2]) + 12) + s[2:-2])

if __name__ == '__main__':
    s = '07:05:45PM'

    result = timeConversion(s)
    print(result)