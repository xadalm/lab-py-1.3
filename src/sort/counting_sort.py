def counting_sort(a: list[int]) -> list[int]:
    if not a: return a
    min_val, max_val = min(a), max(a)
    count = [0] * (max_val - min_val + 1)
    for n in a:
        count[n - min_val] += 1
    result = []
    for i, freq in enumerate(count):
        result.extend([i + min_val] * freq)
    return result