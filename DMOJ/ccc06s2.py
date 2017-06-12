import sys
all_data = sys.stdin.read().split('\n')

i = 0
cipher = {}
for char in all_data[1]:
  cipher[char] = all_data[0][i]
  i+=1

out=''

for char in all_data[2]:
  try:
    out += cipher[char]
  except:
    out += '.'

print(out);