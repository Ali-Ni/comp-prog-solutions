import sys
input= sys.stdin.readline

temp =input().strip()
consonants='bcdfghjklmnpqrstvwxz'

while temp != 'quit!':
  if len(temp)<=4 or temp[-2:] != 'or' or temp[-3] not in consonants:
    print(temp)
  else:
    out = temp[:-1]
    out+= 'u'
    out+='r'
    print(out)
  
  temp=input().strip()