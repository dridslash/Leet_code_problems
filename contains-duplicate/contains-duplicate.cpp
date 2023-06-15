class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
         set<int> du_chcker;
        for(int i : nums){
            if (du_chcker.find(i) == du_chcker.end())
                du_chcker.insert(i);
            else
                return true;
        }
        return false;
    }
};