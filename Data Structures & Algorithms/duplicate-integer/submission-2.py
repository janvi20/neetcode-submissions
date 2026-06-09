class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setN = []
        for i in range(len(nums)):
            if nums[i] not in setN:
                setN.append(nums[i])
            else:
                return True
        return False