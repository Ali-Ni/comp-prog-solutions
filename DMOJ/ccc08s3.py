import sys
input = sys.stdin.readline

for case in range(int(input())):
  rows = int(input())
  columns = int(input())
  m = [['' for i in range(columns)] for j in range(rows)]
  for i in range(rows):
    line = input()
    for j in range(columns):
      m[i][j] = line[j]

  q = [[0,0,1]]
  dp = [[float('inf') for i in range(columns)] for j in range(rows)]
  minpath = float('inf')
  #prev = {}
  while q:
    node = q.pop()
    val = m[node[0]][node[1]]
    #print(node)
    if val == '*' or node[2]>=minpath or dp[node[0]][node[1]]<=node[2]:
      continue
    elif node[:2] == [rows-1,columns-1]:
      minpath = min(minpath,node[2])
    elif val == '|' or val == '+':
      if node[0]>0:
        q.append([node[0]-1,node[1],node[2]+1])
      if node[0]<rows-1:
        q.append([node[0]+1,node[1],node[2]+1])
    if val == '-' or val == '+':
      if node[1]>0:
        q.append([node[0],node[1]-1,node[2]+1])
      if node[1]<columns-1:
        q.append([node[0],node[1]+1,node[2]+1])
    dp[node[0]][node[1]] = node[2]
  if minpath == float('inf'):
    print(-1)
  else:
    print(minpath)