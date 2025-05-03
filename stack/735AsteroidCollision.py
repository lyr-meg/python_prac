class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for a in asteroids:
            while stack and a<0<stack[-1]:
                if stack[-1] < -a:
                    stack.pop()
                    continue
                elif stack[-1] == -a:
                    stack.pop()
                break
            else:
                stack.append(a)
        
        return stack

# Time Complexity: O(n), where n is the length of the input list. Each asteroid is processed once.
# Space Complexity: O(n), for storing asteroids in the stack.