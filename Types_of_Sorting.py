
# you can use this to sort numbers or strings

def bubble_sort(arr):
    size = len(arr)-1

    for i in range(size):
        swapped = False
        for j in range(size-i):
            if arr[j] > arr[j+1]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp
                swapped = True
        
        if not swapped:# If we do this, when the arr are already sorted, it will have time complexity o(n), otherwise o(n^2)
            break

# Sorting numbers
numbers = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(numbers)
print("Sorted numbers:", numbers)

# Sorting strings
strings = ['apple', 'orange', 'banana', 'grape', 'pear']
bubble_sort(strings)
print("Sorted strings:", strings)

# Output:
# Sorted numbers: [11, 12, 22, 25, 34, 64, 90]
# Sorted strings: ['apple', 'banana', 'grape', 'orange', 'pear']

# 

# ------------------------------------------------------------------------------------------------------------

def insertion_sort(arr):
    for i in range(1, len(arr)):
        anchor = arr[i]
        j = i - 1
        while j >= 0 and anchor < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = anchor
    print(arr)  # Print the sorted list within the same cell

# Testing the function with a sample list
sample_list = [9, 5, 1, 4, 3]
insertion_sort(sample_list)  # Directly calling the function to print the output

# Expected Output: [1, 3, 4, 5, 9]


# ------------------------------------------------------------------------------------------------------------

def selection_sort(arr):
    size = len(arr)-1
    for i in range(size):
        min_index = i
        for j in range(min_index + 1, size+1):
            if arr[j] < arr[min_index]:
                min_index = j
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    print(arr)  # Print the sorted array within the same cell

# Testing the function with a sample array
sample_array = [64, 25, 12, 22, 11]
selection_sort(sample_array)  # Directly calling the function to print the output

# Expected Output: [11, 12, 22, 25, 64]


# ------------------------------------------------------------------------------------------------------------

def divide(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left, right = divide(lst[:mid]), divide(lst[mid:])
    return merge(left, right)


def merge(left, right):
    merged = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


print(divide([1, 3, 5, 2, 10, 9, 87, 6]))

# ------------------------------------------------------------------------------------------------------------

def quick(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[0]
    print(pivot)
    right = []
    left = []
    pivot_val = []
    for i in lst:   
        if i > pivot:
            right.append(i)
        elif i < pivot:
            left.append(i)
        else:
            pivot_val.append(i)  # handle duplicate values also
    return quick(left) + pivot_val + quick(right)


print(quick([1, 3, 4, 4, 2, 0]))

# ------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------