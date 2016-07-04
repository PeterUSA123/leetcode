#include<iostream>
#include<cstring>

using namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
    	string tmp="";
    	if(x<0){
    		return false;
    	}
		while(x!=0){
			tmp += char(x%10+'0');
			x /=10;
		}
		for(int i=0; i<tmp.size()/2; i++){
			if(tmp[i]!=tmp[tmp.size()-1-i]){
				return false;
			}
		}
		return true;    
    }
};

int main(){
	
	return 0;
}
