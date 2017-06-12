import sys
input = sys.stdin.readline

nm=[int(x) for x in input().split()]
g = [[] for x in range(nm[0])]

for i in range(nm[1]):
  temp = [int(x) for x in input().split()]
  g[temp[0]-1].append(temp[1]-1)
  g[temp[1]-1].append(temp[0]-1)


visited = []
q = [0]

tracking = [-1 for x in range(nm[0])]
loop = False
loopcheck=[]
while(q):
  node = q.pop()
  if node not in visited:
    visited.append(node)
    
    for bond in g[node]:
      if tracking[node]!=bond:
        tracking[bond] = node
      q.append(bond)
  else:
    count = 0
    i=tracking[0]
    while(count<6):
      if i<0 or i>=nm[0]:
        #print('dank')
        count = 0
        break
      i = tracking[i]
      count+=1
      if i==tracking[0]:
        break
      
    #print(tracking)
    if count == 6:
      loop=True
      q=[]
      break
    #print(count)

if loop:
  print('YES')
else:
  print('NO')