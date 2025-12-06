def factorial_recursive(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError("Число должно быть целым")
    if n < 0:
        raise ValueError("Число должно быть положительным")

    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)