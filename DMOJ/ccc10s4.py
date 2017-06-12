import sys
from heapq import *
from collections import defaultdict, Counter
input = sys.stdin.readline

m = int(input())


meme = {}
g = [[float('inf') for i in range(m+1)] for j in range(m+1)]
#print(g)
for pen in range(m):
  v = [int(x) for x in input().split()]
  e = v.pop(0)
 
  for i in range(e):
    a = v[i]
    if i==e-1:
      b = v[0]
    else:
      b = v[i+1]
    
    if (a,b) in meme.keys():
      if v[e+i]<g[meme[(a,b)][0]][pen+1]:
        g[meme[(a,b)][0]][pen+1] = v[e+i]
        g[pen+1][meme[(a,b)][0]] = v[e+i]
      meme.pop((a,b))
      meme.pop((b,a))
    else:
      meme[(a,b)] = (pen+1, v[e+i])
      meme[(b,a)] = (pen+1, v[e+i])
for k,v in meme.items():
  if v[1]<g[v[0]][0]:
    g[v[0]][0] = v[1]
    g[0][v[0]] = v[1]
#for each in g:
  #print(each)
  
  
def prim(G,s):
  P, Q = {}, [(0, None, s)]
  l = len(G)
  val = 0
  while Q:
    #print(Q)
    w, p, u = heappop(Q)
    if u in P:
      continue
    else:
      val+=w
      P[u] = p
      for child in range(l):
        if G[u][child] != float('inf'):
          heappush(Q, (G[u][child], u, child))
  return P, val


outside = prim(g, 1)
#print(outside[0])
#c = Counter(list(outside[0].keys())+list(outside[0].values()))
#print(c)
#print(c)
newg = g[:]
newg[0] = [float('inf') for i in range(m+1)]
for i in range(m+1):
  newg[i][0] = float('inf')



inside = prim(newg, 1)


#print(inside[1],outside[1])
if len(inside[0])<m:
  #print('not including the whole meme')
  
  print(outside[1])
else:
  c = Counter(outside[0].values())
  #print(outside)
  if c[0]>=2:
    #print('outside in the middle of MST')
    print(outside[1])
    
  else:
    #print('graph connected and outside on edge')
    print(inside[1])
    
#print(len(inside[0]))
#print(len(outside[0]))