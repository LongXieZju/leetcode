class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        index = 0
        while index < len(nums):
            while nums[index] != 0 and nums[index] != index + 1:
                value = nums[index]
                if value == nums[value - 1]:
                    nums[index] = 0
                else:
                    nums[index] = nums[value - 1]
                    nums[value - 1] = value
            index += 1

        result = []
        for i in range(len(nums)):
            if nums[i]== 0:
                result.append(i+1)

        return result


            

nums = [4,3,2,7,8,2,3,1]       
s = Solution()
result = s.findDisappearedNumbers(nums)
print(result)
