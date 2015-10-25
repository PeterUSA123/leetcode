#include <iostream>
#include <cmath>

using namespace std;

class Solution {
public:
    int reverse(int x) {
    	long long ans=0;
    	const int max = 0x7fffffff;    
        const int min = 0x80000000;   
		while(x!=0){
			ans = ans*10 + x%10;
			if(ans > max || ans < min){
				return 0;
			}
			x /= 10;
		}
		return ans;    
    }
};

int main(){
	Solution s;
	cout << s.reverse(123) << endl;
	cout << s.reverse(-12) << endl;
	cout << s.reverse(100) << endl;
	cout << s.reverse(1534236469) << endl;
	cout << 0x7fffffff << " " <<  0x80000000 << endl; 
	return 0;
}
