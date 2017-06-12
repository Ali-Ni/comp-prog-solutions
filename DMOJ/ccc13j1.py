import sys
input= sys.stdin.readline
ages = [int(input().strip()) for i in range(2)]

print(ages[1]+(ages[1]-ages[0]))