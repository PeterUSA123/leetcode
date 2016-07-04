class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        vector<int> merge;
        if(nums1.size()==0 && nums2.size()==0){
        	return 0;
        }
		if(nums1.size()==0){
			for(int i=0; i<nums2.size(); i++){
				merge.push_back(nums2[i]);
			}
		}else if(nums2.size()==0){
			for(int i=0; i<nums1.size(); i++){
				merge.push_back(nums1[i]);
			}
		}else{
			if(nums1[0]>=nums2[nums2.size()-1]){
				for(int i=0; i<nums2.size(); i++){
					merge.push_back(nums2[i]);
				}
				for(int i=0; i<nums1.size(); i++){
					merge.push_back(nums1[i]);
				}
			}else if(nums2[0]>=nums1[nums1.size()-1]){
				for(int i=0; i<nums1.size(); i++){
					merge.push_back(nums1[i]);
				}
				for(int i=0; i<nums2.size(); i++){
					merge.push_back(nums2[i]);
				}
			}else{
				int i=0, j=0;
				while(i<nums1.size() && j<nums2.size()){
					if(nums1[i]<nums2[j]){
						merge.push_back(nums1[i]);
						i++;
					}else{
						merge.push_back(nums2[j]);
						j++;
					}	
				}
				
				if(i<nums1.size()){
					for(;i<nums1.size();i++){
						merge.push_back(nums1[i]);
					}
				}
				
				if(j<nums2.size()){
					for(;j<nums2.size(); j++){
						merge.push_back(nums2[j]);
					}
				}
			}
		}
		if(merge.size()%2!=0){
			return merge[merge.size()/2];
		}else{
			return ( merge[merge.size()/2] + merge[merge.size()/2-1]) / 2.0;
		}
    }
};
