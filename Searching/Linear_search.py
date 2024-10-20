def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [1, 2, 3, 4, 5]
print(linear_search(arr, 4))  # Output: 3 (index of element 4)
print(linear_search(arr, 7))  # Output: -1 (element not found)