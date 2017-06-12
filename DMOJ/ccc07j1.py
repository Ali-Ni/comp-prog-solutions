import sys
input= sys.stdin.readline
bowls = [int(input().strip()) for i in range(3)]

print(sorted(bowls)[1])