def radix_sort(a: list[int]) -> list[int]:
    if not a:
        return a
    for i in range(len(str(max(a)))):
        neg, pos = [[] for _ in range(10)], [[] for _ in range(10)]
        for j in range(len(a)):
            if a[j] < 0: neg[a[j] // (10 ** i) % 10].append(a[j])
            if a[j] >= 0: pos[a[j] // (10 ** i) % 10].append(a[j])
        a, m = [], []
        m.extend(neg)
        m.extend(pos)
        for k in range(len(m)): a.extend(m[k])
    return a