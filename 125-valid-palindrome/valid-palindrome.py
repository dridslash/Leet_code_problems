class Solution:
    def isPalindrome(self, s: str) -> bool:
        f = 0;
        l = len(s) - 1;
        for _ in range(len(s)):
            if (s[f].isalnum() == False):
                f += 1;
                continue;
            elif (s[l].isalnum() == False):
                l -= 1;
                continue;
            if (s[f].lower() != s[l].lower()):
                return (False);
            f += 1;
            l -= 1;
        return (True);

        