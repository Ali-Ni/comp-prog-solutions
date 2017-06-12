import sys
input = sys.stdin.readline

c = int(input())
a=[]
for i in range(c):
  temp = input().split()
  temp[0]=int(temp[0])
  #print(temp)
  if temp[0] == 1:
    if temp[1] in a:
      print('false')
    else:
      print('true')
      a.append(temp[1])
  elif temp[0] == 2:
    if temp[1] in a:
      print('true')
      a.remove(temp[1])
    else:
      print('false')
  elif temp[0] == 3:
    if temp[1] in a:
      print(a.index(temp[1]))
    else:
      print('-1')
  else:
    out= ''
    if len(a) == 2:
      print('false true')
    elif len(a) == 1:
      print(a[0])
    else:
      print('')