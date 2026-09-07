class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}

        for i in range(len(nums)):
            seen[nums[i]]=i
        for i in range(len(nums)):
            pair=target-nums[i]
            if pair in seen:
                if i!=seen[pair]:
                    return [i,seen[pair]]

        return nums
        