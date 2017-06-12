import sys
input= sys.stdin.readline

d = [int(input()) for i in range(2)]

if d[0]>2:
  print("After")
elif d[0] <2:
  print("Before")
elif d[1]>18:
  print("After")
elif d[1] ==18:
  print("Special")
else:
  print("Before")