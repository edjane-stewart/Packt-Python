def factorial_iterative(n):
        result = 1
        for i in range(n):
            result *= i + 1
        return result


def factorial_recursive(n):
        if n == 1 or n == 0:
            return 1
        else:
            return n * factorial_recursive(n - 1)    

result = factorial_iterative(5)
print(result)

result2 = factorial_recursive(5)
print(result2)