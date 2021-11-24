# Language: Python 3

def solve(s):
    a = s[:].split()
    for i in a:
        s = s.replace(i, i.capitalize())
    return s

if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)