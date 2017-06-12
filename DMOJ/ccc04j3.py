n = int(input())
m = int(input())
b = []
e = []
for i in range(n):
    b.append(input().strip())
for i in range(m):
    e.append(input().strip())

for s in b:
    for n in e:
        print(s + ' as ' + n)