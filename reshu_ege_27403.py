for s in range(1_000_000, 0, -1):
    s1 = s // 10
    n = 1
    while s1 < 51:
        s1 = s1 + 5
        n = n * 2
    if n == 64:
        print(s)
        break