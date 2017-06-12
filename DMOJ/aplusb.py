import sys
all_data = sys.stdin.read().split('\n')

for i in range(1,int(all_data[0])+1):
  j = all_data[i].split()
  print(int(j[0])+int(j[1]))