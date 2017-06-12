#include <iostream>

using namespace std;

int main(){
  int k, m, n;
  scanf("%d", &k);
  for (int _=0;_<k;_++){

    scanf(" %d %d", &m, &n);
    int grid[m][n]={0};
    for(int i=0;i<m;i++){
      for(int j=0;j<n;j++){
        char temp;
        scanf(" %c", &temp);
        if (temp == 'F'){
          if (i!=0){
            grid[i][j]=grid[i-1][j]+1;
          }else{
            grid[i][j]=1;
          }
        }else{
          grid[i][j]=0;
        }
      }
    }
    int maxsize = 0;
    for(int i=0;i<m;i++){
      for(int j=0;j<n;j++){
        int left = j;
        int right = j;
        if(grid[i][j]==0 || (j!=0 && grid[i][j]==grid[i][j-1] )){
          continue;
        }
        while(grid[i][left-1]>=grid[i][j] && left>0){
          left--;
        }
        
        while(right<n-1 && grid[i][right+1]>=grid[i][j]){
          right++;
        }
        int temp = (right-left+1)*grid[i][j]*3;
        if (temp>maxsize){
          maxsize =temp;
        }
      }
    }
    printf("%d\n", maxsize);
  }
}