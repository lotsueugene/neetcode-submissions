class Solution:
    def findMin(self, nums: List[int]) -> int:

        sorted_num = sorted(nums)
        return min(sorted_num)
        