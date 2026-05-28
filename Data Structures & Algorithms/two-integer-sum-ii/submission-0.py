class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l, r = 0, len(numbers) - 1

        while l < r:
            sumOfnums = numbers[l] + numbers[r]

            if sumOfnums == target:
                return [l+1, r + 1]

            if sumOfnums < target:
                l +=1
            
            if sumOfnums > target:

                r -=1
        