from collections import deque

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        queue = deque([])
        dic = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        for i in range(len(digits)):
            if len(queue) == 0:
                for c in dic[digits[i]]:
                    queue.append(c)
            else:
                while len(queue[0]) == i:
                    prefix = queue.popleft()
                    for c in dic[digits[i]]:
                        queue.append(prefix + c)
        return queue

digits = '23'       
s = Solution()
result = s.letterCombinations(digits)
print(result)
