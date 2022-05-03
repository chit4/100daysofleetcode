#https://leetcode.com/problems/two-sum/
#https://leetcode.com/submissions/detail/692063084/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res=[[nums.index(val),nums[ind +1:].index(target-val)+ ind+1] for ind,val in enumerate(nums) if target -val in nums[ind +1:]]
        return res[0]
