def max_area(height):
    max_area = 0
    left = 0
    right = len(height) - 1
    while left < right:
        width = right - left
        container_height = min(height[left], height[right])
        current_area = width * container_height
        max_area = max(max_area, current_area)
        if height[left] < height[right]:
            left += 1
        else:
                right -= 1
                return max_area
height = [1,5,4,3]
result = max_area(height)
print(result)
