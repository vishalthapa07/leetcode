class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            total = 0
            restList = range(i+1, len(nums))
            for j in restList:
                total = nums[i]+nums[j]
                if total == target:
                    return [i,j]
  
            

                
