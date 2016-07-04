#include <iostream>
#include <cstring>
#include <map>

using namespace std;

class Solution {
public:
    int romanToInt(string s) {
    	int ans = toNum(s[0]);
    	for(int i=1;i<s.size(); i++){
    		if(toNum(s[i-1])<toNum(s[i])){
    			ans += toNum(s[i]) - 2*toNum(s[i-1]);
			}else{
				ans += toNum(s[i]);
			}
		}
		return ans;
    }
    
    int toNum(char c){
    	switch(c){
    		case 'I':return 1;
    		case 'V':return 5;
    		case 'X':return 10;
    		case 'L':return 50;
    		case 'C':return 100;
    		case 'D':return 500;
    		case 'M':return 1000;
    	}
	}
};

int main(){
	return 0;
}
