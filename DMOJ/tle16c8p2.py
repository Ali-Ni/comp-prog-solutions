from sys import stdin
input = stdin.readline

for i in range(int(input())):
    out = []
    for each in bin(int(input()))[2:]:
        if each == '0':
            out.append('meme')
        else:
            out.append('dank')
    print(' '.join(out))