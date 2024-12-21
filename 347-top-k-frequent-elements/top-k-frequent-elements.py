class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ct = Counter(nums)
        l = [nb for nb, app in sorted(ct.items(),key=lambda vl : vl[1],reverse=True)]
        return (l[:k])
        