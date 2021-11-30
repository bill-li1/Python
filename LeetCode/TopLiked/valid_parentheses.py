class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
                '(': ')',
                '[': ']',
                '{': '}',
                }
        for c in s:
            if c in pairs:
                stack.append(c)
            elif not stack:
                return False
            else:
                top = stack.pop()
                if c != pairs[top]:
                    return False
        if not stack:
            return True
        return False
