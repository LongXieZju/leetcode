class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 0
        while index < len(nums):
            while nums[index] != 0 and nums[index] != index + 1:
                value = nums[index]
                if value > len(nums) or value == nums[value - 1] or value < 0:
                    nums[index] = 0
                else:
                    nums[index] = nums[value - 1]
                    nums[value - 1] = value
            index += 1
        for i in range(len(nums)):
            if nums[i] == 0:
                return i + 1
        return len(nums) + 1

nums = [1,2,3,4]
s = Solution()
result = s.firstMissingPositive(nums)
print(result)
