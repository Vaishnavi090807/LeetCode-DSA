class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mini=nums[0]
        maxi=nums[0]
        missing=[]
        for i in range(0,len(nums)):
            if(nums[i]<=mini):
                mini=nums[i]
            if(nums[i]>=maxi):
                maxi=nums[i]
        for i in range(mini+1,maxi):
            if i not in nums:
                missing.append(i)
        return missing
            