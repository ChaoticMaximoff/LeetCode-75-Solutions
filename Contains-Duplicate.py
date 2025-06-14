class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums = sorted(nums)

        for i in range(1, len(nums) - 1):
            if nums[i] == nums[i - 1] or nums[i] == nums[i + 1]:
                return True

        if len(nums) == 2:
            return nums[0] == nums[1]

        return False