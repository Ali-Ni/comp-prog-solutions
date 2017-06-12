import sys
#input = sys.stdin.readline
n = int(input())

fac = [int(x) for x in input().split()]

m=[0 for i in range(n+1)]
m[fac[0]]=1
m[fac[1]]=1
m[fac[2]]=1

q = [fac[0],fac[1],fac[2]]

while q:
  x=q.pop()
  for p in fac: 
    if x+p<=n and m[x+p]<m[x]+1:
      m[x+p] = m[x]+1
      q.append(x+p)

#print(m)
print(m[n])