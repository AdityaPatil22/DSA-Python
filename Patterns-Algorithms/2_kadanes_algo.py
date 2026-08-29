# Kadane's Algorithm is used to find the maximum sum of a contiguous subarray within a one-dimensional array of numbers.

# Step-by-step Logic
# Initialize:
# - currentSum → max sum ending at current index
# - maxSum → overall maximum sum found so far
# Traverse the array:
# - Update currentSum
# - Update maxSum if currentSum is larger
# Return maxSum


def kadanes_algorithm(arr):
    current_sum = arr[0]
    max_sum = arr[0]

    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)

    return max_sum

def kadanes_algorithm(nums):
    max_sum = float('-inf')
    curr = 0
    for num in nums:
        curr += num    
        if curr > max_sum:
            max_sum = curr
                
        if curr < 0:
            curr = 0
    return max_sum
