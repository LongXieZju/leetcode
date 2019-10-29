class Solution1(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        count = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                target = nums[i] + nums[j]
                lo = j + 1
                hi = len(nums) - 1
                while lo <= hi:
                    mid = (lo+hi)>>1
                    if target > nums[mid]:
                        lo = mid + 1
                    else:
                        hi = mid - 1
                count += hi-j
        return count

class Solution2(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

nums = [2,2,3,4,4]
s = Solution2()
result = s.triangleNumber(nums)
print(result)