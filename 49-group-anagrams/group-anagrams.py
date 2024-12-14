from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dd = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            dd[key].append(s)
        return list(dd.values())
        