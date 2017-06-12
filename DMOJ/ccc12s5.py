import sys
input = sys.stdin.readline

r, a = [int(i) for i in input().split()]
dp = [[-1 for i in range(r)]for j in range(a)]


for i in xrange(int(input())):
  temp = [int(x) for x in input().split()]
  dp[temp[1]-1][temp[0]-1]=0
rip = False
for i in xrange(r):
  if dp[0][i]==0:
    rip = True
  elif rip:
    dp[0][i]=0
  else:
    dp[0][i]=1

rip =False
for i in xrange(a):
  if dp[i][0]==0:
    rip = True
  elif rip:
    dp[i][0]=0
  else:
    dp[i][0] = 1

#print(dp)
for i in xrange(1,a):
  for j in xrange(1,r):
    if dp[i][j]==-1:
      dp[i][j]=dp[i-1][j]+dp[i][j-1]

print dp[a-1][r-1]