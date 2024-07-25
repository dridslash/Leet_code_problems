class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_s = s.lower();
        concat ="";
        for c in lower_s:
            if c.isalnum():
                concat = concat + c;
        if(concat == concat[::-1]):
            return (True);
        return (False);

        