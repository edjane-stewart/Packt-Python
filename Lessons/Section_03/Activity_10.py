def fibonacci_iterative(n):
    previous = 0
    current = 1
    for i in range(n - 1):
        current_old = current
        current = previous + current
        previous = current_old
    return current

print(fibonacci_iterative(3))
print(fibonacci_iterative(10))