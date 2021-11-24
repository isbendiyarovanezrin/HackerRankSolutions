a = int(input())
b = int(input())

d = divmod(a,b)
i = a//b
m = a%b
print(i, m, d, sep="\n")