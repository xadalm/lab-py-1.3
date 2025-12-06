def bubble_sort(a: list[int]) -> list[int]:
    k = False
    for i in range(0, len(a) - 1):
        if a[i] > a[i + 1]: 
            a[i], a[i + 1] = a[i + 1], a[i]
            k = True
    if k == False: return a
    return bubble_sort(a)