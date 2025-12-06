def bucket_sort(a: list[int]) -> list[int]:
    if not a:
        return a
    mn = min(a)
    mx = max(a)
    # если все элементы равны, деления на ноль не будет — просто вернуть копию
    if mn == mx:
        return a.copy()
    n = len(a)
    buckets = [[] for _ in range(n)]
    for x in a:
        # индекс в диапазоне [0, n-1]
        idx = int((x - mn) / (mx - mn) * (n - 1))
        buckets[idx].append(x)
    result = []
    for b in buckets:
        result.extend(sorted(b))
    return result