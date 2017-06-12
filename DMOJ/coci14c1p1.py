#import sys
#input = sys.stdin.readline

n=int(input())
#print(n)
s = [int(x) for x in input().split()]
#print(s)
total = 0
out = ''
last = 0
for i in range(n):
  temp = int(s[i]*(i+1))
  out+=str(temp-last)
  last = temp
  if i<n-1:
    out+=' '
    
print(out)