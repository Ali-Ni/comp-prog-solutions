#include <iostream>
#include <string>
using namespace std;


int main(){
    string text;
    string p;
    cin >> text;
    cin >> p;
    
    
    
    int m = text.length();
    int n = p.length();
    int b = (n>600000)?600000:n;
    int badchar[26][b]={-1};
    for (int i=0;i<26;i++){
        int a = -1;
        for (int j=0;j<b;j++){
            if (i+97 == p[j]){
                a = j;
            }
            badchar[i][j]=a;
        }
    }
    
    int out = -1;
    int skip = 0;
    int shift;
    for (int i =0;i<=m-n;i+=skip){
      
        skip = 0;
        for (int j=n-1;j>=0;j--){
          //printf("%c\n",text[i+j]);
            if (p[j]!=text[i+j]){
              try{
                shift = j-badchar[text[i+j]-97][j];
              }catch(...){
                shift = 1;
              }
                if (shift<0){
                    shift = 1;
                }
                skip = shift;
                break;
            }
        }
        if (skip==0){
            out = i;
            break;
        }
    }

    printf("%i\n", out);
}