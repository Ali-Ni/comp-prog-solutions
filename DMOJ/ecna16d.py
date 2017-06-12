from sys import stdin
from heapq import *
from collections import defaultdict, deque
input = stdin.readline

n, m = [int(x) for x in input().split()]
langs = input().split()
l = {"English":0}
for i in range(1,n+1):
  l[langs[i-1]]=i
costs = [[-1 for k in range(n+1)] for i in range(n+1)]
adj = [[] for i in range(n+1)]
for i in range(m):
  a, b, c = input().split()
  a, b, c = l[a], l[b], int(c)
  costs[a][b] = c
  costs[b][a] = c
  adj[a].append(b)
  adj[b].append(a)


q = [(0, 0, 0, None)]
g = defaultdict(list)
visited = set()

totallength = 0
while q:
  l, c, no, p = heappop(q)

  if no in visited:
    continue
  #print(l, c, n, p)
  visited.add(no)
  if p!=None:
    g[p].append(no)
  totallength+=c
  for child in adj[no]:
    if child not in visited:
      heappush(q, (l+1, costs[no][child],child, no))

if len(visited)<n+1:
  print("Impossible")
else:
  print(totallength)