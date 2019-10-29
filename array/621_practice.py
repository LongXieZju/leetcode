class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        max_num = 0
        max_count = 0
        counter = [0]*26
        for c in tasks:
            counter[ord(c) - ord('A')] += 1
            if max_count == counter[ord(c) - ord('A')]:
                max_num += 1
            if max_count < counter[ord(c) - ord('A')]:
                max_count = counter[ord(c) - ord('A')]
                max_num = 1

        part_count = max_count - 1
        empty_slots = part_count * (n - max_num + 1)
        availale_task = len(tasks) - max_num * max_count
        idles = max(0, empty_slots - availale_task)
        return idles + len(tasks)

n = 2        
tasks = ["A","A","A","B","B","B"]
s = Solution()
result = s.leastInterval(tasks, n)
print(result)