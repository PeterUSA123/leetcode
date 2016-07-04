#include <iostream>
#include <cstring>

using namespace std;
/*
* p[i][j]note that whether the string from i to j is palidrmoe
* the beginning is p[i][i] is true
* p[i][i+1] is true if s[i]==s[i+1]
* the after thing is that p[i][j] is true when p[i+1][j-1] is true and s[i]=s[j]
*/
class Solution {
public:
    string longestPalindrome(string s) {
    	int longestBegin = 0;
		int maxLen = 1;
		bool p[1000][1000] = {false}; 
		
		for(int i=0; i<s.size(); i++){
			p[i][i] = true;
		}
		
		for(int i=0; i<s.size()-1; i++){
			if(s[i]==s[i+1]){
				p[i][i+1] = true;
				longestBegin = i;
				maxLen = 2;
			}
		}
		
		for(int k=3; k<=s.size(); k++){
			for(int i=0; i<s.size()-k+1; i++){
				int j = i+k-1;
				if(p[i+1][j-1] && s[i]==s[j]){
					p[i][j] = true;
					longestBegin = i;
					maxLen = k;	
				}
			}
		}
		return s.substr(longestBegin,maxLen);
    }
};

int main(){
	
	return 0;
} 
