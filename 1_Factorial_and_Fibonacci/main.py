import timeit

# Factorial functions
def factorial_iterative(n):
    """Computes factorial of n iteratively."""
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

def factorial_recursive(n):
    """Computes factorial of n recursively."""
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n-1)

# Fibonacci functions
def fibonacci_iterative(n):
    """Computes the nth Fibonacci number iteratively."""
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def fibonacci_recursive(n):
    """Computes the nth Fibonacci number recursively."""
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-2) + fibonacci_recursive(n-1)

def compare_functions(functions, numbers):
    """Compares the execution time of functions for a list of numbers."""
    for name, func in functions.items():
        print(f"--- {name} ---")
        for n in numbers:
            # Use timeit to get execution time
            stmt = f"{func.__name__}({n})"
            setup = f"from __main__ import {func.__name__}"
            execution_time = timeit.timeit(stmt, setup=setup, number=1000)
            print(f"Input: {n}, Time: {execution_time:.6f} seconds")
        print("\\n")

if __name__ == "__main__":
    factorial_functions = {
        "Factorial Iterative": factorial_iterative,
        "Factorial Recursive": factorial_recursive
    }
    
    fibonacci_functions = {
        "Fibonacci Iterative": fibonacci_iterative,
        "Fibonacci Recursive": fibonacci_recursive
    }
    
    # Numbers for testing
    factorial_numbers = [5, 10, 15, 20]
    fibonacci_numbers = [5, 10, 15, 20, 25, 30]

    print("### Factorial Performance ###")
    compare_functions(factorial_functions, factorial_numbers)
    
    print("### Fibonacci Performance ###")
    compare_functions(fibonacci_functions, fibonacci_numbers)
