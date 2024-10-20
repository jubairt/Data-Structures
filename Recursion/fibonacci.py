#  Fibinocci calculation
def fibonacci(n):
    if n == 0:  # Base case
        return 0
    elif n == 1:  # Base case
        return 1
    else:  # Recursive case
        return fibonacci(n - 1) + fibonacci(n - 2)

# Test case
n = 6
result = fibonacci(n)
print(f'The {n}-th Fibonacci number is: {result}')  # Output: The 6-th Fibonacci number is: 8