class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        wanted = {}
        for i in range(len(nums)):
            if nums[i] in wanted:
                return [wanted[nums[i]], i]
            else:
                wanted[target - nums[i]] = i
