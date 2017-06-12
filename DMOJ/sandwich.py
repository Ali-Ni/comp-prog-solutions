import sys
input = sys.stdin.readline

n = int(input())
line = input()
forw = []
rev = []
for i in range(n):
  if line[i] == '0':
    rev.append(i+1)
  else:
    forw.append(i+1)

for i in reversed(forw):
  print(i)
for j in rev:
  print(j)