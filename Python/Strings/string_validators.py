if __name__ == '__main__':
    s = input()
    n = any(i.isalnum() for i in s)
    a = any(i.isalpha() for i in s)
    d = any(i.isdigit() for i in s)
    l = any(i.islower() for i in s)
    u = any(i.isupper() for i in s)

    print(n, a, d, l, u, sep="\n")