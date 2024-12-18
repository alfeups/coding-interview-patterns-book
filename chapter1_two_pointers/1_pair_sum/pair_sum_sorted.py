# https://bytebytego.com/exercises/coding-patterns/two-pointers/pair-sum-sorted
from typing import List

def pair_sum_sorted(nums: List[int], target: int) -> List[int]:
    if len(nums) == 0:
        return []

    first = nums[0]
    last = nums[len(nums) - 1]

    if first + last == target:
        return [0,len(nums) - 1]
    for i in range(0, len(nums) - 1, 1):
        for j in range(len(nums) - 1, 0, -1):
            if nums[i] + nums[j] == target:
                return [i, j]
    return[]

nums = [2,3]
target = 5

result = pair_sum_sorted(nums, target)

print(result)