import sys, math
input = sys.stdin.readline

n = int(input())
poss = set()
for i in range(64):
  poss.add(2**i)

for i in range(n):
  if int(input()) in poss:
    print('T')
  else:
    print('F')