#include <iostream>
#include <cstring>

using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int maxLength = 0;
        int start = 0;
        
        //recorde whether the character is exist
        bool exist[256] = {false};
        //recorde the position where the character is
        int pos[256]={0};
        
        
        //if the character exists,start move to the position where the character last exist & the position refresh & clear the exist before the character
        for(int i=0; i<s.size(); i++)
        {
        	if(exist[s[i]]){
        		for(int j=start; j<=pos[s[i]]; j++){
        			exist[s[j]] = false;
				}
				exist[s[i]] = true;	
				start = pos[s[i]] + 1;
				pos[s[i]] = i;
				
			}else{
				exist[s[i]] = true;
				pos[s[i]] = i;
				maxLength = max(maxLength,i-start+1);
			}
		}
		return maxLength;
    }
};

int main(){
	
	return 0;
}
