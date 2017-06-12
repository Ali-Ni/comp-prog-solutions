import sys, bisect
input = sys.stdin.readline

m = [0, 990, 1010, 1970, 2030, 2940, 3060, 3930, 4060, 4970, 5030, 5990, 6010, 7000]
a = int(input())
b = int(input())

for i in range(int(input())):
  bisect.insort(m, int(input()))
m.sort()
paths = 0
def nextmotel(dist):
  if m[dist] == 7000:
    global paths
    paths +=1
  else:
    n = dist+1
    #print(n)
    while n<len(m) and m[n]-m[dist]<a:
      n+=1
    while n<len(m) and m[n]-m[dist]<=b:
      nextmotel(n)
      n+=1

if a>b:
  pass
else:
  nextmotel(0)
print (paths)