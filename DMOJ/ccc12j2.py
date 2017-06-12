import sys
input= sys.stdin.readline
fish = [int(input()) for i in range(4)]

if fish[0]==fish[1]==fish[2]==fish[3]:
  print('Fish At Constant Depth')
elif fish[3]>fish[2]>fish[1]>fish[0]:
  print('Fish Rising')
elif fish[3]<fish[2]<fish[1]<fish[0]:
  print('Fish Diving')
else:
  print('No Fish')