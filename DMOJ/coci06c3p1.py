#import sys
#input = sys.stdin.readline
import itertools
n=[int(input()) for x in range(9)]
perms=list(itertools.combinations(n,7))
for a in perms:
  if sum(a)==100:
    for i in a:
      print(i)
    break