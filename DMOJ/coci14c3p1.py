#import sys
#input = sys.stdin.readline

d = {}
for key in ['1', 'Q', 'A','Z']:
    d[key] = 0
for key in ['2', 'W','S','X']:
    d[key] = 1
for key in ['3', 'E','D','C']:
    d[key] = 2
for key in ['4', 'R','F','V','5','T','G','B']:
    d[key] = 3
for key in ['6', 'Y','H','N','7','U','J','M']:
    d[key] = 4
for key in ['8', 'I','K',',']:
    d[key] = 5
for key in ['9', 'O','L','.']:
    d[key] = 6
for key in ['0', 'P',';','/','-','=','[',']','\'']:
    d[key] = 7
out = [0 for i in range(8)]

for char in input():
  out[d[char]]+=1
for i in range(8):
  print(out[i])