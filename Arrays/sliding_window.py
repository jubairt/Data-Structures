# Sliding Window
def max_sum_subarray(arr, k):
    n = len(arr)
    
    # Initialize the window sum and the maximum sum
    window_sum = sum(arr[:k])  # Sum of the first 'k' elements
    max_sum = window_sum
    
    # Slide the window from the start of the array to the end
    for i in range(k, n):
        # Slide the window by subtracting the element going out and adding the one coming in
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

# Example usage
arr = [2, 1, 5, 1, 3, 2]
k = 3
print("Maximum sum of subarray of size", k, "is:", max_sum_subarray(arr, k))

# Maximum sum of subarray of size 3 is: 9

# =====================================================================================