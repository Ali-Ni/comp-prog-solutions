import sys
input = sys.stdin.readline

for case in range(10):
  if input().strip() == 'encode':
    line = input().strip().split()
    code = ''
    for i in range(len(max(line,key=len))):
      for word in line:
        if i>=len(word):
          continue
        else:
          code+=word[i]
    out = ''
    count = 0
    for i in range(len(line)):
      out+=code[count:count+len(line[i])] + ' '
      count +=len(line[i])
    print (out)
  
  else:
    line = input().strip().split()
    decode = ['' for word in line]
    counter = 0
    for word in line:
      for char in word:
        while len(line[counter])==len(decode[counter]):
          counter+=1
          if counter==len(line):
            counter = 0
        decode[counter] +=char
        counter+=1
        if counter==len(line):
          counter = 0
    print(' '.join(decode))