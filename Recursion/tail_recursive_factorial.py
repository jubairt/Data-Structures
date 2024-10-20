# tail factorial recursion
def tail_recursive_factorial(n, accumulator=1):
    if n == 0:  # Base case
        return accumulator
    else:
        return tail_recursive_factorial(n - 1, n * accumulator)  # Recursive call with updated accumulator

# Test case
print(tail_recursive_factorial(5))  # Output: 120