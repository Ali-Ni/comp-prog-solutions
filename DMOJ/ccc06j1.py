import sys
input= sys.stdin.readline

food=[[461,431,420,0],[100,57,70,0],[130,160,118,0],[167,266,75,0]]

inp = [int(input())-1 for i in range(4)]

s=0
for i in range(len(inp)):
  s+=food[i][inp[i]]

print("Your total Calorie count is "+str(s)+".")