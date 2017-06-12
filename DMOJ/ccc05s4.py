import sys
input = sys.stdin.readline

l = int(input())

for case in range(l):
  
  g = [[]]
  n = int(input())
  depth = 0
  ihavefunplaying = ['' for i in range(n)]
  for i in range(n):
    ihavefunplaying[i] = input().strip()
  names = {}
  names[ihavefunplaying[-1]] = 0
  for i in range(n):
    name = ihavefunplaying[i]
    if name not in names:
      length = len(names)
      g[depth].append(length)
      g.append([])
      depth = length
      names[name] = length
    else:
      depth = names[name]
  #print(g)
  q = [[0]]
  maxdepth = 0
  visited = []
  while q:
    path = q.pop()
    if path[-1] in visited:
      continue
    else:
      visited.append(path[-1])
    #print(path)
    if g[path[-1]]:
      for child in g[path[-1]]:
        q.append(path+[child])
    else:
      maxdepth = max(maxdepth, len(path))
  
  efftime = 20*(maxdepth-1)
  print((10*n)-efftime)