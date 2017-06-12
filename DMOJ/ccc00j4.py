#import sys
#input = sys.stdin.readline
import itertools
n=int(input())
rivers=[int(input()) for x in range(n)]


while(True):
  k = int(input())
  if k == 77:
    break
  elif k == 99:
    split = int(input())
    rivers.insert(split-1, (int(input())/100)*rivers[split-1])
    rivers[split]=rivers[split]-rivers[split-1]
  else:
    join = int(input())
    rivers[join-1]+=rivers[join]
    rivers.pop(join)
out = ''
for r in rivers:
  out+=str(round(r))+' '
print(out)