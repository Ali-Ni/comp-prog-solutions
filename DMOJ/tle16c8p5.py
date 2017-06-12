import sys
from collections import defaultdict, deque
input = sys.stdin.readline

n, m = [int(x) for x in input().split()]
possibilities = [int(x)+n for x in input().split()][1:]

g = defaultdict(list)
for _ in range(2,n+1):
  line = [int(x)+n for x in input().split()][1:]
  for each in line:
    if each in possibilities:
      g[_].append(each)


matching = defaultdict(int)


for k,v in g.items():
  for i in v:
    if i not in matching:
      matching[k]=i
      matching[i]=k
      break
unmatched = [i for i in g if i not in matching]
remaining = []
remaining = [i for i in possibilities]
for k,v in matching.items():
  if v in remaining:
    remaining.remove(v)

#print(g)
#print(matching)
#print(unmatched)
#print(remaining)


def aug(path, tree, m, u, r):
  for i in range(len(path)):
    j = (i+1)%len(path)
    if i%2==0:
      m[path[i]]=path[j]
      m[path[j]]=path[i]
      if path[i] in r:
        r.remove(path[i])
      if path[j] in u:
        u.remove(path[j])
  for k,v in tree.items():
    if k not in path:
      new = [i for i in v if i not in path]
      tree[k]=new
  marked = []
  for k,v in tree.items():
    if len(v)==0:
      marked.append(k)
  for each in marked:
    tree.pop(each)
  return m, tree, u, r




while unmatched:
  augpaths = defaultdict(list)
  #print(dict(matching))
  #print(unmatched)
  q = deque()
  for each in unmatched:
    q.extend([(each, None, 1)])
  nextlevel = float('inf')
  while q:
    u, p, _ = q.popleft()
    if _>= nextlevel:
      break
    elif matching[u]==p or p==None:
      for e in g[u]:
        if matching[e]!= u and u not in augpaths[e]:
          if e in remaining:
            nextlevel = _+1
          augpaths[e].append(u)
          #augpaths[u].append(e)
          q.extend([(e, u,_+1)])
    elif u not in augpaths[matching[u]]:
      if matching[u] in remaining:
        nextlevel = _+1
      augpaths[matching[u]].append(u)
      #augpaths[u].append(matching[u])
      q.extend([(matching[u],u,_+1)])
  
  pathfound = False
  for each in remaining:
    if each not in augpaths:
      continue
    q = [[each]]
    visited = set()
    
    while q:
      node = q.pop()
      #print(node)
      if node[-1] in visited:
        continue
      if node[-1] in unmatched:
        pathfound = True
        matching, augpaths, unmatched, remaining = aug(node, augpaths, matching, unmatched, remaining)
        break
      else:
        visited.add(node[-1])
        for child in augpaths[node[-1]]:
          q.append(node+[child])
  
  if not pathfound:
    break
        
#print(matching) 
print(len(remaining))
#print(remaining)