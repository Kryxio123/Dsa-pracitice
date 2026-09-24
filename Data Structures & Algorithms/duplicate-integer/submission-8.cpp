class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        bool status = false;
        for(size_t i=0;i < nums.size(); i++){
            for(size_t j=i+1;j<nums.size();j++){
                if (nums[i] == nums[j]){
                    status = true;
                    return status;
                }
            }
        }
        if (status != true){
            return status;
        }
    }
};