import sys
input = sys.stdin.readline

n = int(input())
g={}
for i in range(n):
  temp = [int(x)-1 for x in input().split()]
  g[temp[0]]=temp[1]

while True:
  temp = [int(x)-1 for x in input().split()]
  if temp[0]==-1:
    break
  else:
    try:
      q=g[temp[0]]
    except KeyError:
      print('No')
      continue
    sep=0
    same = False
    visited = [temp[0]]
    while q not in visited:
      #print(q)
      sep+=1
      if q==temp[1]:
        same = True
        break
      else:
        try:
          q=g[q]
        except KeyError:
          break
    if same:
      print('Yes '+str(sep-1))
    else:
      print('No')