import sys
input = sys.stdin.readline

n = int(input())
slide = [[] for i in range(n)]
while True:
  temp = [int(x)-1 for x in input().split()]
  #print(temp)
  if temp[0]==-1:
    break
  else:
    slide[temp[1]].append(temp[0])
    
numpaths = [0 for i in range(n)]

numpaths[0] = 1

for point in range(n):
  for i in slide[point]:
    numpaths[point]+=numpaths[i]
#print(slide)
#print(numpaths)
print(numpaths[n-1])