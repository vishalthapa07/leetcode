class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        newSet = {}
        for i in nums:
            if i in newSet:
                newSet[i] +=1
            else:
                newSet[i] = 1

        newList = []
        for key, value in newSet.items():
            n = 0
            for j in range(value):
                if n < 2:
                    newList.append(key)
                    n = n+1
        
        for m in range(len(newList)):
            nums[m] = newList[m]
        print(nums[:len(newList)])
        return len(newList)
            

        