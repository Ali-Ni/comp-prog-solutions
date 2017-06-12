import sys
from collections import Counter
input= sys.stdin.readline
counter = Counter([int(input()) for i in range(3)])

if sum([counter[key]*key for key in counter.keys()]) !=180:
  print("Error")
elif len(counter)==2:
  print("Isosceles")
elif len(counter)==3:
  print("Scalene")
else:
  print("Equilateral")