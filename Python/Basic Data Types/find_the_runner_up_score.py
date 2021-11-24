# Language: Python 3

n = int(input())
arr = map(int, input().split())
print(sorted(list(set(arr)))[-2])