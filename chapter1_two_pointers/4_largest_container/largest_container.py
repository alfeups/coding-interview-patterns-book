# area=min(h[i],h[j])×(j−i)
from typing import List

def largest_container(heights: List[int]) -> int:
    largest_container = 0

    for left in range(len(heights)):
        for right in range(len(heights) - 1, 0 , -1):
            if heights[left] > heights[right]:
                area = heights[right] * (right - left)
                if area > largest_container:
                    largest_container = area
            elif heights[left] < heights[right]:
                area = heights[left] * (right - left)
                if area > largest_container:
                    largest_container = area
            elif heights[left] == heights[right]:
                area = heights[left] * (right - left)
                if area > largest_container:
                    largest_container = area
                break

    return largest_container
                    
# Input: heights = [2, 7, 8, 3, 7, 6]
# Output: 24

heights = [2, 7, 8, 3, 7, 6]
print(largest_container(heights))