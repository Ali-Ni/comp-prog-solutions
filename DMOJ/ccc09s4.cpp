#include <iostream>
#include <algorithm>
#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <deque>
#include <vector>
#define scan(x) do{while((x=getchar())<'0'); for(x-='0'; '0'<=(_=getchar()); x=(x<<3)+(x<<1)+_-'0');}while(0)
char _;
using namespace std;


typedef pair<int,int> xd;


int main(){
  int n, t, x, y, c, k, s;
  scanf("%d%d", &n, &t);
  int routes[n][n] = {-1};
  vector<vector<int>> list;
  list.resize(n);
  for(int i=0;i<t;i++){
    scan(x);
    scan(y);
    scan(c);
    x = x-1;
    y = y-1;
    routes[x][y] = c;
    routes[y][x] = c;
    list[x].push_back(y);
    list[y].push_back(x);
  }
  scanf("%d", &k);
  unordered_map<int,int> pencils;
  for (int i=0;i<k;i++){
    scanf("%d%d", &x, &y);
    pencils[x-1] = y;
  }
  
  scanf("%d", &s);
  priority_queue<xd, deque<xd>, greater<xd>> q;
  q.push(make_pair(0, s-1));

  int minval = 2100000000;
  unordered_set<int> visited;
  
  while(!q.empty()){
    xd node = q.top();
    q.pop();
    //printf("%d %d\n", node.first, node.second);
    if (node.first>=minval){
      break;
    }
    if (visited.count(node.second)){
      continue;
    }
    visited.insert(node.second);
    if(pencils.find(node.second)!=pencils.end()){
      k-=1;
      if (node.first+pencils[node.second]<minval){
        minval = node.first+pencils[node.second];
      }
    }
    if(k==0){
      break;
    }
    for(int i = 0;i<list[node.second].size();i++){
      if(visited.count(list[node.second][i])==0){
        //printf("%d %d\n", node.first+routes[node.second][i], list[node.second][i]);
        q.push(make_pair(node.first+routes[node.second][list[node.second][i]],list[node.second][i]));
      }
    }
  }
  printf("%d\n", minval);
}