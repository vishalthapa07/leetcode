class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        resultInSet = set(nums)
        result = sorted(list(resultInSet))
        nums[:len(result)] = result
        return len(result)