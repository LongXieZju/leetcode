import collections
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1 and nums[0] != k:
            return 0
        if len(nums) == 1 and nums[0] == k:
            return 1
        count = 0
        cur_sum = 0
        hashmap = collections.Counter()
        hashmap[0] = 1
        for i in nums:
            cur_sum += i
            remaind = cur_sum - k
            count += hashmap[remaind]
            hashmap[cur_sum] += 1
        return count

nums = [1,1,1]
k = 2
s = Solution()
result = s.subarraySum(nums, k)
print(result)