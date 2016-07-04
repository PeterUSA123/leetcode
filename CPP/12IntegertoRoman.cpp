#include <iostream>
#include <cstring>

using namespace std;

class Solution {
public:
    string intToRoman(int num) {
    	int val[13]={1000,900,500,400,100,90,50,40,10,9,5,4,1};
    	string sval[13]={"M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"};
    	string ans="";
    	for(int i=0; i<13; i++){
    		while(num>=val[i]){
    			num -= val[i];
    			ans.append(sval[i]);
    			cout << sval[i] << endl;
			}
			
		}
		return ans;
    }
};

int main(){
	Solution s;
	cout << s.intToRoman(1) << endl;
	
	return 0;
}
