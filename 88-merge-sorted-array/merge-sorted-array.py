class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        totalLength = m+n
        nums3 = nums1[:m] + nums2[:n]
        sortedArray = sorted(nums3)
        print(sortedArray)
        nums1[:totalLength] = sortedArray