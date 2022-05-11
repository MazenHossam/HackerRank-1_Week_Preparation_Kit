import math
import os
import random
import re
import sys

def plusMinus(arr):
    pos=0
    neg=0
    zer=0
    for i in arr:
        if i>0:
           pos+=1
        elif i<0:
           neg+=1
        elif i==0:
           zer+=1
    pos=pos/len(arr)
    neg=neg/len(arr)
    zer=zer/len(arr)
    
    print("{:.6f}".format(pos))
    print("{:.6f}".format(neg))
    print("{:.6f}".format(zer))
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
