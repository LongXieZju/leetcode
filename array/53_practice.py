class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: return nums[0]

        sum_current = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            sum_current = max(nums[i], nums[i] + sum_current)
            max_sum = sum_current if max_sum < sum_current else max_sum

        return max_sum

nums = [-2,1,-3,4,-1,2,1,-5,4]
s = Solution()
result = s.maxSubArray(nums)
print(result)
