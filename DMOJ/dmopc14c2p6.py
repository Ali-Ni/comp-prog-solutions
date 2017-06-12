from sys import stdin
input = stdin.readline

n = int(input())
trees = [int(x) for x in input().split()]
treesort = [(trees[i], i+1) for i in range(n)]
treesort.sort()

#print(trees)
#print(treesort)

parent = {}
for i in range(1, n+1):
  parent[i] = i&(i-1)


queries = []
numq = int(input())
for _ in range(numq):
  a, b, q = [int(x) for x in input().split()]
  queries.append((q, a, b, _))
queries.sort()
#print(queries)

fenwick = [0 for i in range(n+1)]
mintree = 0

def traverse(k):
  out = 0
  while k!=0:
    out+=fenwick[k]
    k=parent[k]
  return out

output = [0 for i in range(numq)]

rekt = False
while queries:
  q, a, b, ind = queries.pop()
  if not rekt:
    mintree = treesort[-1][0]
  #print(q, mintree, ind)
  while q<=mintree and not rekt:
    v, i = treesort.pop()
    while i<n+1:
      fenwick[i]+=v
      i += (((~i)+1)&i)
    if not treesort:
      rekt = True
      mintree = float('inf')
    else:
      mintree = treesort[-1][0]
  
  output[ind] = traverse(b+1)-traverse(a)



for ans in output:
  print(ans)