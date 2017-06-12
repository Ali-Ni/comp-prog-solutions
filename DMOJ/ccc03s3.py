import sys
from collections import Counter
input = sys.stdin.readline

f = int(input())
r = int(input())
c = int(input())
#print(f)
p = [[1 for i in range(c)] for j in range(r)] 
rooms = [[0 for i in range(c)] for j in range(r)] 
for w in range(r):
  line = input()
  for k in range(c):
    if line[k]=='.':
      p[w][k]=0
    else:
      rooms[w][k] = -1
#print(p)
def sameroom(i,j,n):
  if i>=0 and i<r and j>=0 and j<c and p[i][j] == 0 and rooms[i][j]!=n:
    rooms[i][j] = n
    sameroom(i+1,j,n)
    sameroom(i-1,j,n)
    sameroom(i,j+1,n)
    sameroom(i,j-1,n)

end = False
roomnum =1
while not end:
  a,b = 0,0
  while 0 not in p[a] or 0 not in rooms[a]:
    a+=1
    if a>r-1:
      end = True
      break
  while not end and (p[a][b]!=0 or rooms[a][b]!=0):
    b+=1
  
  sameroom(a,b,roomnum)
  #for line in rooms:
    #print(line)
  #print()
  roomnum+=1
combined = []

for l in rooms:
  combined+=l

roomsizes = Counter(combined)

out = 0
#print(f)
#print( roomsizes.most_common())
for r in roomsizes.most_common():
  if r[0]==-1:
    continue
  elif f>=r[1]:
    f=f-r[1]
    #print(f)
    out+=1
  else:
    break

if out == 1:
  print('1 room, '+str(f)+' square metre(s) left over')
else:
  print(str(out)+' rooms, '+str(f)+' square metre(s) left over')