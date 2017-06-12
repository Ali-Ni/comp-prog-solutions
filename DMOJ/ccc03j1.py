import sys
input= sys.stdin.readline

inp=[int(input()) for i in range(3)]


out = ''
for i in range(inp[0]):
  for j in range(3):
    out+='*'
    if j<2:
      for w in range(inp[1]):
        out+=' '
  out+='\n'

out+='***'
for i in range(inp[1]*2):
  out+='*'
out+='\n'

for i in range(inp[2]):
  out+=' '
  for j in range(inp[1]):
    out+=' '
  out+='*\n'

print(out)