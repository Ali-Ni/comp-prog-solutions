from sys import stdin
from re import finditer
input = stdin.readline

def subcheck(s):
  if len(s)==0:
    return False
  if s[0] == 'A':
    if len(s)==1:
      return True
    elif len(s)==2:
      return False
    elif s[1] == 'N':
      return subcheck(s[2:])
    else:
      return False
  elif s[0] == 'B':
    possible = False
    indices = [m.start() for m in finditer('S', s)]
    
    for i in indices:
      if i+1==len(s):
        possible = subcheck(s[1:-1])
      elif len(s)>i+2 and s[i+1] == 'N':
        possible = subcheck(s[1:i]) and subcheck(s[i+2:])
      if possible:
        return True
        break
      
  else:
    return False



while True:
 temp = input().strip()
 if temp == 'X':
   break
 else:
  if subcheck(temp):
    print('YES')
  else:
    print('NO')