import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

if n<k:
  need = k-n
else:
  need = min(n%k,k-(n%k))

print(need)