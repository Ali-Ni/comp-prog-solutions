import sys
import math
input = sys.stdin.readline

modval = 2**32

for i in range(int(input())):
  temp = int(input())
  if temp<34:
    print (math.factorial(temp)%modval)
  else:
    print 0