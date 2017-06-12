import sys
input = sys.stdin.readline

def cyclecheck(cycle, a):
  while(len(a)>=len(cycle)):
    if a[:len(cycle)]==cycle:
      a=a[len(cycle):]
    else:
      return False
  return bool(a==cycle[:len(a)])



while True:
  line = [int(x) for x in input().split()]
  if line[0]==0:
    break
  else:
    changes = []
    if len(line)==2:
      print(0)
    else:
      for i in range(2,len(line)):
        changes.append(line[i]-line[i-1])
      #print(changes)
      for i in range(1,len(changes)+1):
        #print(i)
        if cyclecheck(changes[:i],changes):
          print(i)
          break