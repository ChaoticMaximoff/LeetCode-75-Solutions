class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        all_prod = 1
        answer = []
        zeroes = nums.count(0)
        if zeroes > 1:
            for num in nums:
                answer.append(0)
            return answer

        for num in nums:
            if num != 0:
                all_prod *= num

        for num in nums:
            if num != 0 and not zeroes:
                answer.append(int(all_prod/num))
            elif num != 0:
                answer.append(0)
            else:
                answer.append(all_prod)

        return answer
        