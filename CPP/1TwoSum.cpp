#include <iostream>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

class Solution {
public:
	int findfirst(vector<int> nums, int key){
		for(int i=0; i<nums.size(); i++){
			if(nums[i]==key){
				return i+1;
			}
		}
	}
		
	int findlast(vector<int> nums, int key){
		for(int i=nums.size()-1; i>=0; i--){
			if(nums[i]==key){
				return i+1;
			}
		}
	}
	
    vector<int> twoSum(vector<int>& nums, int target) {
		
		vector<int> copy = nums;
		sort(nums.begin(),nums.end());
        
        vector<int> ans;
        int beg = 0;
        int end = nums.size()-1;
		while(beg<end){
			if(nums[beg]+nums[end]==target){
				ans.push_back(findfirst(copy,nums[beg]));
				ans.push_back(findlast(copy,nums[end]));
				sort(ans.begin(),ans.end());
				break; 
			}else if(nums[beg]+nums[end]>target){
				end--;
			}else{
				beg++;
			}
		}
		return ans;
    }
};
int main()
{
	vector<int> tc;
	tc.push_back(0); 
	tc.push_back(4); 
	tc.push_back(3); 
	tc.push_back(0); 

	int target=0;
	Solution S;
	
	vector<int> answer;
	answer =  S.twoSum(tc,target);
	
	for(int i=0; i<answer.size(); i++)
	{
		cout << answer[i] << " ";
	}
	cout << endl;
	return 0;
 } 
