import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

dp = [[0 for i in range(n)] for j in range(k)]
dp[0] = [1 for i in range(n)]
for i in range(1,k):
  #for line in dp:
   # print(line)
  #print()
  dp[i][i] = 1
  for j in range(i+1, n):
    dp[i][j] = dp[i-1][j-1]+dp[i][j-i-1]

print(dp[k-1][n-1])