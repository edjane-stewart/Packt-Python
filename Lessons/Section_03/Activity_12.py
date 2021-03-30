stored = {0: 0, 1: 1}  # We set the first 2 terms of the Fibonacci sequence here.

def fibonacci_dynamic(n):
    if n in stored:
        return stored[n]
    else:
        stored[n] = fibonacci_dynamic(n - 2) + fibonacci_dynamic(n - 1)
        return stored[n]

result = fibonacci_dynamic(100)
print(result)