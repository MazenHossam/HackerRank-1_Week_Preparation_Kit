import math
import os
import random
import re
import sys

def timeConversion(s):
    mTime=''
    sts = s[-2]+s[-1]
    hr = int(s[0]+s[1])
    
    if sts=='AM':
        if hr==12:
            hr=00   
    else:
        if hr!=12:
            hr+=12
    if hr<10 : mTime='0'+str(hr)+s[2:-2]
    else: mTime=str(hr)+s[2:-2]
            
    return mTime

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
