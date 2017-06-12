import sys
input = sys.stdin.readline

n = int(input())

e = sorted([int(x) for x in input().split()])
l = sorted([int(x) for x in input().split()])

l.reverse()


out = 0
for i in range(n):
  out += e[i]*l[i]

print(out)