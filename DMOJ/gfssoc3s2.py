from sys import stdin
from collections import deque
input = stdin.readline

r, c = [int(x) for x in input().split()]

grid = []

for _ in range(r):
  grid.append(list(input().strip()))

for i in range(r):
  if 'X' in grid[i]:
    dest = (i, grid[i].index('X'))
    grid[i][dest[1]] = '.'
  if 'B' in grid[i]:
    box = (i, grid[i].index('B'))
    grid[i][box[1]] = '.'
  if 'P' in grid[i]:
    start = (i, grid[i].index('P'))
    grid[i][start[1]] = '.'
q = deque()
visited = set()
try:
    q.append([start, box, 0])
except NameError:
    pass
ans = -1

while q:
  p,b,d = q.popleft()
  if (p,b) in visited:
    continue
  elif b == dest:
    ans = d
    break
  else:
    visited.add((p,b))
    if p[0]>0 and grid[p[0]-1][p[1]]!='#':#up
      np = (p[0]-1,p[1])
      if b == np:
        if b[0]>0 and grid[b[0]-1][b[1]]!='#':
          q.append([np, (b[0]-1,b[1]), d+1])
      else:
        q.append([np, b, d+1])
    if p[0]<r-1 and grid[p[0]+1][p[1]]!='#':#down
      np = (p[0]+1,p[1])
      if b == np:
        if b[0]<r-1 and grid[b[0]+1][b[1]]!='#':
          q.append([np, (b[0]+1,b[1]), d+1])
      else:
        q.append([np, b, d+1])
    if p[1]>0 and grid[p[0]][p[1]-1]!='#':#left
      np = (p[0],p[1]-1)
      if b == np:
        if b[1]>0 and grid[b[0]][b[1]-1]!='#':
          q.append([np, (b[0],b[1]-1), d+1])
      else:
        q.append([np, b, d+1])
    if p[1]<c-1 and grid[p[0]][p[1]+1]!='#':
      np = (p[0],p[1]+1)
      if b == np:
        if b[1]<c-1 and grid[b[0]][b[1]+1]!='#':
          q.append([np, (b[0],b[1]+1), d+1])
      else:
        q.append([np, b, d+1])
    
print ans