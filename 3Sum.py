class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, n - 1

            while l < r:
                if nums[l] + nums[r] + num > 0:
                    r -= 1
                elif nums[l] + nums[r] + num < 0:
                    l += 1
                
                else:
                    res.append([nums[l], nums[r], num])
                    l += 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1



       
            
        return res
        



