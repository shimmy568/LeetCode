#!/bin/python3

from itertools import count
import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#


def pickingNumbers(a):
    counts = {}
    for value in a:
        if not value in counts:
            counts[value] = 0
        counts[value] += 1

    max_count = 0
    for v in range(1, 100):
        if v in counts and (v + 1) in counts:
            max_count = max(counts[v] + counts[v + 1], max_count)
        elif v in counts:
            max_count = max(counts[v], max_count)

    return max_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
