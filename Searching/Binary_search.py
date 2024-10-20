# Binary Search
def binary_search(arr, target):
    # Set the initial left and right pointers
    left = 0
    right = len(arr) - 1
    
    # Continue searching while left pointer is less than or equal to right pointer
    while left <= right:
        # Calculate the middle index
        mid = (left + right) // 2
        
        # Check if the middle element is the target
        if arr[mid] == target:
            return mid  # Return the index if found
        elif arr[mid] < target:
            left = mid + 1  # Move to the right half
        else:
            right = mid - 1  # Move to the left half
            
    return -1  # Return -1 if the target is not found

# Test Case
sorted_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]  # A sorted array
target_number = 7  # The target number we want to find

# Call the function and store the result
result = binary_search(sorted_array, target_number)

# Output the result
if result != -1:
    print(f'Target {target_number} found at index: {result}.')  # Output: Target 7 found at index: 3.
else:
    print(f'Target {target_number} not found in the array.')