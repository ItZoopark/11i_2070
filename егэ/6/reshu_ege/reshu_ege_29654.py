for s in range(-100, 100):
    s1 = s
    n = 4
    while s1 < 37:
        s1 = s1 + 3
        n = n * 2
    if n == 128:
        print(s)
        break