class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answ = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j, k = i + 1, len(nums) - 1

            while j < k:
                thr_s = nums[i] + nums[j] + nums[k]
                if thr_s > 0:
                    k -= 1
                elif thr_s < 0:
                    j += 1
                else:
                    answ.append([nums[i], nums[j], nums[k]])
                    j += 1        
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

        return answ