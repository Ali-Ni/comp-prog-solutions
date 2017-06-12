import sys
input = sys.stdin.readline

v = [(0,-1),
    (0,-2),
    (0,-3),
    (1,-3),
    (2,-3),
    (3,-3),
    (3,-4),
    (3,-5),
    (4,-5),
    (5,-5),
    (5,-4),
    (5,-3),
    (6,-3),
    (7,-3),
    (7,-4),
    (7,-5),
    (7,-6),
    (7,-7),
    (6,-7),
    (5,-7),
    (4,-7),
    (3,-7),
    (2,-7),
    (1,-7),
    (0,-7),
    (-1,-7),
    (-1,-6),
    (-1,-5)
    ]

current = (-1,-5)
rekt = False
while True:
  inst = input().split()
  inst[1] = int(inst[1])
  if inst[0] == 'q':
    break
  elif inst[0] == 'u':
    for i in range(inst[1]):
      current = tuple([current[0],current[1]+1])
      if current in v:
        rekt = True
      else:
        v.append(current)
  elif inst[0] == 'd':
    for i in range(inst[1]):
      current = tuple([current[0],current[1]-1])
      if current in v:
        rekt = True
      else:
        v.append(current)
  elif inst[0] == 'l':
    for i in range(inst[1]):
      current = tuple([current[0]-1,current[1]])
      if current in v:
        rekt = True
      else:
        v.append(current)
  elif inst[0] == 'r':
    for i in range(inst[1]):
      current = tuple([current[0]+1,current[1]])
      if current in v:
        rekt = True
      else:
        v.append(current)
  out = str(current[0])+' ' +str(current[1])+ ' '
  if rekt:
    out+='DANGER'
    print(out)
    break
  else:
    out+='safe'
    print(out)