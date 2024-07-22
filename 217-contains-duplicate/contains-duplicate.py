class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        u_numbers = set(nums);
        return (len(u_numbers) != len(nums));

        