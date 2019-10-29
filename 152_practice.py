class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        max_num = nums[0]
        imax = max_num
        imin = max_num
        for i in nums[1:]:
            if i < 0:
                imax, imin = imin, imax
            imax = max(i, i*imax)
            imin = min(i, i*imin)

            max_num = max(max_num, imax)

        return max_num
        
        
s = Solution()
nums = [-2, 3, 5, -3, -5, 3, -1]
result = s.maxProduct(nums)
print(result)