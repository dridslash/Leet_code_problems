class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
         std::unordered_map<int,int>set_nb;
        int n_size = nums.size();

        for(int i = 0; i < n_size ; i++){
                if (set_nb.count(nums[i])){
                        if (abs(i - set_nb[nums[i]]) <= k)
                            return true;
                }
                set_nb[nums[i]] = i;
        }
        return false;
    }
};