class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> mp;

        int diff;

        for(int i = 0; i < nums.size(); i++){
            diff = target - nums[i];
            if (mp.count(diff)){
                return {mp[diff],i};
            }
            mp[nums[i]] = i;
        }
        
        return {};
    }
};