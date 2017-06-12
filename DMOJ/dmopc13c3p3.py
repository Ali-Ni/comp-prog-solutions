import sys
input = sys.stdin.readline

n, h  = [int(x) for x in input().split()]
e = [[] for j in range(n)]

for i in range(n):
  e[i] = [int(x) for x in input().split()]

q = [[0,0]]
visited = set()
found = False
while q:
  node = q.pop()
  if tuple(node) in visited:
    continue
  elif node == [n-1,n-1]:
    found = True
    break
  else:
    visited.add(tuple(node))
    if node[0]>0 and abs(e[node[0]][node[1]] - e[node[0]-1][node[1]])<=h:
      q.append([node[0]-1,node[1]])
    if node[0]<n-1 and abs(e[node[0]][node[1]] - e[node[0]+1][node[1]])<=h:
      q.append([node[0]+1,node[1]])
    if node[1]>0 and abs(e[node[0]][node[1]] - e[node[0]][node[1]-1])<=h:
      q.append([node[0],node[1]-1])
    if node[1]<n-1 and abs(e[node[0]][node[1]] - e[node[0]][node[1]+1])<=h:
      q.append([node[0],node[1]+1])
if found:
  print('yes')
else:
  print('no')