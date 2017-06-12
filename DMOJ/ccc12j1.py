import sys
input= sys.stdin.readline

d = float(input())-float(input())

if d>=0:
  print("Congratulations, you are within the speed limit!")
else:
  if d<=-31:
    fine = 500
  elif d<=-21:
    fine = 270
  else:
    fine = 100
  print("You are speeding and your fine is $"+str(fine)+".")