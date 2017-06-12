#include <iostream>
#include <map>
int main(){
	int n;
	scanf("%d",&n);
	
	std::map<int,int> m;
	int temp;
	
	for(int i=0;i<n;i++){
	  scanf("%d",&temp);
	  //if(m.find(temp)==m.end()){
	    //m[temp]=1;
	  //}else{
	    m[temp]++;
	  //}
	}
	std::map<int,int>::iterator it;
	for (it=m.begin();it!=m.end();it++){
	  if(it->second%2==1){
	    printf("%d\n",it->first);
	    break;
	  }
	}
}