import sys
input= sys.stdin.readline

a = int(input())
e = int(input())

names = ['TroyMartian','VladSaturnian', 'GraemeMercurian']
bools = [False for i in range(3)]

if a>=3 and e<=4:
  bools[0] = True
if a<=6 and e>=2:
  bools[1]=True
if a<=2 and e<=3:
  bools[2]=True

for i in range(3):
  if bools[i]:
    print(names[i])