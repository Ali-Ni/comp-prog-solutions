import sys
input= sys.stdin.readline
bmi = (int(input().strip())/(float(input().strip())**2))

if bmi>25:
  print("Overweight")
elif bmi<18.5:
  print("Underweight")
else:
  print("Normal weight")