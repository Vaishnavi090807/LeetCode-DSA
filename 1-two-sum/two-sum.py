class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen={}
        for i in range(0,len(nums)):
            needed=target-nums[i]
            if needed in seen:
                return [seen[needed],i]
            seen[nums[i]]=i