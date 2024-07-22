class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        final_set=set()
        for i in nums:
            if i not in final_set:
                final_set.add(i)
            else:
                return True
        return False

        