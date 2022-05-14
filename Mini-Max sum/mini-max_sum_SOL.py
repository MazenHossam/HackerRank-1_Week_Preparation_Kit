import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    sums=[]
    for i in range(len(arr)):
        sums.append(sum(arr[:i] + arr[i+1:]))
    
    sums.sort()
    print("{} {}".format(sums[0],sums[-1]))
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
