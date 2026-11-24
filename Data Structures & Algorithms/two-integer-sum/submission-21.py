class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        storage=dict()
        for i, num in enumerate(nums):
            need = target-num
            if need in storage:
                return [storage[need], i]
            storage[num] = i
            
            