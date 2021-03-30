def fibonacci_recursive(n):
        if n == 1 or n == 0:
            return 1
        else:
            return n * fibonacci_recursive(n - 1)    

result = fibonacci_recursive(3)
print(result)

result2 = fibonacci_recursive(10)
print(result2)