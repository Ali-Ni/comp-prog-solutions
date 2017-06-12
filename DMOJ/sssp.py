from sys import stdin
from heapq import *
input = stdin.readline

n, m = [int(x) for x in input().split()]

g = [[float('inf') for j in range(n)] for i in range(n)]

for i in range(m):
  temp = [int(x) for x in input().split()]
  #print(temp)
  g[temp[0]-1][temp[1]-1] = min(g[temp[0]-1][temp[1]-1], temp[2])
  g[temp[1]-1][temp[0]-1] = min(g[temp[1]-1][temp[0]-1], temp[2])



visited = set()
q = [(0,0)]
d = [-1 for i in range(n)]
d[0] = 0
while q:
  cost, node = heappop(q)
  if node not in visited:
    visited.add(node)
    d[node] = cost
    
    for i in range(n):
      if i not in visited:
        temp = g[node][i]
        if temp != float('inf'):
          heappush(q, (cost+temp,i))
        
d = [str(x) for x in d]
print('\n'.join(d))