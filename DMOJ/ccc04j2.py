import sys
input= sys.stdin.readline
inp = [int(input()) for i in range(2)]

while(inp[0]<=inp[1]):
  print('All positions change in year ' + str(inp[0]))
  inp[0]+=60