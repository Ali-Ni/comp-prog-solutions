import sys
from collections import Counter
input= sys.stdin.readline
input()

votes = Counter(input())

if votes['A'] == votes['B']:
  print('Tie')
elif votes['A']>votes['B']:
  print('A')
else:
  print('B')