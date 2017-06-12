from sys import stdin
input = stdin.readline

t = int(input())
pref = {}
for i in range(t):
  pref[input()] = i

n = int(input())
questions = []
for i in range(n):
  questions.append(tuple([pref[input()], i+1]))
  
questions.sort()

for q in questions:
  print(q[1])