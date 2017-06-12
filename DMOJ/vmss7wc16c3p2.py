import sys
input = sys.stdin.readline
n,m,a,b = [int(x) for x in input().split()]

g = [[] for i in range(n)]

for i in range(m):
  line = [int(x) for x in input().split()]
  g[line[0]-1].append(line[1]-1)
  g[line[1]-1].append(line[0]-1)

q = [a-1]

go = False
visited = []
while q:
  node = q.pop()
  if node == b-1:
    go = True
    break
  elif node in visited:
    continue
  else:
    visited.append(node)
    for child in g[node]:
      q.append(child)
if go:
  print('GO SHAHIR!')
else:
  print('NO SHAHIR!')