# Two pointer
def two_pointer_search(arr, target):
    left = 0                     # Start pointer at the beginning
    right = len(arr) - 1        # End pointer at the end of the array

    while left <= right:
        print(f"Checking indices: left={left} (value: {arr[left]}), right={right} (value: {arr[right]})")
        
        if arr[left] == target:
            print(f"Found target {target} at index {left}")
            return left          # Target found at left index
        if arr[right] == target:
            print(f"Found target {target} at index {right}")
            return right         # Target found at right index
        
        left += 1                # Move left pointer to the right
        right -= 1               # Move right pointer to the left
    
    print(f"Target {target} not found in the array")
    return -1                   # Target not found

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
two_pointer_search(arr, target)

# output
# Checking indices: left=0 (value: 1), right=8 (value: 9)
# Checking indices: left=1 (value: 2), right=7 (value: 8)
# Checking indices: left=2 (value: 3), right=6 (value: 7)
# Checking indices: left=3 (value: 4), right=5 (value: 6)
# Checking indices: left=4 (value: 5), right=4 (value: 5)
# Found target 5 at index 4


# ========================================================================
