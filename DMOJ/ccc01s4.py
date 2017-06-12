import sys
from itertools import combinations
from math import sqrt
input = sys.stdin.readline

n = int(input())



cookies = [[int(x) for x in input().split()] for i in range(n)]



maxdist = 0

def dist(p1,p2):
  return (sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2))

def bigcircles(p1,p2,p3):
   a = dist(p1,p2)
   b = dist(p2,p3)
   c = dist(p1,p3)
   s = (a+b+c)/2
   if (a**2)>((c**2)+(b**2)) or (c**2)>((a**2)+(b**2)) or (b**2)>((c**2)+(a**2)):
    #print('wew')
    return(max([a,b,c]))
   else:
    return( (a*b*c)/(2*sqrt(s*(s-a)*(s-b)*(s-c))))
   


combos = combinations(cookies, 3)
for co in combos:
  #print(co)
  temp = bigcircles(co[0],co[1],co[2])
  #print(temp)
  maxdist = max(maxdist,temp)

maxdist = str(round(maxdist,2))
while maxdist[-3]!='.':
  maxdist+='0'

print(maxdist)