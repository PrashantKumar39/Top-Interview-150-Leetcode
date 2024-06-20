class Solution:
    def trap(self, height):
        if not height:
            return 0
        
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n
        
        # Fill left_max array
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])
        
        # Fill right_max array
        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])
        
        # Calculate the total trapped water
        total_water = 0
        for i in range(n):
            total_water += min(left_max[i], right_max[i]) - height[i]
        
        return total_water

# Example Usage
solution = Solution()
print(solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  
print(solution.trap([4, 2, 0, 3, 2, 5])) 
