class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        storage_dict = {}
        for i, num in enumerate(nums):
            difference = target - num
            if difference in storage_dict:
                return [storage_dict [difference], i]
            storage_dict[num] = i