# Language: Python 3

import os

def aVeryBigSum(ar):
    total = 0
    for i in range(len(ar)):
        total += ar[i]
    return total
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()