def factorial(n: int) -> int:
    p = 1
    for i in range(2, n + 1):
        p *= i
    return p