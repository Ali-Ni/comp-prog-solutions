import sys
input = sys.stdin.readline

n = int(input())
possibilities = set()
twin = False
for i in range(n):
  line = tuple(sorted([int(x) for x in input().split()]))
  if line in possibilities:
    twin = True
    break
  else:
    possibilities.add(line)

if twin:
  print('Twin snowflakes found.')
else:
  print('No two snowflakes are alike.')