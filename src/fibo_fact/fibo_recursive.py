def fibo_recursive(n: int) -> int:
    if n < 0: raise ValueError("n принимает только неотрицательные значения")
    if n <= 1: return n
    return fibo_recursive(n - 2) + fibo_recursive(n - 1)