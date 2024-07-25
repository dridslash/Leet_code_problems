class Solution:
    def isPalindrome(self, s: str) -> bool:
        concat = [chata for chata in s.lower() if (chata.isalnum())];
        return(concat == concat[::-1]);

        