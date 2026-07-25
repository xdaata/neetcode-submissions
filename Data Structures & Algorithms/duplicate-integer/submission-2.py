class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
            k = len(nums)
            s = set(nums)
            return k != len(s)