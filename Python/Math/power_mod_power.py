# Language: Python 3

a = int(input())
b = int(input())
m = int(input())

power = pow(a,b)  
modpower = pow(a,b,m)

print(power, modpower, sep="\n")