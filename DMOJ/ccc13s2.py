import sys
input = sys.stdin.readline

maxw = int(input())
n = int(input())
weights = [0 for i in range(n)]

for i in range(n):
  weights[i] = int(input())
#print(weights)
out = 0

total = 0
for i in range(len(weights)):
  total+=weights[i]
  if i>=4:
    total-=weights[i-4]
  #print(total)
  if total<=maxw:
    out+=1
  else:
    break
print(out)