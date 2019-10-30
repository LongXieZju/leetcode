class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            mid = (lo + hi)>>1
            if nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid
            if nums[mid] < nums[mid + 1]:
                lo = mid + 1
            if nums[mid] > nums[mid + 1]:
                hi = mid - 1
        return hi

nums = [1,2]
s = Solution()
result = s.findPeakElement(nums)
print(result)