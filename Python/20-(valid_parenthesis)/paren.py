class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {
            ')': '(',
            '}': '{',
            ']': '[',
        }

        for c in s:
            if c not in map.keys():
                stack.append(c)
                continue
            if len(stack) > 0 and stack[-1] == map[c]:
                stack.pop()
            else:
                return False

        return not stack


checkparen = Solution()
output = checkparen.isValid(")[]{}")
print(output)
