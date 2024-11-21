class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for ch in s:
            if ch in "([{":
                stack.append(ch)
            else:
                if (
                    not stack
                    or (ch == "]" and stack[-1] != "[")
                    or (ch == ")" and stack[-1] != "(")
                    or (ch == "}" and stack[-1] != "{")
                ):
                    return False
                stack.pop()
        return not stack
        