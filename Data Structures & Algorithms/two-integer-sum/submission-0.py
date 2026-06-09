class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliment = 0
        data = {}

        for i, n in enumerate(nums):
            compliment = target - n

            if compliment in data:
                return([data.get(compliment),i])
            
            data[n] = i
            
        return []