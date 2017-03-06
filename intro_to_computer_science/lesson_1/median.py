def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))

def median1(a, b, c):
    d = biggest(a, b, c)
    if bigger(a, b) < d:
        return bigger(a, b)
    if bigger(b, c) < d:
        return bigger(b, c)
    if bigger(a, c) < d:
        return bigger(a, c)
    return d

def median(a, b, c):
    d = biggest(a, b, c)
    if a == d:
        return bigger(b, c)
    if b == d:
        return bigger(a, c)
    if c == d:
        return bigger(a, b)