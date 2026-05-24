class Solution:
    def twoSum(self, nums, target):
        mp = {}

        for i in range(len(nums)):
            remain = target - nums[i]

            if remain in mp:
                return [mp[remain], i]

            mp[nums[i]] = i
