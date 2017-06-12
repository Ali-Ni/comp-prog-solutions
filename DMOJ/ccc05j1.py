import sys
input= sys.stdin.readline

mins = [int(input()) for i in range(3)]

lel = lambda x: (abs(x)+x)/2
A=round(((lel(mins[0]-100)*0.25) + (mins[1]*0.15) + (mins[2]*0.20)),2)
B=round(((lel(mins[0]-250)*0.45) +(mins[1]*0.35)+(mins[2]*0.25)),2)

print("Plan A costs " + str(A))
print("Plan B costs " + str(B))

if A==B:
  print("Plan A and B are the same price.")
elif A<B:
  print("Plan A is cheapest.")
else:
  print("Plan B is cheapest.")