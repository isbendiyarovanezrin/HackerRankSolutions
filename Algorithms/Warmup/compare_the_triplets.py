# Language: Python 3

import os

def compareTriplets(a, b):
    Alice = [] 
    Bob = []
    
    if a[0] > b[0]:
        Alice.append(1)
    elif a[0] == b[0]:
        Alice.append(0)
        Bob.append(0)
    else:
        Bob.append(1)    
        
    if a[1] > b[1]:
        Alice.append(1)
    elif a[1] == b[1]:
        Alice.append(0)
        Bob.append(0)
    else:
        Bob.append(1)
        
    if a[2] > b[2]:
        Alice.append(1)
    elif a[2] == b[2]:
        Alice.append(0)
        Bob.append(0)
    else:
        Bob.append(1)
        
    return(sum(Alice), sum(Bob))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()