#include <iostream>
#include <cstring>

using namespace std;

class Solution {
public:
    bool isMatch(string s, string p) {
    	if(p.size()==0){
    		return s.size() == 0;
		}
		if(p.size()==1){
			return (s.size()==1&&(s[0]==p[0] || p[0]=='.'));
		}
		if(p[1]!='*'){
			if(s.size()==0){
				return false;
			}else{
				return (s[0]==p[0] || p[0]=='.') && isMatch(s.substr(1),p.substr(1));
			}
		}else{
			while(s.size()>0 && (p[0]==s[0] || p[0]=='.')){
				if(isMatch(s,p.substr(2))){
					return true;
				}
				s = s.substr(1);
			}
			return isMatch(s,p.substr(2));
		}
    }
};

int main(){
	return 0;
}
