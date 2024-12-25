class Solution:
    def isPalindrome(self, s: str) -> bool:
        k = "".join(c for c in s.lower() if c.isalnum())
        return k == k[::-1]
        