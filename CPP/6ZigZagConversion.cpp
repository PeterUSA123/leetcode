#include <iostream>
#include <cstring>

using namespace std;
class Solution {
public:
    string convert(string s, int numRows) {
    	if(numRows <=1 || s.size() ==0)
			return s;
		string ans="";
		int n= s.size();
		for(int i=0; i<n&&i<numRows; i++){
			int index = i;
			ans += s[index];
			for(int j=1; index<n; j++){
				if(i==0 || i==numRows-1){
					index += 2*numRows -2;
				}else{
					if(j%2!=0){
						index += 2*(numRows-1-i);
					}else{
						index += 2*i;
					}
				}
				
				if(index < n){
					ans += s[index];
				}
			}
		}
		return ans;    
    }
};


int main(){
	return 0;
} 
