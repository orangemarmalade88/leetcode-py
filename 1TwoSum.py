class Solution(object):
    def twoSum(self, nums, target):
        dict = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in dict:
                return [dict[comp], i]
            else:
                dict[nums[i]] = i
        return [-1, -1]
    