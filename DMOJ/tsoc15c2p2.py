import sys
input = sys.stdin.readline

h = int(input())

t = int(h/2)
a = []
a.append(''.join(['*' for i in range(h)]))
for i in range(t):
  a.append(''.join(['*' for i in range(t-i)]) + ''.join([' ' for i in range((2*i)+1)]) + ''.join(['*' for i in range(t-i)]))

print('\n'.join(a[:-1])+'\n'+'\n'.join(reversed(a)))