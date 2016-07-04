#include <iostream>
#include <vector>
#include <cmath>

using namespace std;
/* ³¬Ê± 
class Solution {
public:
    int maxArea(vector<int>& height) {
    	int p[4000]={0};	
    	p[1] = min(height[0],height[1]);
    	for(int i=2; i<height.size(); i++){
    		int tmp = p[i-1];
    		for(int j=i-1; j>=0; j--){
    			if(tmp < min(height[j],height[i])*(i-j)){
    				tmp = min(height[j],height[i])*(i-j);
				}
			}
			p[i] = tmp;
		}
		return p[height.size()-1];
    }
};
*/
class Solution {
public:
    int maxArea(vector<int>& height) {
    	int left = 0;
		int right = height.size()-1;
		int ans = 0;
		while(left < right){
			int tmp = min(height[left],height[right])*(right-left);
			if(ans < tmp){
				ans = tmp;
			}
			if(height[left]<height[right]){
				left++;
			}else{
				right--;
			}
		}    
		return ans;
    }
};

int main(){
	Solution s;
	vector<int> v;
	v.push_back(1);
	v.push_back(2);
	v.push_back(1);
	cout << s.maxArea(v) << endl; 
	return 0; 
}
