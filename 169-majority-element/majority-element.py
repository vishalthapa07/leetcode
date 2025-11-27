class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for i in nums:
            # print("test..", i)
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        
        item = max(count, key = count.get)
        return item