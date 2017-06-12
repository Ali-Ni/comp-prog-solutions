import sys
input = sys.stdin.readline

I = int(input())
base = 0
for i in range(I):
  base+=int(input())
  
nxt = base
for i in range(int(input())):
  base+=int(input())
  print(round(base/(I+i+1),3))