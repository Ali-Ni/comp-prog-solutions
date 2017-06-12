import sys
#input = sys.stdin.readline
n = int(input())
fac = []
for i in range(int(input())):
  fac.append(int(input()))
  
m=[float('inf') for i in range(n+1)]
for i in fac:
  m[i]=1

q = [fac[0],fac[1],fac[2]]

while q:
  x=q.pop(0)
  for p in fac: 
    if x+p<=n and m[x+p]>m[x]+1:
      m[x+p] = m[x]+1
      q.append(x+p)

if m[n]==float('inf'):
  print('Roberta acknowledges defeat.')
else:
  print('Roberta wins in '+ str(m[n]) + ' strokes.')