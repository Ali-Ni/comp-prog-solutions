import sys
input = sys.stdin.readline

n , m = [int(x) for x in input().split()]

g = [[] for x in range(n+1)]
#grev = [[] for x in range(n)]
for i in range(m):
  temp = [int(x) for x in input().split()]
  g[temp[0]].append(temp[1])
  #grev[temp[1]-1].append(temp[0]-1)
tall,short = [int(x) for x in input().split()]

rip = True
if g[tall] or g[short]:
  out = 'no'
  visited = []
  q=[tall]
else:
  out = 'unknown'
  q=[]
#print(tall)
#print(short)
#print(g)
while q:
  
  node = q[0]
  #print(node)
  del q[0]
  if node ==short:
    #print('YES')
    out = 'yes'
    rip = False
    q = []
    break
  elif node not in visited:
    visited.append(node)
    for child in g[node]:
      q.append(child)
if rip:
  out = 'unknown'
  visited = []
  q=[short]
else:
  q=[]
while q:
  node = q[0]
  del q[0]
  if node ==tall:
    out = 'no'
    q = []
    break
  elif node not in visited:
    visited.append(node)
    for child in g[node]:
      q.append(child)
print(out)