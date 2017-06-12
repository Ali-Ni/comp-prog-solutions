import sys
input = sys.stdin.readline

n=int(input())
g= [[] for i in range(n)]
for i in range(n-1):
  g[int(input())-1].append(i)
#print(g)
def branchtotal(g, i):
  total = 1
  for branch in g[i]:
    #print(branch)
    total *= branchtotal(g,branch)
  return total +1

print(branchtotal(g,n-1)-1)