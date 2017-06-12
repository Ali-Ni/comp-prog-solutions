import sys
input = sys.stdin.readline

g=[[] for i in range(26)]
alph = {
  'A':0,
  'B':1,
  'C':2,
  'D':3,
  'E':4,
  'F':5,
  'G':6,
  'H':7,
  'I':8,
  'J':9,
  'K':10,
  'L':11,
  'M':12,
  'N':13,
  'O':14,
  'P':15,
  'Q':16,
  'R':17,
  'S':18,
  'T':19,
  'U':20,
  'V':21,
  'W':22,
  'X':23,
  'Y':24,
  'Z':25
}
text = []
while(True):
  temp = input().strip()
  if temp == '**':
    break
  else:
    text.append(temp)
    g[alph[temp[0]]].append(alph[temp[1]])
    g[alph[temp[1]]].append(alph[temp[0]])
#print(g)
#q = [0]
#visited = []
#tracking = []
paths = []

def findpath(path, graph, vis):
  #print(path)
  if path[-1] == 1:
    paths.append([sorted((path[x],path[x+1])) for x in range(len(path)-1)])
  elif path[-1] not in vis:
    newvis = vis+[path[-1]]
    for child in graph[path[-1]]:
      new = path+[child]
      findpath(new, g, newvis)

findpath([0], g, [])

#print(paths)
strat = paths[0]
paths=list(map(list,map(lambda x:map(tuple,x), paths)))
roads = set.intersection(*map(set, paths))
#print(roads)
revalph = dict([(v,k) for k,v in alph.items()])

for con in roads:
  out = revalph[con[0]]+revalph[con[1]]
  if out not in text:
    reversed(out)
  print(out)

print('There are ' + str(len(roads)) + ' disconnecting roads.')