import sys
input = sys.stdin.readline

n = int(input())
k = round(n+0.1)
grades = []
for i in range(n):
  grades.append(int(input()))
  
grades.sort()

if n%2==0:
  med = int(n/2)
  out = int(round(((grades[med]+grades[med-1])/2)+0.01))
else:
  med = int(n/2)
  out = grades[med]

print(out)