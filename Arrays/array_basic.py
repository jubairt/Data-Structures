arr = [1, 2, 3, 4, 5]
arr.append(6)  # Insert 6 at the end
print(arr)  # Output: [1, 2, 3, 4, 5, 6]

arr.insert(2, 10)  # Insert 10 at index 2
print(arr)  # Output: [1, 2, 10, 3, 4, 5, 6]

arr.pop()  # Remove the last element
print(arr)  # Output: [1, 2, 10, 3, 4, 5]

arr.pop(2)  # Remove element at index 2
print(arr)  # Output: [1, 2, 3, 4, 5]

# ---------------------------------------------


def reverse_array(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]  # Swap the elements
        start += 1
        end -= 1
    return arr

arr = [1, 2, 3, 4, 5]
print(reverse_array(arr))  # Output: [5, 4, 3, 2, 1]

# ---------------------------------------------

def find_largest(arr):
    max_element = arr[0]  # Assume the first element is the largest
    for element in arr:
        if element > max_element:
            max_element = element
    return max_element

arr = [1, 2, 3, 4, 5]
print(find_largest(arr))  # Output: 5

# ---------------------------------------------

def find_smallest(arr):
    min_element = arr[0]  # Assume the first element is the smallest
    for element in arr:
        if element < min_element:
            min_element = element
    return min_element

arr = [1, 2, 3, 4, 5]
print(find_smallest(arr))  # Output: 1


# ===================================================