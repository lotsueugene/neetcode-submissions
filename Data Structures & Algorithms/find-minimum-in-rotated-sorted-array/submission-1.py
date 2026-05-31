class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums) -1 

        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]: #mid value greater, means the min is on the right
                l = mid + 1 #move the left pointer forward
            else:
                r = mid 
        return nums[l]
        