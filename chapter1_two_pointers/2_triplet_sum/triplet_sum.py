from typing import List

def triplet_sum(nums: List[int]) -> List[List[int]]:
    triplets = []
    nums.sort()
    n = len(nums)

    if nums[0] > 0 or len(nums) <= 1:
        return triplets

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                    triplets.append(triplet)

    return [list(triplet) for triplet in triplets]



nums = [0, -1, 2, -3, 1] # -3, -1, 0, 1, 2
print(triplet_sum(nums))