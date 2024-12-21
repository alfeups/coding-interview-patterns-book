from typing import List

'''
def shift_zeros_to_the_end(nums: List[int]) -> None:
    left, right = 0, len(nums) - 1

    while left < right:
        if nums[left] == 0:
            tmp = 0
            for i in range(left, len(nums) - 1):
                nums[i] = nums[i + 1]
            nums[len(nums) - 1] = tmp
            right -= 1
        else:
            left += 1
'''

def shift_zeros_to_the_end(nums: List[int]) -> None:
    left = 0
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1


nums =  [0, 1, 0, 3, 2] #[0,0,1,2]
print(shift_zeros_to_the_end(nums))