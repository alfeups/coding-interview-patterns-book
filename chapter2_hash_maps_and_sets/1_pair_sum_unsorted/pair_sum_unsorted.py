'''
Pair Sum - Unsorted
Given an array of integers, return the indexes of any two numbers that add up to a target.
The order of the indexes in the result doesn't matter.
If no pair is found, return an empty array.

Example:

Input: nums = [-1, 3, 4, 2], target = 3
Output: [0, 2]
Explanation: nums[0] + nums[2] = -1 + 4 = 3

Constraints:
The same index cannot be used twice in the result.

BF:
def pair_sum_unsorted(nums: List[int], target: int) -> List[int]:
    meu_mapa = {}
    for i in range(len(nums) - 1):
        meu_mapa[i] = nums[i]
    for j in range(len(meu_mapa)):
        if target + nums[j] in meu_mapa:
            return [j, nums[j] + target]
    return []

'''
from typing import List

def pair_sum_unsorted(nums: List[int], target: int) -> List[int]:
    meu_mapa = {}
    for index, valor in enumerate(nums):
        o_que_falta_para_target = target - valor
        if o_que_falta_para_target in meu_mapa:
            return [meu_mapa[o_que_falta_para_target], index]
        meu_mapa[valor] = index
    return []

nums = [-1,3,4,2]
target = 6
print(pair_sum_unsorted(nums,target))
