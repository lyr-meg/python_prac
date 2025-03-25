class Solution:
    def isValid(self, s: str) -> bool:
        # ([)], stack will be [(], [[, (]
        stack = []
        valid_dict = {"(":")", "{":"}", "[":"]"}
        for i in range(len(s)):
            char = s[i]
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
            else:
                if len(stack) != 0:
                    char_popped = stack.pop()
                    if valid_dict[char_popped] != char:
                        return False
                else:
                    return False
        return stack == []
                            
# time complexity: O(n), because we are iterating through the string once
# space complexity: O(n), because we are using a stack to store the opening brackets