class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = set()

        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                left = j + 1
                right = n - 1
                while left < right:
                    curr_sum = nums[i] + nums[j] + nums[left] + nums[right]

                    if curr_sum == target:
                        res.add((nums[i], nums[j], nums[left], nums[right]))
                        left += 1
                        right -= 1
                    elif curr_sum < target:
                        left += 1
                    else:
                        right -= 1

        return [list(q) for q in res]