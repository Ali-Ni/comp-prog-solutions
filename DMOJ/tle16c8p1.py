from sys import stdin
input = stdin.readline

temp = input().strip()[1:]

for i in range(int(input())):
    rekt = False
    line = input().strip()
    for each in temp:
        if each not in line:
            rekt = True
            break
    if rekt:
        print('no')
    else:
        print('yes')