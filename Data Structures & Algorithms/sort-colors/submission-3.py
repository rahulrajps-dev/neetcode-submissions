class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = 0
        blue = len(nums)-1
        scan = 0
        while scan <= blue:
            if nums[scan] == 2:
                nums[blue],nums[scan] = nums[scan],nums[blue]
                blue -= 1
            elif nums[scan] == 0:
                nums[red],nums[scan] = nums[scan],nums[red]
                red += 1
                scan += 1
            else:
                scan += 1
                    
            