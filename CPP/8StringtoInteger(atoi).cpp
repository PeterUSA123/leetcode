#include <iostream>
#include <cstring>

using namespace std;

class Solution {
public:
    int myAtoi(string str) {
        if(str.size()==0){
        	return 0;
        }
        const int maxInt = 0x7fffffff;    
        const int minInt = 0x80000000; 
        string cpy="";
        bool key = true;
        for(int i=0; i<str.size(); i++){
        	if(str[i]==' '&&key){
        		continue;
        	}else{
        		key = false;
				cpy += str[i];
        	}
        }
        long long ans = 0;
        int flag = 1;
        if(cpy[0]=='-'){
        	flag = -1;
        }else if(cpy[0]=='+'){
        	flag = 1;
        }else if((cpy[0]-'0')>=0 && (cpy[0]-'0')<=9){
        	ans =cpy[0]-'0';
        }else{
        	return 0;
        }
        for(int i=1; i<cpy.size(); i++){
        	if((cpy[i]-'0')>=0 && (cpy[i]-'0')<=9){
				ans = ans*10 + (cpy[i]-'0');
				if(ans>maxInt){
					break;
				}
			}else{
				break;
			}
        }
        ans *=flag;
		if(ans>maxInt || ans<minInt){
			ans = ans>0?maxInt:minInt;
		}	
		return ans;
    }
};

int main(){
	Solution s;
	cout << s.myAtoi("9223372036854775809")<< endl;
	cout << s.myAtoi("-2147483648") << endl;
	
	return 0;
}
