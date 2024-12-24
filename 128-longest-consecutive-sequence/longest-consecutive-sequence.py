class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nb_set = set(nums)
        long_cons = 0

        for val in nums:
            if val in nb_set and (val - 1) not in nb_set:
                nb = val
                cons = 0
                while nb in nb_set:
                    nb_set.remove(nb)
                    nb += 1
                    cons += 1
                long_cons  = max(long_cons,cons)
        
        return(long_cons)
        