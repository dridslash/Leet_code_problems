class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lent = len(nums)
        proc = [1] * lent
        for i in range(1,lent):
            proc[i] = proc[i - 1] * nums[i - 1]
        rproc = nums[-1]
        for i in range(lent - 2, -1 , -1):
            proc[i] *= rproc
            rproc *= nums[i]
        return proc
        