import math

def nCr(n,r=4):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

print(round(nCr(int(input()))))