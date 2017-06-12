import sys
input = sys.stdin.readline

n, t = [int(x) for x in input().split()]

names = {}
names['home'] = 0
names['Waterloo GO'] = n+1
g = [[] for i in range(n+2)]
for i in range(n):
  names[input().strip()] = i+1

for i in range(t):
  temp = [x.strip() for x in input().split('-')]
  g[names[temp[0]]].append(names[temp[1]])
  g[names[temp[1]]].append(names[temp[0]])

minpath = float('inf')
q = [[0]]

while q:
  node = q.pop(0)
  #print(node)
  if len(node)>=minpath:
    continue
  elif node[-1] == n+1:
    minpath = len(node)
  else:
    for child in g[node[-1]]:
      if child not in node:
        q.append(node+[child])
#print(names)
#print(g)
if minpath == float('inf'):
  print('RIP ACE')
else:
  print(minpath-1)


#print(g)